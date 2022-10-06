import os
import csv
import importlib

import fingerprints


def main():
    sentence_count = {}

    for module in import_modules():
        write_module(
            module,
            "storage/hysothyrith/sentences",
            segmented=True,
            tagged=True,
            encoded=True,
        )
        sentence_count[module["intent"]] = len(module["sentences"])

    print("\nDone!")

    fingerprints.save()


def import_modules() -> list[dict]:
    modules = []
    for file in os.listdir("src/hysothyrith/sentences"):
        if file.endswith(".py") and not file.startswith("_"):
            if fingerprints.changed("src/hysothyrith/sentences/{}".format(file)):
                print("Importing {}...".format(file))
                module_name = file.replace(".py", "")
                module = importlib.import_module("sentences.{}".format(module_name))
                modules.append({"intent": module_name, "sentences": module.sentences()})
            else:
                print("Skipping {}...".format(file))

    return modules


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


if __name__ == "__main__":
    main()
