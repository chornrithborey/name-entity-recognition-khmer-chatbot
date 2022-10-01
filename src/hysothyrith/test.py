print("hello")

# class EntityType:
#     name: str
#     code: str

#     def __init__(self, name: str, code: str) -> None:
#         self.name = name
#         self.code = code


# class Entity:
#     type: EntityType
#     segments: list[str]

#     def __init__(self, type: EntityType, segments: list[str]) -> None:
#         if len(segments) == 0:
#             raise Exception("Entity must have at least one segment")

#         self.type = type
#         self.segments = segments

#     def tagged(self) -> str:
#         firstSegment = self.segments[0]
#         otherSegments = self.segments[1:]

#         # fmt: off
#         return (
#             firstSegment + "/B-" + self.type.code + " "
#             + " ".join(segment + "/I-" + self.type.code for segment in otherSegments)
#         )
#         # fmt: on


# room = EntityType("Room", "ROOM")
# building = EntityType("Building", "BUILD")
# person = EntityType("Person", "PER")
# floor = EntityType("Floor", "FLOOR")
# ordinal = EntityType("Ordinal", "ORD")
# cardinal = EntityType("Cardinal", "CAR")
# date = EntityType("Date", "DATE")
# time = EntityType("Time", "TIME")
# money = EntityType("Money", "MONEY")
# event = EntityType("Event", "EVE")
# announcement = EntityType("Announcement", "ANN")
# geopolitical = EntityType("Country, City", "GPE")
# location = EntityType("Location", "LOC")
# organization = EntityType("Organization", "ORG")

# cadt_building = [
#     Entity(building, ["អាគារ", "IDT"]),
#     Entity(building, ["អាគារ", "Innovation", "Centre"]),
# ]

# for entity in cadt_building:
#     print(entity.tagged())
