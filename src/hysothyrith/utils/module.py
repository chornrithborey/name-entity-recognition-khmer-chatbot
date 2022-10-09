import csv
import os


def write_module(module, root_dir: str, segmented=False, tagged=False, encoded=False):
    raw_dir = os.path.join(root_dir, "raw")
    segmented_dir = os.path.join(root_dir, "segmented")
    tagged_dir = os.path.join(root_dir, "tagged")
    encoded_dir = os.path.join(root_dir, "encoded")

    intent = module["intent"]
    sentences = module["sentences"]

    for directory in (root_dir, raw_dir, segmented_dir, tagged_dir, encoded_dir):
        if not os.path.exists(directory):
            os.makedirs(directory)

    raw_file_path = os.path.join(raw_dir, "{}.csv".format(intent))
    with open(raw_file_path, "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(["question", "intent"])

        for sentence in sentences:
            writer.writerow([sentence, intent])

    if segmented:
        segmented_file_path = os.path.join(segmented_dir, "{}.csv".format(intent))
        with open(segmented_file_path, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "intent"])

            for sentence in sentences:
                writer.writerow([sentence.segmented(), intent])

    if tagged:
        tagged_file_path = os.path.join(tagged_dir, "{}.csv".format(intent))
        with open(tagged_file_path, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "intent"])

            for sentence in sentences:
                writer.writerow([sentence.tagged(), intent])

    if encoded:
        encoded_file_path = os.path.join(encoded_dir, "{}.csv".format(intent))
        with open(encoded_file_path, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "intent"])

            for sentence in sentences:
                writer.writerow([sentence.encoded(), intent])
