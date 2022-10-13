import os


def test_sentences_are_aligned():
    encoded_dir = os.listdir("entity-tag")

    for file in encoded_dir:
        with open(f"entity-tag/{file}", "r") as f:
            encoded_sentences = f.readlines()

        with open(f"pos/{file}", "r") as f:
            tagged_sentences = f.readlines()

        assert len(encoded_sentences) == len(tagged_sentences)

        for encoded, tagged in zip(encoded_sentences, tagged_sentences):
            encoded_sentence = encoded.split(",")[0].strip().split()
            tagged_sentence = tagged.split(",")[0].strip().split()

            assert len(encoded_sentence) == len(tagged_sentence)
