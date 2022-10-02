from dictionary.entities import cadt_building, some_floor
from dictionary.objects import robot, toilet
from dictionary.questions import where
from utils.generator import materialize


def sentences():
    return materialize(
        (toilet, "នៅ", where, "?"),
        ("នៅ", some_floor, toilet, "នៅ", where, "?"),
        (robot, "តើ", "នៅ", cadt_building, toilet, "នៅ", where, "?"),
    )
