import os
import shutil

directory_map = {
    "raw": "datasets",
    "segmented": "segment",
    "tagged": "pos",
    "encoded": "entity-tag",
}


def main():
    for key, value in directory_map.items():
        from_dir = os.path.join("storage/hysothyrith/sentences", key)
        to_dir = value

        for file in os.listdir(from_dir):
            shutil.copy(os.path.join(from_dir, file), to_dir)


if __name__ == "__main__":
    main()
