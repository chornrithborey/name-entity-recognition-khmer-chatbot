import os


def count_into(dictionary: dict, subject: str) -> dict:
    if not subject in dictionary:
        dictionary[subject] = 0

    dictionary[subject] += 1

    return dictionary


def generate_markdown_table(rows: list[list[str]], headers: list[str]) -> str:
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---" for _ in headers]) + " |\n"
    for row in rows:
        for cell in row:
            table += f"| {cell} "
        table += "|\n"
    return table


def dict_to_markdown_table(dictionary: dict, title: str) -> str:
    rows = [
        [key, value]
        for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    ]
    return generate_markdown_table(rows, [title, "Count"])


def tag_segments(segments: list[str]) -> list[dict]:
    out = []
    for segment in segments:
        sub_segment = segment.split("/")
        if len(sub_segment) == 1:
            out.append({"text": sub_segment[0], "entity": None})
        else:
            out.append({"text": sub_segment[0], "entity": sub_segment[1]})
    return out


def collect_entities(segments: list[dict]) -> list[dict]:
    entity_segments = [segment for segment in segments if segment["entity"]]

    if len(entity_segments) == 0:
        return []

    entities = []
    iter_entities = iter(entity_segments)
    prev = next(iter_entities)
    entity_value = prev["text"]
    prev_entity_code = prev["entity"].split("-")[1]
    for entity in iter_entities:
        curr_marker, curr_entity_code = entity["entity"].split("-")

        if curr_marker == "B":
            entities.append({"value": entity_value, "type_code": prev_entity_code})
            prev_entity_code = curr_entity_code
            entity_value = entity["text"]
        else:
            entity_value += entity["text"]

    entities.append({"value": entity_value, "type_code": prev_entity_code})
    return entities


def collect_stats(directory: str) -> tuple:
    files = os.listdir(directory)

    words_count = {}
    entities_count = {}
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

                for entity in collect_entities(segments):
                    count_into(
                        entities_count, entity["value"] + ":" + entity["type_code"]
                    )
                    count_into(entity_types_count, entity["type_code"])

    return words_count, entities_count, entity_types_count, max_length


def main():
    words_count, entities_count, entity_types_count, max_length = collect_stats(
        "entity-tag"
    )

    with open("stats.md", "w") as f:
        f.write("# Entity Tagging Dataset\n\n")
        f.write(f"Max sentence length: {max_length}")

        f.write("\n\n## Words\n\n")
        f.write(dict_to_markdown_table(words_count, "Word"))

        f.write("\n\n## Entities\n\n")
        f.write(dict_to_markdown_table(entity_types_count, "Entity Type"))
        f.write("\n")
        f.write(
            generate_markdown_table(
                [
                    [key.split(":")[1], key.split(":")[0], value]
                    for key, value in sorted(
                        entities_count.items(),
                        key=lambda x: x[0].split(":")[1] + str(x[1]),
                        reverse=True,
                    )
                ],
                ["Entity Type", "Entity", "Count"],
            )
        )


if __name__ == "__main__":
    main()
