from dictionary.entities import some_cadt_room
from dictionary.objects import robot
from utils.generator import materialize


def sentences():
    return materialize(
        (some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
        ("តើ", robot, "ឯងដឹងទេថា", some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
    )
