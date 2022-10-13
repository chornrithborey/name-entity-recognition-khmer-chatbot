import os


def test_number_of_sentences_are_the_same():
    encoded_dir = "entity-tag"
    tagged_dir = "pos"

    encoded_lengths = {}
    encoded_files = os.listdir(encoded_dir)

    tagged_lengths = {}
    tagged_files = os.listdir(tagged_dir)

    unique_encoded_files = list(set(encoded_files))
    unique_tagged_files = list(set(tagged_files))

    assert len(unique_encoded_files) == len(unique_tagged_files)

    for file in encoded_files:
        with open(f"{encoded_dir}/{file}", "r") as f:
            encoded_lengths[file] = len(f.readlines())

    for file in tagged_files:
        with open(f"{tagged_dir}/{file}", "r") as f:
            tagged_lengths[file] = len(f.readlines())

    for file in encoded_lengths:
        assert encoded_lengths[file] == tagged_lengths[file]
