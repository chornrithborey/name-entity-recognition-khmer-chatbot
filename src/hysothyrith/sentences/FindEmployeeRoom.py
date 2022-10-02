from dictionary.entities import cadt_employee, cadt_lecturer
from dictionary.objects import study_room
from dictionary.questions import where
from utils.generator import materialize


def sentences():
    return materialize(
        ("តើបន្ទប់របស់", cadt_employee, "នៅ", where, "?"),
        (study_room, cadt_lecturer, "នៅ", where, "?"),
    )
