from dictionary.objects import cadt_building, robot, some_floor, toilet
from dictionary.questions import where
from utils.generator import materialize


def sentences():
    return materialize(
        (toilet, "នៅ", where, "?"),
        ("នៅ", some_floor, toilet, "នៅ", where, "?"),
        (robot, "តើ", "នៅ", cadt_building, toilet, "នៅ", where, "?"),
    )
