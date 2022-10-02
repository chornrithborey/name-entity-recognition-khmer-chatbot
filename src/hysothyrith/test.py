import os
import csv
import importlib


def main():
    intent = "FindEmployeeRoom"
    module = importlib.import_module("sentences.{}".format(intent))

    if not os.path.exists("storage/sentences"):
        os.makedirs("storage/sentences")

    file_path = "storage/sentences/{}.csv".format(intent)
    with open(file_path, "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(["query", "entities"])

        for sentence in module.sentences():
            writer.writerow([sentence.tagged(), ""])

    print("\nDone!")


if __name__ == "__main__":
    main()
