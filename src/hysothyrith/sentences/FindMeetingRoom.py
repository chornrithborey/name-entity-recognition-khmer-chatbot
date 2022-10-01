from dictionary.objects import meeting_room
from dictionary.questions import where
from utils.generator import materialize


topic = [
    "អាហារូបករណ៍",
    "ការងារស្ម័គ្រចិត្ត",
]

time = [
    "ព្រឹកនេះ",
    "ម៉ោង៩",
    "ម៉ោងដប់",
    "ម៉ោងបួន",
]

person = [
    "លោកគ្រូបញ្ញា",
    "នាយកសាលា",
]

organization = [
    "ក្រសួង",
    "ស្ថានទូតអាមេរិក",
    "ធនាគារអេសុីលីដា",
    "អង្គការសហគមន៍អាមេរិក",
    "ក្រុមហ៊ុនស្មាត",
]


def sentences():
    return materialize(
        # Simple
        (where, meeting_room, "?"),
        # With time
        (meeting_room, time, "នៅ", where, "?"),
        # With topic
        (meeting_room, "ពាក់ព័ន្ធនឹង", topic, "នៅ", where, "?"),
        # With person
        (where, meeting_room, "ជាមួយ", person, "?"),
        # With organization
        (where, meeting_room, "ជាមួយ", organization, "?"),
        # Complex combination
        # (where, meeting_room, "ជាមួយ", person, "ពាក់ព័ន្ធនឹង", topic, "នៅ", time, "?"),
        # # fmt: off
        # (where, meeting_room, "ជាមួយ", person, "និង", organization, "រឿង", topic, "នៅ", time, "?"),
        # # fmt: on
    )
