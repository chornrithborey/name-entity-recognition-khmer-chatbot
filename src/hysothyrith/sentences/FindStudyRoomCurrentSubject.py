from dictionary.entities import cadt_study_room
from dictionary.objects import lecturer, robot
from dictionary.questions import i_would_like_to_ask, please_tell_me
from dictionary.verbs import study
from utils.generator import materialize


def sentences():
    return materialize(
        ("នៅ", cadt_study_room, "គេកំពុង", study, "អ្វី?"),
        (cadt_study_room, lecturer, "កំពុងបង្រៀនអ្វី?"),
        # fmt: off
        (please_tell_me, "បន្ទិចមក នៅ", cadt_study_room, "គេកំពុង", study, "អ្វី?"),
        (robot, i_would_like_to_ask, "ថានៅ", cadt_study_room, lecturer, "កំពុងបង្រៀនអ្វីដែរ?"),
        # fmt: on
    )
