class Entity:
    name: str
    code: str
    variations: list[str]

    def __init__(self, name: str, code: str, variations: list[str] = None):
        self.name = name
        self.code = code
        self.variations = variations

    def get_name(self) -> str:
        return self.name

    def get_code(self) -> str:
        return self.code

    def get_variations(self) -> list[str]:
        return self.variations

    def beginning(self) -> str:
        return "B-" + self.code

    def inside(self) -> str:
        return "I-" + self.code

    def __str__(self) -> str:
        return self.name + "-" + self.code

class EntityType:
    name: str
    code: str

    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

class Ent:
    type: EntityType
    value: str

    def __init__(self, type: EntityType, value: str) -> None:
        self.type = type
        self.value = value

# Room	ROOM
# Building	BUILD
# Person	PER
# Floor	FLOOR
# Ordinal	ORD
# Cardinal	CAR
# Date	DATE
# Time	TIME
# Money	MONEY
# Event	EVE
# Announcement	ANN
# Country, CIty	GPE
# Location	LOC
# Organization	ORG

room = EntityType("Room", "ROOM")
building = EntityType("Building", "BUILD")
person = EntityType("Person", "PER")
floor = EntityType("Floor", "FLOOR")
ordinal = EntityType("Ordinal", "ORD")
cardinal = EntityType("Cardinal", "CAR")
date = EntityType("Date", "DATE")
time = EntityType("Time", "TIME")
money = EntityType("Money", "MONEY")
event = EntityType("Event", "EVE")
announcement = EntityType("Announcement", "ANN")
gpe = EntityType("Country, City", "GPE")
location = EntityType("Location", "LOC")
organization = EntityType("Organization", "ORG")

cadt_building = [
    Ent(building, "អាគារInnovation Centre"),
]
