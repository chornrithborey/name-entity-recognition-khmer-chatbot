from utils.generation import materialize
from dictionary.objects import some_cadt_room, robot


def sentences():
    return materialize(
        (some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
        ("តើ", robot, "ឯងដឹងទេថា", some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
    )
