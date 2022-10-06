import hashlib
import os
import pickle


def load() -> dict:
    try:
        with open("storage/hysothyrith/fingerprints.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save():
    if not os.path.exists("storage/hysothyrith/sentences"):
        os.makedirs("storage/hysothyrith/sentences")

    with open("storage/hysothyrith/fingerprints.pickle", "wb") as file:
        pickle.dump(fingerprints, file)


fingerprints = load()


def changed(file: str) -> bool:
    with open(file, "rb") as f:
        hash = hashlib.md5(f.read()).hexdigest()
        if fingerprints.get(file) == hash:
            return False

        fingerprints[file] = hash
        return True
