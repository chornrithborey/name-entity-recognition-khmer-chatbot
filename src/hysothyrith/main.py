import importlib
import os

import fingerprints
from utils.module import write_module


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


if __name__ == "__main__":
    main()
