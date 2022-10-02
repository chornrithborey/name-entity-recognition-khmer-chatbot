import re
from typing import Union

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
            segmented_entity = entity.segmented()
            encoded_entity = entity.encoded()

            if not segmented_entity in out:
                extracted = self.extract_entity(entity)
                if extracted:
                    segmented_entity = extracted
                    encoded_entity = entity.type.encode(extracted.split(" "))
                else:
                    raise ValueError(
                        "Entity '{}' not found in sentence '{}'".format(
                            segmented_entity, out
                        )
                    )

            out = out.replace(segmented_entity, encoded_entity)

        return out

    def extract_entity(self, entity: Entity) -> Union[str, None]:
        pattern = "\s*".join([char for char in entity.value.replace(" ", "")])
        search = re.search(pattern, self.segmented())
        return search.group(0) if search else None
