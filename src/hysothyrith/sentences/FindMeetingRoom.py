from core.entity import Entity
from dictionary import entity_types
from dictionary.entities import cadt_employee, some_organization, some_time
from dictionary.objects import meeting_room, robot
from dictionary.questions import (
    can_you_tell_me,
    i_would_like_to_ask,
    please_tell_me,
    where,
)
from utils.generator import materialize

topic = Entity.from_list(
    entity_types.announcement,
    [
        "អាហារូបករណ៍ទៅបារាំង",
        "ការងារស្ម័គ្រចិត្ត",
    ],
)

person = cadt_employee + [
    "នាយកសាលា",
]

location = [
    "ទីតាំង",
    "កន្លែង",
]


def sentences():
    return materialize(
        (where, meeting_room, "?"),
        (please_tell_me, location, "របស់", meeting_room, "មក", robot),
        (meeting_room, some_time, "នៅ", where, "?"),
        (meeting_room, "ពាក់ព័ន្ធនឹង", topic, "នៅ", where, "?"),
        (where, meeting_room, "ជាមួយ", person, "?"),
        (where, meeting_room, "ជាមួយ", some_organization, "?"),
        (i_would_like_to_ask, "រក", meeting_room, "ជាមួយ", some_organization),
        # fmt: off
        (robot, can_you_tell_me, "ថា", meeting_room, "ទាក់ទងនឹង", topic, "នៅ", where, "?"),
        # fmt: on
        # (where, meeting_room, "ជាមួយ", person, "ពាក់ព័ន្ធនឹង", topic, "នៅ", time, "?"),
        # (where, meeting_room, "ជាមួយ", person, "និង", organization, "រឿង", topic, "នៅ", time, "?"),
    )
