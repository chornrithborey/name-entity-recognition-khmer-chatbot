from core.entity import Entity
from dictionary import entity_types
from dictionary.entities import cadt_employee, some_organization, some_time
from dictionary.objects import meeting_room
from dictionary.questions import where
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


def sentences():
    return materialize(
        (where, meeting_room, "?"),
        (meeting_room, some_time, "នៅ", where, "?"),
        (meeting_room, "ពាក់ព័ន្ធនឹង", topic, "នៅ", where, "?"),
        (where, meeting_room, "ជាមួយ", person, "?"),
        (where, meeting_room, "ជាមួយ", some_organization, "?"),
        # (where, meeting_room, "ជាមួយ", person, "ពាក់ព័ន្ធនឹង", topic, "នៅ", time, "?"),
        # (where, meeting_room, "ជាមួយ", person, "និង", organization, "រឿង", topic, "នៅ", time, "?"),
    )
