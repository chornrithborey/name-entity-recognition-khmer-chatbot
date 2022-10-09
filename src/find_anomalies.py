import os


def main():
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


if __name__ == "__main__":
    main()
