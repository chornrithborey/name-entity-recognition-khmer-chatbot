import os
import shutil


def main():
    for file in os.listdir("storage/sentences"):
        shutil.copy("storage/sentences/{}".format(file), "entity-tag")


if __name__ == "__main__":
    main()
