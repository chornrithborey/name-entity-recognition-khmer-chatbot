from utils.generator import materialize
from dictionary.objects import robot

useless = [
    "អត់ប្រយោជន៍",
    "អត់បានការម៉ែន",
    "មិនដឹងស្អីទេ",
    "អត់ចេះស្អីផងនឹង",
]

bad_answer = [
    "ឆ្លើយខុសសំណួរ",
    "មិនបានឆ្លើយសំណួរផង",
    "ឆ្លើយមិនត្រូវសំណួរផង",
    "សួរគោឆ្លើយក្របី",
    "សួរAឆ្លើយB",
]

implied = [
    "អុញ",
    "ទៅចេញចឹងទៅ",
    "ចេះតែចេញហើយ",
]


def sentences():
    return materialize(
        (robot, useless),
        (bad_answer,),
        (implied,),
    )
