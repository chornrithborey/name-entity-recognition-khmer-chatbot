from utils.generator import materialize
from dictionary.objects import robot

goodbye = [
    "លាហើយ",
    "ខ្ញុំលាសិនហើយ",
    "ជម្រាបលា",
    "ជួបគ្នាថ្ងៃស្អែក",
    "ជួបគ្នាថ្ងៃក្រោយ",
    "សុខសប្បាយ",
    "បាយបាយ",
    "ទៅមុនហើយណា",
]


def sentences():
    return materialize(
        (goodbye,),
        (goodbye, robot),
    )
