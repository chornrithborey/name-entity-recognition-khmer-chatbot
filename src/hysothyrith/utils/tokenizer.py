import os
import re
import pickle
import warnings
import numpy as np

from typing import Union
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

warnings.filterwarnings("ignore")

MAX_SEQ_LENGTH = 1000
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2"

with open("storage/pos_tag_data.pkl", "rb") as f:
    word2id, id2word, tag2id, id2tag = pickle.load(f)


def ignore_class_accuracy(to_ignore=0):
    def ignore_accuracy(y_true, y_pred):
        y_true_class = K.argmax(y_true, axis=-1)
        y_pred_class = K.argmax(y_pred, axis=-1)

        ignore_mask = K.cast(K.not_equal(y_pred_class, to_ignore), "int32")
        matches = K.cast(K.equal(y_true_class, y_pred_class), "int32") * ignore_mask
        accuracy = K.sum(matches) / K.maximum(K.sum(ignore_mask), 1)
        return accuracy

    return ignore_accuracy


def decode(pred_tags, input_sent):
    error = 0
    tmp, seq, pos = [], [], []

    for i, tag in enumerate(pred_tags):
        try:
            if tag == "NS":
                tmp.append(input_sent[i])
            else:
                pos.append(tag)
                if len(tmp) > 0:
                    seq.append("".join(tmp))
                    tmp = []
                tmp.append(input_sent[i])
        except:
            error = error + 1

    if len(tmp) > 0:
        seq.append("".join(tmp))

    return seq, pos


def vector2tag(predictions):
    pred_tags_sents = []
    for pred in predictions:
        pred_tags_sent = []
        for vec in pred:
            try:
                if id2tag[np.argmax(vec)] == "PAD":
                    continue
                pred_tags_sent.append(id2tag[np.argmax(vec)])
            except:
                pass

        pred_tags_sents.append(pred_tags_sent)

    return pred_tags_sents


def test_predict(sentences, model, type_="2d"):
    if type_ == "3d":
        for i, sent in enumerate(sentences):
            sentences[i] = "".join(sentences[i])
            sentences[i] = re.sub(" ", "", sentences[i])
            sentences[i] = re.sub(r"\u200b", "", sentences[i])
            sentences[i] = re.sub(r"\n", "", sentences[i])
    else:
        for i, _ in enumerate(sentences):
            sentences[i] = re.sub(" ", "", sentences[i])
            sentences[i] = re.sub(r"\u200b", "", sentences[i])
            sentences[i] = re.sub(r"\n", "", sentences[i])

    tokenize_sents = []

    for sent in sentences:
        tokenize_sent = []
        for ch in sent:
            try:
                tokenize_sent.append(word2id[ch])
            except:
                tokenize_sent.append(word2id["UNK"])

        tokenize_sents.append(tokenize_sent)

    tokenize_sents = pad_sequences(
        np.asarray(tokenize_sents), maxlen=MAX_SEQ_LENGTH, truncating="post"
    )

    predictions = model.predict(tokenize_sents, verbose=1)

    return predictions


def load_model_(path="storage/bi-lstm_1000_seq.h5"):
    model = load_model(path, compile=False)
    model.compile(
        loss="categorical_crossentropy",
        optimizer="adam",
        metrics=["acc", ignore_class_accuracy(0)],
    )
    return model


tok_model = load_model_()


def tokenize_file_bilstm(f, o):
    with open(f, encoding="utf8") as f:
        lines = [line.strip() for line in f]
    predictions = test_predict(lines, tok_model)
    pred_sents = vector2tag(predictions)
    results = []
    for i, pred_sent in enumerate(pred_sents):
        seq, pos = decode(pred_sent, lines[i])
        result = [s for s in seq]
        results.append(result)

    temp = [" ".join(sentence) for sentence in results]
    sentences = []
    for sent in temp:
        sent = re.sub(
            r"([0-9០-៩]{1,3})\s((,|.)\s([0-9០-៩]{3})(\s))+", r"\1\3\4\5", sent
        )
        sentences.append(sent)
    print("Writing to file: In progress.")
    with open(o, "w+", encoding="utf8") as file_handler:
        for item in sentences:
            file_handler.write("{}\n".format(item))
    print("Word segmentation status: Sucess.")


def tokenize_sentences_bilstm(data):
    lines = [line.strip() for line in data]

    predictions = test_predict(lines, tok_model)
    pred_sents = vector2tag(predictions)

    results = []
    for i, pred_sent in enumerate(pred_sents):
        seq, pos = decode(pred_sent, lines[i])
        result = [s for s in seq]
        results.append(result)

    temp = [" ".join(sentence) for sentence in results]
    sentences = []
    for sent in temp:
        sent = re.sub(
            r"([0-9០-៩]{1,3})\s((,|.)\s([0-9០-៩]{3})(\s))+", r"\1\3\4\5", sent
        )
        sentences.append(sent)
    return sentences


def segment(sentence: str) -> Union[str, list[str]]:
    line = sentence.strip()

    predictions = test_predict([line], tok_model)
    pred_sent = vector2tag(predictions)[0]
    segments, pos = decode(pred_sent, line)

    return [
        re.sub(r"([0-9០-៩]{1,3})\s((,|.)\s([0-9០-៩]{3})(\s))+", r"\1\3\4\5", segment)
        for segment in segments
    ]
