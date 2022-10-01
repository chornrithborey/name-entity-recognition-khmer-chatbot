from dictionary.adjectives import exists, has
from dictionary.objects import robot, some_floor, toilet
from dictionary.questions import yes_or_no
from utils.generator import materialize

some_place = [
    "នឹង",
    "កន្លែងនេះ",
    "សាលានឹង",
    "អាគារនេះ",
] + some_floor


def sentences():
    return materialize(
        # Simple
        (exists, toilet, yes_or_no, "?"),
        # With place
        (exists, toilet, yes_or_no, "នៅ", some_place, "?"),
        # With robot and place
        ("សុំសួរមួយ", robot, "តើនៅ", some_place, has, toilet, yes_or_no, "?"),
    )
