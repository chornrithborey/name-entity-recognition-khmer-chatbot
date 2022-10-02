import os

# Read all the file names inside datasets
files = os.listdir("entity-tag")

# Create a dictionary to store the file names and their respective number of lines
file_lines = {}

# loop through the files and count the number of rows
for file in files:
    with open("entity-tag/" + file, "r") as f:
        file_lines[file] = len(f.readlines()) - 1

# generate a markdown table from the dictionary
table = "| Intent | Number of Sentences |\n| --- | --- |\n"
for file, lines in file_lines.items():
    # remove the .csv extension
    table += "| {} | {} |\n".format(file.replace(".csv", ""), lines)

# generate the summary table
summary = "|Total Number of Intents | Total Number of Sentences |\n| --- | --- |\n"
summary += "| {} | {} |\n".format(len(file_lines), sum(file_lines.values()))

# write the table to a markdown file
with open("README.md", "w") as f:
    # write the title
    f.write("# Entity Tagging Dataset\n\n")
    # write the table
    f.write(table)
    # write the summary
    f.write("\n" + summary)
