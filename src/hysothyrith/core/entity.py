from utils import tokenizer


class EntityType:
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        return self.name


class Entity:
    __segments: list[str] = None

    def __init__(self, type: EntityType, value: str) -> None:
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return self.value

    def segments(self) -> str:
        if not self.__segments:
            self.__segments = tokenizer.segment(self.value)

        return self.__segments

    def segmented(self) -> str:
        return " ".join(self.segments())

    def coded(self) -> str:
        return " ".join(
            f"{segment}/{'B' if i == 0 else 'I'}-{self.type.code}"
            for i, segment in enumerate(self.segments())
        )

    @staticmethod
    def from_list(type: EntityType, values: list[str]) -> list["Entity"]:
        return [Entity(type, value) for value in values]
