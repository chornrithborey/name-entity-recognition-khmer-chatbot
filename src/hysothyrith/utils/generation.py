import itertools
from typing import Iterable

from pipe import select


def materialize(*formats: tuple) -> list:
    return list(itertools.chain(*(generate(*format) for format in formats)))


def generate(*format: tuple) -> Iterable:
    return itertools.product(
        *([segment] if isinstance(segment, str) else segment for segment in format)
    ) | select(form_sentence)


def form_sentence(segments: list) -> str:
    # for i, segment in enumerate(segments):
    #     if isinstance(segment, Entity):
    #         segments[i] = segment[0]

    return ["".join(segments)]
