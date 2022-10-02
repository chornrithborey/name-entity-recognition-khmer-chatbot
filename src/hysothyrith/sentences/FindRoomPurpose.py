from dictionary.entities import some_cadt_room
from dictionary.objects import robot
from dictionary.questions import please_tell_me
from utils.generator import materialize


def sentences():
    return materialize(
        (some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
        (some_cadt_room, "ជាបន្ទប់គេប្រើក្នុងគោលបំណងអ្វី?"),
        (please_tell_me, "មក", some_cadt_room, "គេប្រើធ្វើអ្វី?"),
        ("តើ", robot, "ឯងដឹងទេថា", some_cadt_room, "គេសម្រាប់ធ្វើអ្វី?"),
    )
