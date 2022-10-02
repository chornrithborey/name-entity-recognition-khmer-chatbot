from dictionary.objects import class_subject, robot
from dictionary.questions import i_would_like_to_ask, please_tell_me
from utils.generator import materialize

study = [
    "រៀន",
    "សិក្សា",
]


def sentences():
    return materialize(
        (class_subject, study, "អំពីអ្វីទៅ?"),
        ("សូមផ្តល់ពត៌មានអំពីមុខវិជ្ជា", class_subject),
        (please_tell_me, "ពត៌មានអំពីមុខវិជ្ជា", class_subject, "មក"),
        (i_would_like_to_ask, "ពត៌មានអំពីថ្នាក់", class_subject),
        (robot, i_would_like_to_ask, "ថា", class_subject, "ជាថ្នាក់បែបម៉េចវិញ?"),
        # fmt: off
        ("ពេលដែល", study, class_subject, "នឹងហើយ", ["យើង", "ខ្ញុំ", "សិស្ស", "និស្សិត"], "អាច", ["ធ្វើអ្វីបាន", "យល់ដឹងអំពីអ្វី", "មានសមត្ថភាពបែបណា"], "ខ្លះ?"),
        # fmt: on
    )
