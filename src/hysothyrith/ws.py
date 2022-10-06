import re

from tensorflow.keras import utils
from tensorflow.keras.layers import (
    GRU,
    LSTM,
    Bidirectional,
    Dense,
    Dropout,
    Embedding,
    Input,
    TimeDistributed,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences

PADDING_IDENTIFIER = "<PAD>"
UNKNOWN_IDENTIFIER = "<UNK>"


def load_dataset():
    with open("storage/hysothyrith/data_km.km-tok.nova", "r") as f:
        lines = f.readlines()
        return [re.sub(r"SNT\.\d+\.\d+\s", "", line).strip() for line in lines]


def build_dictionaries(lines):
    chars = set()
    for line in lines:
        for char in line:
            chars.add(char)

    char2idx = {c: i + 2 for i, c in enumerate(sorted(chars))}
    char2idx[PADDING_IDENTIFIER] = 0
    char2idx[UNKNOWN_IDENTIFIER] = 1

    idx2char = {i: c for c, i in char2idx.items()}

    return char2idx, idx2char


def encode_sequences(char2idx, lines, max_len=100):
    X = []
    y = []

    for line in lines:
        X_line = []
        y_line = []

        for word in line.split(" "):
            X_line += [char2idx.get(c, 1) for c in word]
            y_line += [1] + [-1 for _ in range(len(word) - 1)]

        X.append(X_line)
        y.append(y_line)

    return (
        pad_sequences(sequences=X, maxlen=max_len, padding="pre", value=0),
        pad_sequences(sequences=y, maxlen=max_len, padding="pre", value=0),
    )


def main():
    data = load_dataset()
    char2idx, idx2char = build_dictionaries(data)
    max_seq_len = max([len(line) for line in data])

    X, y = encode_sequences(char2idx, data, max_len=max_seq_len)

    train_size = int(len(X) * 0.8)
    val_size = int(len(X) * 0.1)

    X_train = X[:train_size]
    X_val = X[train_size : train_size + val_size]
    X_test = X[train_size + val_size :]

    y_train = utils.to_categorical(y[:train_size])
    y_val = utils.to_categorical(y[train_size : train_size + val_size])
    y_test = utils.to_categorical(y[train_size + val_size :])

    bidirect_model = Sequential()
    bidirect_model.add(
        Embedding(
            input_dim=len(char2idx),
            output_dim=64,
            input_length=max_seq_len,
            trainable=True,
        )
    )

    bidirect_model.add(Bidirectional(LSTM(64, return_sequences=True)))
    bidirect_model.add(TimeDistributed(Dense(2, activation="softmax")))

    bidirect_model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["acc"]
    )

    bidirect_model.summary()

    bidirect_model.fit(
        X_train,
        y_train,
        batch_size=32,
        epochs=10,
        validation_data=(X_val, y_val),
        verbose=1,
    )

    bidirect_model.save("storage/hysothyrith/bidirect_model.h5")


if __name__ == "__main__":
    main()
