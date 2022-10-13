import os


def test_dataset_split():
    root_dir = "datasets"

    dev_dir = os.path.join(root_dir, "dev")
    test_dir = os.path.join(root_dir, "test")
    train_dir = os.path.join(root_dir, "train")

    for group in [dev_dir, test_dir, train_dir]:
        lengths = []
        for file in os.listdir(group):
            with open(os.path.join(group, file), "r") as f:
                lengths.append(len(f.readlines()))

    assert len(set(lengths)) == 1
