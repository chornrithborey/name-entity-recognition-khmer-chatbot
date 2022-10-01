import itertools

from pipe import select
from typing import Iterable
from core.sentence import Sentence


def materialize(*formats: tuple) -> list:
    return list(
        itertools.chain(*(generate(*format) for format in formats)),
    )


def generate(*format: tuple) -> Iterable:
    return itertools.product(
        *(segment if isinstance(segment, list) else [segment] for segment in format)
    ) | select(lambda x: form_sentence(*x))


def form_sentence(*segments: tuple) -> Sentence:
    return Sentence(*segments)
