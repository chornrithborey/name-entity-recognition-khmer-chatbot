from core.entity import EntityType, Entity

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
geopolitical = EntityType("Country, City", "GPE")
location = EntityType("Location", "LOC")
organization = EntityType("Organization", "ORG")

idt_building = Entity.from_list(
    [
        "អគារសិក្សា",
        "អគារIDT",
    ],
    building,
)
