import sys
from rich.table import Table
from rich import print
from rich.console import Console


def lzw_encode(input_text):
    table = Table(show_header=True, header_style="bold", box=None, padding=(0, 2))
    table.add_column("LAST WORD", style="dim")
    table.add_column("CURRENT CHAR")
    table.add_column("COMMENT", no_wrap=True)
    table.add_column("ENTRIES")
    table.add_column("OUTPUT")
    table.add_column("")

    # create basic dictionary with 255 entries (ASCII)
    dictionary = []
    for i in range(256):
        dictionary.append(chr(i))

    encoded_text_char = ""
    output_size = 0
    input_size = 0
    last = ""

    # for every character of the input string do...
    for curr in input_text:
        input_size += 1
        pattern = last + curr
        # if the combination of the last word and the current character exists inside the dictionary...
        if pattern in dictionary:
            table.add_row(last, curr, "pattern (last+curr) found")
            last = pattern
        else:
            comment = "pattern (last+curr) not found"
            dictionary.append(pattern)
            entry = str(len(dictionary) - 1) + " = " + pattern
            # print the last word
            if len(last) == 1:
                output = last
            else:
                output = "<" + str(dictionary.index(last)) + ">"
            encoded_text_char += output
            output_size += 1
            # last word is the current character
            table.add_row(last, curr, comment, entry, output)
            last = curr

    if len(last) == 1:
        output = last
    else:
        output = "<" + str(dictionary.index(last)) + ">"
    encoded_text_char += output
    output_size += 1
    table.add_row(last, "", "", "", output)

    print()
    info = Table(show_header=False, show_edge=False, box=None, padding=(0, 2))
    info.add_column()
    info.add_column()
    info.add_row("input", input_text)
    info.add_row("output", encoded_text_char)
    info.add_row("storage", str(output_size / input_size * 100) + "%")
    info.add_row("compression rate", str(input_size / output_size))

    console.print(table)
    print()
    console.print(info)


console = Console()
if len(sys.argv) <= 1:
    print("no parameter found: abort...")
    exit()
text = sys.argv[1]
lzw_encode(text)
