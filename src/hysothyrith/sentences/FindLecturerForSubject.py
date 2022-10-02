from dictionary.objects import class_subject, robot
from dictionary.questions import i_would_like_to_ask, please_tell_me
from utils.generator import materialize

which_lecturer = [
    "គ្រូណា",
    "អ្នកគ្រូណា",
    "លោកគ្រូណា",
    "អ្នកណា",
    "សាស្រ្តាចារ្យណា",
]


def sentences():
    return materialize(
        (which_lecturer, "ជាអ្នកបង្រៀន", class_subject, "?"),
        (robot, please_tell_me, "មកអ្នកបង្រៀន", class_subject, "មានឈ្មោះអ្វី?"),
        (i_would_like_to_ask, "ថាអ្នកបង្រៀនមុខវិជ្ជា", class_subject, "គាត់ជាអ្នកណា?"),
    )
