import os


def all_sentences():
    root_dir = "entity-tag"
    files = os.listdir(root_dir)

    for file in files:
        with open(os.path.join(root_dir, file), "r") as f:
            f.readline()
            for line in f:
                yield line.strip().split(",")[0].strip()

    return files


def get_all_entity_tags():
    entity_tags = set()
    for sentence in all_sentences():
        for word in sentence.split():
            segments = word.split("/")

            assert len(segments) < 3, "Invalid word: {}".format(word)

            if len(segments) == 2:
                assert segments[0] != "", "Empty tag: {}".format(word)
                entity_tags.add(segments[1])

    return entity_tags


def test_tags_are_valid():
    valid_tags = set(
        [
            "B-ROOM",
            "I-ROOM",
            "B-BUILD",
            "I-BUILD",
            "B-PER",
            "I-PER",
            "B-FLOOR",
            "I-FLOOR",
            "B-ORD",
            "I-ORD",
            "B-CAR",
            "I-CAR",
            "B-DATE",
            "I-DATE",
            "B-TIME",
            "I-TIME",
            "B-MONEY",
            "I-MONEY",
            "B-EVE",
            "I-EVE",
            "B-ANN",
            "I-ANN",
            "B-GPE",
            "I-GPE",
            "B-LOC",
            "I-LOC",
            "B-ORG",
            "I-ORG",
            "B-MAJOR",
            "I-MAJOR",
        ]
    )

    for tag in get_all_entity_tags():
        assert tag in valid_tags, "Invalid tag: {}".format(tag)
