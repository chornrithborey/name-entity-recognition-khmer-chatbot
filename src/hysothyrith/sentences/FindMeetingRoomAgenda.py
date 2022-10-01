from dictionary.objects import cadt_meeting_room, some_organization, some_time_period
from utils.generator import materialize

discussing = [
    "ជជែកគ្នាអំពី",
    "ប្រជុំរឿង",
]


def sentences():
    return materialize(
        ("តើនៅ", cadt_meeting_room, "គេកំពុង", discussing, "អ្វី?"),
        (some_time_period, "គេ", discussing, "អ្វីនៅ", cadt_meeting_room, "?"),
        # fmt: off
        ("តើ", some_organization, "គេកំពុង", discussing, "អ្វីនៅ", cadt_meeting_room, "?"),
        # fmt: on
    )
