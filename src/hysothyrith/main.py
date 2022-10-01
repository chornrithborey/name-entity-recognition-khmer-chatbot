import os
import csv
import importlib

import fingerprints


def main():
    sentence_count = {}

    for module in import_modules():
        write_module(module)
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


def write_module(module):
    if not os.path.exists("storage/sentences"):
        os.makedirs("storage/sentences")

    file_path = "storage/sentences/{}.csv".format(module["intent"])
    with open(file_path, "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(["query", "entities"])

        for sentence in module["sentences"]:
            writer.writerow([sentence, ""])


if __name__ == "__main__":
    main()
