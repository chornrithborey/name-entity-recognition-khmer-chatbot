from core.entity import Entity

from dictionary import entity_types

some_floor = Entity.from_list(
    entity_types.floor,
    [
        "ជាន់នេះ",
        "ជាន់លើ",
        "ជាន់ក្រោម",
        "ជាន់ទី១",
        "ជាន់ទី២",
        "ជាន់ផ្ទាល់ដី",
        "ជាន់លើគេ",
        "ជាន់លើគេបង្អស់",
    ],
)

some_organization = Entity.from_list(
    entity_types.organization,
    [
        "ក្រសួង",
        "ស្ថានទូតអាមេរិក",
        "ធនាគារអេសុីលីដា",
        "អង្គការសហគមន៍អាមេរិក",
        "ក្រុមហ៊ុនស្មាត",
    ],
)

cadt = Entity.from_list(
    entity_types.organization,
    [
        "CADT",
        "សុីអេឌីធី",
        "Cambodia Academy of Digital Technology",
        "បណ្ឌិត្យសភាបច្ចេកវិទ្យាឌីជីថលកម្ពុជា",
    ],
)

cadt_researcher = Entity.from_list(
    entity_types.person,
    [
        "លោកចាន់ សុភី",
        "លោកអាឡិច",
        "លោកAlexander",
    ],
)

cadt_lecturer = Entity.from_list(
    entity_types.person,
    [
        "លោកគ្រូបញ្ញា",
        "អ្នកគ្រូចរិយា",
    ],
)

cadt_employee = cadt_researcher + cadt_lecturer

cadt_building = Entity.from_list(
    entity_types.building,
    [
        "អគារនេះ",
        "អគារIDT",
        "អគារInnovation Center",
    ],
)

cadt_meeting_room = Entity.from_list(
    entity_types.room,
    [
        "បន្ទប់Jupyter",
        "សាលប្រជុំធំ",
    ],
)

cadt_study_room = Entity.from_list(
    entity_types.room,
    [
        "បន្ទប់១០១",
        "បន្ទប់៣០១",
    ],
)

some_cadt_room = cadt_meeting_room + cadt_study_room

some_time = Entity.from_list(
    entity_types.time,
    [
        "ព្រឹកនេះ",
        "រសៀលនេះ",
        "ម៉ោង១០",
        "ម៉ោងបួន",
    ],
)

some_date = Entity.from_list(
    entity_types.date,
    [
        "ថ្ងៃនេះ",
        "ថ្ងៃស្អែក",
        "ថ្ងៃអាទិត្យ",
        "ម្លិលមិញ",
        "ថ្ងៃទី១០",
        "ថ្ងៃទី១០ ខែមិថុនា ឆ្នាំ២០២១",
    ],
)

some_time_period = some_time + some_date
