import sys
script, input_encoding, error = sys.argv  # input_encoding = utf-8 ; error = strict


def main(language_file, encoding, errors):  # language_file references "languages" which references the languages.txt file ; encoding references "input_encoding" (which was provided in line23 in main fnct) and was provided when the script was called ; "errors" references "error" (see when main fnct is called at line23)
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")  # opens txt file and assigns it to this variable

main(languages, input_encoding, error)  # languages is "languages.txt" ; input_encoding is provided when calling the script ; error is provided when calling the script
