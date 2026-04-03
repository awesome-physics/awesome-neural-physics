import re
from pathlib import Path

import util


def iter_bib_entries(text):
    index = 0
    while True:
        start = text.find("@", index)
        if start == -1:
            return
        brace_start = text.find("{", start)
        if brace_start == -1:
            return
        depth = 0
        end = brace_start
        while end < len(text):
            char = text[end]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    yield text[start : end + 1]
                    index = end + 1
                    break
            end += 1
        else:
            return


def extract_bib_value(entry_text, field_name):
    pattern = re.compile(rf"(^|\n)\s*{re.escape(field_name)}\s*=\s*", re.I)
    match = pattern.search(entry_text)
    if not match:
        return ""

    index = match.end()
    while index < len(entry_text) and entry_text[index].isspace():
        index += 1
    if index >= len(entry_text):
        return ""

    quote = entry_text[index]
    if quote == "{":
        depth = 0
        start = index + 1
        index += 1
        while index < len(entry_text):
            char = entry_text[index]
            if char == "{":
                depth += 1
            elif char == "}":
                if depth == 0:
                    return entry_text[start:index].strip()
                depth -= 1
            index += 1
        return ""

    if quote == '"':
        start = index + 1
        index += 1
        while index < len(entry_text):
            if entry_text[index] == '"' and entry_text[index - 1] != "\\":
                return entry_text[start:index].strip()
            index += 1
        return ""

    end = index
    while end < len(entry_text) and entry_text[end] not in ",\n":
        end += 1
    return entry_text[index:end].strip()


def parse_entry(entry_text):
    entry_type_match = re.match(r"@(\w+)\{", entry_text)
    entry_type = entry_type_match.group(1) if entry_type_match else ""
    entry = {
        "ENTRYTYPE": entry_type,
        "title": extract_bib_value(entry_text, "title"),
        "author": extract_bib_value(entry_text, "author"),
        "year": extract_bib_value(entry_text, "year"),
        "link": extract_bib_value(entry_text, "link"),
        "label": extract_bib_value(entry_text, "label"),
        "journal": extract_bib_value(entry_text, "journal"),
        "booktitle": extract_bib_value(entry_text, "booktitle"),
        "archiveprefix": extract_bib_value(entry_text, "archivePrefix"),
    }
    return entry


def load_bibtex(file_path):
    text = Path(file_path).read_text(encoding="utf-8")
    return [parse_entry(entry_text) for entry_text in iter_bib_entries(text)]


def format_entry(entry):
    dict_entry = {}
    dict_entry["title"] = entry.get("title", "No title")
    dict_entry["author"] = entry.get("author", "No author")
    dict_entry["year"] = entry.get("year", "No year")
    dict_entry["link"] = entry.get("link", "")
    dict_entry["venue"] = util.get_venue_display(entry)
    label = entry.get("label", "")
    split_labels = [l.strip() for l in label.split(",") if l.strip()]
    dict_entry["label"] = split_labels
    return dict_entry


def generate_markdown(bib_entries, output_file):
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(util.get_markdown_header())

        group_entry_dict = {}
        label_color_dict = {}

        group_entry_dict["fluid"] = []
        group_entry_dict["cloth"] = []
        group_entry_dict["softbody"] = []
        group_entry_dict["rigidbody"] = []
        group_entry_dict["multiphys"] = []
        group_entry_dict["survey"] = []

        for bib_entry in bib_entries:
            entry = format_entry(bib_entry)
            for label in entry["label"]:
                if label in group_entry_dict.keys():
                    group_entry_dict[label].append(entry)

        for group_label, group_entries in group_entry_dict.items():
            group_entry_dict[group_label] = [v for v in sorted(group_entries, key=lambda entry: entry["year"])]

        for group_label, group_entries in group_entry_dict.items():
            md_file.write("## " + group_label.title() + "\n\n")
            md_file.write("|Name|Info|Link|Label|\n")
            md_file.write("|---|---|---|---|\n")
            for entry in group_entries:
                labels = entry["label"]
                label_str = ""
                for label in labels:
                    label_str += "![][~" + label + "]"
                    if label not in label_color_dict.keys():
                        label_color_dict[label] = util.get_label_badge_link(label)

                info_parts = [part for part in [entry["venue"], entry["year"]] if part]
                info_text = " ".join(info_parts)
                md_file.write(f"|**{entry['title']}**| {info_text}| [Link]({entry['link']}) | {label_str}\n")
            md_file.write("\n\n")
        md_file.write("\n\n")

        md_file.write(util.get_markdown_footer())

        for label, color_code in label_color_dict.items():
            md_file.write(f"[~{label}]:{color_code}\n")


def main():
    input_bibtex = "main.bib"
    output_markdown = "README.md"

    bib_entries = load_bibtex(input_bibtex)
    generate_markdown(bib_entries, output_markdown)
    print(f"Awesome list generated and saved to {output_markdown}")


if __name__ == "__main__":
    main()
