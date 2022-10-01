from utils import tokenizer

from core.entity import Entity


class Sentence:
    format: tuple = None
    entities: list[Entity] = None

    __segments: list[str] = None

    def __init__(self, *format: tuple) -> None:
        self.format = format
        self.entities = [segment for segment in format if isinstance(segment, Entity)]

    def __repr__(self) -> str:
        return "".join(str(segment) for segment in self.format)

    def segments(self) -> list[str]:
        if not self.__segments:
            self.__segments = tokenizer.segment(repr(self))

        return self.__segments

    def segmented(self) -> str:
        return " ".join(self.segments())

    def tagged(self) -> str:
        out = self.segmented()
        for entity in self.entities:
            out = out.replace(entity.segmented(), entity.coded())

        return out
