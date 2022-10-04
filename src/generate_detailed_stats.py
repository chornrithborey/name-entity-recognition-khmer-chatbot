import os


def count_into(dictionary: dict, subject: str) -> dict:
    if not subject in dictionary:
        dictionary[subject] = 0

    dictionary[subject] += 1

    return dictionary


def collect_entities(segments: list[dict]):
    return [segment for segment in segments if segment["entity"]]


def collect_entity_types(entities: list[dict]) -> list[str]:
    if len(entities) == 0:
        return []
    elif len(entities) == 1:
        return [entities[0]["entity"].split("-")[1]]

    entity_types = []
    iter_entities = iter(entities)
    prev = next(iter_entities)
    prev_marker, prev_entity_code = prev["entity"].split("-")
    for entity in iter_entities:
        curr_marker, curr_entity_code = entity["entity"].split("-")
        if curr_marker == "B":
            entity_types.append(prev_entity_code)
            prev_marker, prev_entity_code = curr_marker, curr_entity_code

    entity_types.append(prev_entity_code)
    return entity_types


def tag_segments(segments: list[str]) -> list[dict]:
    out = []
    for segment in segments:
        sub_segment = segment.split("/")
        if len(sub_segment) == 1:
            out.append({"text": sub_segment[0], "entity": None})
        else:
            out.append({"text": sub_segment[0], "entity": sub_segment[1]})
    return out


def dict_to_md_table(dictionary: dict, title: str) -> str:
    table = f"| {title} | Count |\n| --- | --- |\n"
    for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
        table += f"| {key} | {value} |\n"
    return table


def collect_stats(directory: str) -> tuple:
    files = os.listdir(directory)

    words_count = {}
    entity_types_count = {}
    max_length = 0

    for file in files:
        with open(directory + "/" + file, "r") as f:
            f.readline()
            for line in f:
                line = f.readline()
                question = line.strip().split(",")[0]
                max_length = max(max_length, len(question))
                segments = tag_segments(question.replace("?", "").strip().split(" "))

                for word in segments:
                    count_into(words_count, word["text"])

                entities = collect_entities(segments)
                entity_types = collect_entity_types(entities)

                for entity_type in entity_types:
                    count_into(entity_types_count, entity_type)

    return words_count, entity_types_count, max_length


def main():
    words_count, entity_types_count, max_length = collect_stats("entity-tag")

    with open("stats.md", "w") as f:
        f.write("# Entity Tagging Dataset\n\n")
        f.write(dict_to_md_table(words_count, "Word"))
        f.write("\n")
        f.write(dict_to_md_table(entity_types_count, "Entity Type"))
        f.write("\n")
        f.write(f"Max length: {max_length}")


if __name__ == "__main__":
    main()
