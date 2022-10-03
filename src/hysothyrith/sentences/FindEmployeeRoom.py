from dictionary.entities import cadt_employee, cadt_lecturer, some_floor
from dictionary.objects import robot, study_room
from dictionary.questions import (
    correct_or_not,
    i_would_like_to_ask,
    please_tell_me,
    where,
)
from utils.generator import materialize

which_floor = [
    "ជាន់ណា",
    "ជាន់ទីប៉ុន្មាន",
]


def sentences():
    return materialize(
        ("តើបន្ទប់របស់", cadt_employee, "នៅ", where, "?"),
        (study_room, cadt_lecturer, "នៅ", where, "?"),
        (please_tell_me, "ទីតាំងបន្ទប់របស់", cadt_employee, "បន្ទិចមក"),
        (robot, please_tell_me, "មួយមកថាបន្ទប់របស់", cadt_employee, "នៅណា?"),
        (robot, i_would_like_to_ask, "រកទីតាំងបន្ទប់របស់", cadt_employee),
        (robot, cadt_employee, "បន្ទប់របស់គាត់នៅ", where, "?"),
        ("បន្ទប់របស់", cadt_employee, "នៅ", some_floor, correct_or_not, "?"),
        ("បន្ទប់របស់", cadt_employee, "នៅ", which_floor, "?"),
    )


def patches():
    return [
        ["ច/I-PER រិយា/I-PER", "ចរិយា/I-PER"],
    ]
