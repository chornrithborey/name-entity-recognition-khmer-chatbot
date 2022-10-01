from utils.generation import materialize
from dictionary.objects import cadt_employee, cadt_lecturer
from dictionary.questions import where

study_room = [
    "បន្ទប់សិក្សា",
    "បន្ទប់រៀន",
]


def sentences():
    return materialize(
        ("តើបន្ទប់របស់", cadt_employee, "នៅ", where, "?"),
        (study_room, cadt_lecturer, "នៅ", where, "?"),
        # Heavy implication
        ("តើបន្ទប់ម៉ោង", cadt_lecturer, "នៅទីណា?"),
    )
