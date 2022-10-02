from dictionary.objects import robot
from utils.generator import materialize

useless = [
    "អត់ប្រយោជន៍",
    "អត់បានការម៉ែន",
    "មិនដឹងស្អីទេ",
    "អត់ចេះស្អីផងនឹង",
    "មិនបានការអ្វីសោះ",
]

bad_answer = [
    "ឆ្លើយខុសសំណួរ",
    "ឆ្លើយខុសទំនង",
    "មិនបានឆ្លើយសំណួរផង",
    "ឆ្លើយមិនត្រូវសំណួរផង",
    "សួរគោឆ្លើយក្របី",
    "សួរAឆ្លើយB",
]

implied = [
    "អុញ",
    "ទៅចេញចឹងទៅ",
    "ចេះតែចេញហើយ",
    "ទៅសួរមនុស្សវិញ",
    "សួរមនុស្សវិញគ្រាន់ជាង",
    "ស្មានតែពូកែ",
    "ស្មានតែអស្ចារ្យ",
]


def sentences():
    return materialize(
        (robot, "ឯងមិនបានជួយខ្ញុំផង"),
        (robot, useless),
        (bad_answer,),
        (robot, "ឯង", bad_answer),
        (implied,),
    )
