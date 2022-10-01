import hashlib
import os
import pickle


def load() -> dict:
    try:
        with open("storage/fingerprints.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save():
    if not os.path.exists("storage/sentences"):
        os.makedirs("storage/sentences")

    with open("storage/fingerprints.pickle", "wb") as file:
        pickle.dump(fingerprints, file)


fingerprints = load()


def changed(file: str) -> bool:
    with open(file, "rb") as f:
        hash = hashlib.md5(f.read()).hexdigest()
        if fingerprints.get(file) == hash:
            return False

        fingerprints[file] = hash
        return True
