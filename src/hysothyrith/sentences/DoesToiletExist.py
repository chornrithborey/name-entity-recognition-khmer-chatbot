from dictionary.adjectives import exists, has
from dictionary.entities import some_floor
from dictionary.objects import robot, toilet
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
        (exists, toilet, yes_or_no, "?"),
        (exists, toilet, yes_or_no, "នៅ", some_place, "?"),
        ("សុំសួរមួយ", robot, "តើនៅ", some_place, has, toilet, yes_or_no, "?"),
    )
