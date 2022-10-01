import csv
import importlib
import os

import fingerprints


def main():
    sentence_count = {}

    for module in import_modules():
        if fingerprints.changed(module):
            print("Writing {}...".format(module["intent"]))
            write_module(module)
        else:
            print("Skipping {}...".format(module["intent"]))

        sentence_count[module["intent"]] = len(module["sentences"])

    # Print stats
    print("\nDone! Wrote {} sentences.".format(sum(sentence_count.values())))

    summary_lines = []
    for intent, count in sentence_count.items():
        summary_lines.append("{}: {}".format(intent, count))

    print("\n".join(sorted(summary_lines)))

    # Remove old csv files
    # for file in os.listdir("storage/sentences"):
    #     if file.endswith(".csv") and file[:-4] not in sentence_count:
    #         print("Removing {}...".format(file))
    #         os.remove("storage/sentences/{}".format(file))

    fingerprints.save()


def import_modules() -> list[dict]:
    modules = []
    for file in os.listdir("src/hysothyrith/sentences"):
        if file.endswith(".py") and not file.startswith("_"):
            module_name = file.replace(".py", "")
            module = importlib.import_module("sentences.{}".format(module_name))
            modules.append({"intent": module_name, "sentences": module.sentences()})

    return modules


def write_module(module):
    if not os.path.exists("storage/sentences"):
        os.makedirs("storage/sentences")

    file_path = "storage/sentences/{}.csv".format(module["intent"])
    with open(file_path, "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(["query", "entities"])

        for sentence in module["sentences"]:
            query = sentence[0]
            entities = ""
            # * Skip writing the entities for now
            # try:
            #     entities = "|".join(sentence[1])
            # except IndexError:
            #     pass
            writer.writerow([query, entities])


if __name__ == "__main__":
    main()
