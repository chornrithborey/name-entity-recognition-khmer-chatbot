import os


def find_misalignments():
    encoded_dir = os.listdir("entity-tag")

    misalignments = []

    for file in encoded_dir:
        with open("entity-tag/" + file, "r") as encoded_file, open(
            "pos/" + file, "r"
        ) as tagged_file:
            encoded_file.readline()
            tagged_file.readline()
            line_number = 1

            for line in encoded_file:
                encoded_line = line.split(",")[0].strip()
                tagged_line = tagged_file.readline().split(",")[0].strip()

                encoded_segments = encoded_line.split(" ")
                tagged_segments = tagged_line.split(" ")

                if len(encoded_segments) != len(tagged_segments):
                    misalignments.append(
                        [file, line_number, encoded_segments, tagged_segments]
                    )

                line_number += 1

    with open("storage/misalignments.csv", "w") as f:
        f.write(
            "file,line_number,encoded_length,tagged_length,encoded_line,tagged_line\n"
        )

        for misalignment in sorted(misalignments, key=lambda x: x[0]):
            f.write(
                f"{misalignment[0]},{misalignment[1]},{len(misalignment[2])},{len(misalignment[3])},{' '.join(misalignment[2])},{' '.join(misalignment[3])}\n"
            )

    affected_files = list(set([misalignment[0] for misalignment in misalignments]))
    total_affected_lines = len(misalignments)

    print("Affected files:")
    for file in affected_files:
        print(f"\t{file}")
    print(f"Total affected files: {len(affected_files)}")
    print(f"Total affected lines: {total_affected_lines}")


def main():
    find_misalignments()

    # encoded_dir = "entity-tag"
    # tagged_dir = "pos"

    # encoded_lengths = {}
    # encoded_files = os.listdir(encoded_dir)

    # tagged_lengths = {}
    # tagged_files = os.listdir(tagged_dir)

    # unique_encoded_files = list(set(encoded_files))
    # unique_tagged_files = list(set(tagged_files))

    # if len(unique_encoded_files) != len(unique_tagged_files):
    #     print("Number of encoded and tagged files do not match")
    #     return

    # for file in encoded_files:
    #     with open(f"{encoded_dir}/{file}", "r") as f:
    #         encoded_lengths[file] = len(f.readlines())

    # for file in tagged_files:
    #     with open(f"{tagged_dir}/{file}", "r") as f:
    #         tagged_lengths[file] = len(f.readlines())

    # for file in encoded_lengths:
    #     print(f"{file}: {encoded_lengths[file]}, {tagged_lengths[file]}")

    # for file in encoded_lengths:
    #     if encoded_lengths[file] != tagged_lengths[file]:
    #         print(f"File {file} has different number of lines")


if __name__ == "__main__":
    main()
