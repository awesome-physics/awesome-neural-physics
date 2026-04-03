import argparse
import html
import re
from pathlib import Path

import util


SECTION_ORDER = ["fluid", "cloth", "softbody", "rigidbody", "multiphys", "survey"]
PRIMARY_GROUPS = SECTION_ORDER[:-1]
GROUP_TITLES = {
    "fluid": "Fluid",
    "cloth": "Cloth",
    "softbody": "Softbody",
    "rigidbody": "Rigidbody",
    "multiphys": "Multiphys",
    "survey": "Survey",
}
TAG_METADATA = {
    "differentiable_simulation": {
        "display": "Differentiable Simulation",
        "description": "Pipelines whose forward pass is an explicit physical simulator, with differentiable gradients propagated through that simulator.",
    },
    "neural_simulation": {
        "display": "Neural Simulation",
        "description": "Learned forward simulators where part or all of the dynamics model is neural.",
    },
    "neural_representation": {
        "display": "Neural Representation",
        "description": "Physics-aware neural state, field, or latent representations used to model dynamics.",
    },
    "neural_material": {
        "display": "Neural Material",
        "description": "Neural representations or neural constitutive models that explicitly encode material behavior.",
    },
    "reconstruction": {
        "display": "Reconstruction",
        "description": "Recovering geometry, motion, or physical state from images, videos, or sparse observations.",
    },
    "interaction": {
        "display": "Interaction",
        "description": "Interactive systems, authoring tools, editing workflows, or user-in-the-loop interfaces.",
    },
    "control": {
        "display": "Control",
        "description": "Control, optimal control, MPC, or policy design for simulated physical systems.",
    },
    "reinforce_learning": {
        "display": "Reinforcement Learning",
        "description": "Works that explicitly use reinforcement learning.",
    },
    "embodied_ai": {
        "display": "Embodied AI",
        "description": "Validation on robotic or embodied manipulation settings.",
    },
    "real2sim": {
        "display": "Real2Sim",
        "description": "Inferring simulation-ready models or parameters from real observations.",
    },
    "sim2real": {
        "display": "Sim2Real",
        "description": "Transfer from simulation-trained models or policies to the real world.",
    },
    "nerf": {
        "display": "NeRF",
        "description": "Neural radiance fields or related volumetric neural rendering methods.",
    },
    "3dgs": {
        "display": "3DGS",
        "description": "3D Gaussian splatting based modeling, rendering, or simulation pipelines.",
    },
    "engine": {
        "display": "Engine",
        "description": "Reusable simulation engines or general-purpose physics frameworks.",
    },
    "super_resolution": {
        "display": "Super-Resolution",
        "description": "Increasing spatial or temporal detail beyond the native simulation resolution.",
    },
    "style_transfer": {
        "display": "Style Transfer",
        "description": "Transferring appearance or motion style across simulations.",
    },
    "fracture": {
        "display": "Fracture",
        "description": "Fracture, crack propagation, or failure phenomena in physical systems.",
    },
    "avatar": {
        "display": "Avatar",
        "description": "Human or character-centric avatars, garments, or hair driven by body motion.",
    },
}
README_RECENT_LIMIT = 5
PUBLIC_SITE_URL = "https://awesome-physics.github.io/awesome-neural-physics/"


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
    return {
        "ENTRYTYPE": entry_type,
        "title": extract_bib_value(entry_text, "title"),
        "author": extract_bib_value(entry_text, "author"),
        "year": extract_bib_value(entry_text, "year"),
        "link": extract_bib_value(entry_text, "link"),
        "label": extract_bib_value(entry_text, "label"),
        "journal": extract_bib_value(entry_text, "journal"),
        "booktitle": extract_bib_value(entry_text, "booktitle"),
        "archiveprefix": extract_bib_value(entry_text, "archivePrefix"),
        "url": extract_bib_value(entry_text, "url"),
        "project": extract_bib_value(entry_text, "project"),
        "abstract": extract_bib_value(entry_text, "abstract"),
        "doi": extract_bib_value(entry_text, "doi"),
    }


def load_bibtex(file_path):
    text = Path(file_path).read_text(encoding="utf-8")
    return [parse_entry(entry_text) for entry_text in iter_bib_entries(text)]


def clean_bib_text(value):
    value = value or ""
    replacements = {
        "\\&": "&",
        "\\%": "%",
        "\\_": "_",
        "\\texttrademark": "TM",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = html.unescape(value)
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def clean_abstract_text(value):
    value = clean_bib_text(value)
    return re.sub(r"^abstract\s+", "", value, flags=re.I).strip()


def split_labels(value):
    return [label.strip() for label in value.split(",") if label.strip()]


def split_authors(value):
    authors = [clean_bib_text(author) for author in re.split(r"\s+and\s+", value) if author.strip()]
    return [author for author in authors if author]


def author_snippet(authors, limit=4):
    if not authors:
        return ""
    if len(authors) <= limit:
        return ", ".join(authors)
    return ", ".join(authors[:limit]) + ", et al."


def parse_year_sort(value):
    matches = re.findall(r"\b\d{4}\b", value or "")
    if not matches:
        return 0
    return max(int(match) for match in matches)


def default_paper_url(entry):
    for field_name in ("link", "url"):
        value = entry.get(field_name, "").strip()
        if value:
            return value
    doi = entry.get("doi", "").strip()
    if not doi:
        return ""
    if doi.startswith("http://") or doi.startswith("https://"):
        return doi
    return f"https://doi.org/{doi}"


def normalize_project_url(project_url, paper_url):
    project_url = (project_url or "").strip()
    if not project_url or project_url == paper_url:
        return ""
    return project_url


def primary_group(labels):
    for label in PRIMARY_GROUPS:
        if label in labels:
            return label
    if "survey" in labels:
        return "survey"
    return ""


def sort_key(entry):
    return (-entry["year_sort"], entry["title"].casefold())


def build_catalog(bib_entries):
    catalog = []
    for bib_entry in bib_entries:
        labels = split_labels(bib_entry.get("label", ""))
        title = clean_bib_text(bib_entry.get("title", "")) or "Untitled"
        paper_url = default_paper_url(bib_entry)
        project_url = normalize_project_url(bib_entry.get("project", ""), paper_url)
        authors = split_authors(bib_entry.get("author", ""))
        entry = {
            "title": title,
            "paper_url": paper_url,
            "project_url": project_url,
            "doi": clean_bib_text(bib_entry.get("doi", "")),
            "authors": authors,
            "author_text": author_snippet(authors),
            "year_text": clean_bib_text(bib_entry.get("year", "")),
            "year_sort": parse_year_sort(bib_entry.get("year", "")),
            "venue": clean_bib_text(util.get_venue_display(bib_entry)),
            "labels": labels,
            "primary_group": primary_group(labels),
            "abstract": clean_abstract_text(bib_entry.get("abstract", "")),
        }
        catalog.append(entry)
    return sorted(catalog, key=sort_key)


def group_entries(catalog, group):
    entries = [entry for entry in catalog if group in entry["labels"]]
    return sorted(entries, key=sort_key)


def section_counts(catalog):
    return {group: len(group_entries(catalog, group)) for group in SECTION_ORDER}


def get_recent_entries(catalog, limit):
    unique_titles = set()
    recent = []
    for entry in sorted(catalog, key=sort_key):
        if entry["title"] in unique_titles:
            continue
        unique_titles.add(entry["title"])
        recent.append(entry)
        if len(recent) >= limit:
            break
    return recent


def collect_tag_counts(catalog):
    counts = {}
    for entry in catalog:
        for label in entry["labels"]:
            if label in PRIMARY_GROUPS:
                continue
            counts[label] = counts.get(label, 0) + 1
    return counts


def get_tag_display(tag):
    return TAG_METADATA.get(tag, {}).get("display", tag)


def get_tag_description(tag):
    return TAG_METADATA.get(tag, {}).get("description", "")


def format_inline_tags(tags):
    if not tags:
        return ""
    return " ".join(f"`{get_tag_display(tag)}`" for tag in tags)


def format_info_line(entry):
    parts = [part for part in (entry["venue"], entry["year_text"]) if part]
    return " ".join(parts)


def render_title_link(title, url):
    if not url:
        return title
    return f"[{title}]({url})"


def render_readme_intro(catalog):
    return (
        "# Awesome Neural Physics\n\n"
        "A curated list of papers on  the seamless fusion of neural models and physics simulation. "
        "It follows the field from injecting neural capabilities into classical solvers to embedding physical simulators directly within neural architectures.\n\n"
        f"> **Best browsing experience:** use the [interactive index]({PUBLIC_SITE_URL}) for search, filtering, tag lookup, and faster navigation.\n\n"
    )


def render_recent_additions(catalog):
    lines = ["## Recent Additions", ""]
    for entry in get_recent_entries(catalog, README_RECENT_LIMIT):
        info = format_info_line(entry)
        extra_tags = [label for label in entry["labels"] if label not in {entry["primary_group"], "survey"}]
        tag_text = format_inline_tags(extra_tags[:2])
        parts = [f"- {render_title_link(entry['title'], entry['paper_url'])}"]
        if info:
            parts.append(f"`{info}`")
        if tag_text:
            parts.append(tag_text)
        lines.append(" ".join(parts))
    lines.extend(["", ""])
    return "\n".join(lines)


def render_tag_guide(catalog):
    tag_counts = collect_tag_counts(catalog)
    ordered_tags = [tag for tag in TAG_METADATA if tag in tag_counts]

    lines = [
        '<a id="tag-guide"></a>',
        "<details>",
        "<summary><strong>Tag Guide</strong></summary>",
        "",
        "Inline tags only show secondary signals beyond the section label itself.",
        "",
        "| Tag | Meaning |",
        "| --- | --- |",
    ]
    for tag in ordered_tags:
        lines.append(f"| `{get_tag_display(tag)}` | {get_tag_description(tag)} |")
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def render_category_links(catalog):
    counts = section_counts(catalog)
    links = [
        f"[{GROUP_TITLES[group]} ({counts[group]})](#{group})"
        for group in SECTION_ORDER
        if counts[group]
    ]
    return " | ".join(links)


def render_group_entry(entry, group):
    info = format_info_line(entry)
    extra_tags = [label for label in entry["labels"] if label != group]
    tag_text = format_inline_tags(extra_tags)
    link_parts = []
    if entry["project_url"]:
        link_parts.append(f"[project]({entry['project_url']})")
    doi = entry.get("doi", "").strip()
    if doi:
        doi_url = doi if doi.startswith("http://") or doi.startswith("https://") else f"https://doi.org/{doi}"
        link_parts.append(f"[doi]({doi_url})")
    elif entry["paper_url"]:
        link_parts.append(f"[paper]({entry['paper_url']})")

    parts = [f"- {entry['title']}."]
    if info:
        parts.append(f"*{info}*.")
    if tag_text:
        parts.append(tag_text)
    if link_parts:
        parts.append(" ".join(link_parts))
    return " ".join(parts)


def render_group_section(group, entries):
    open_attr = " open" if group == "fluid" else ""
    lines = [
        f'<a id="{group}"></a>',
        f"<details{open_attr}>",
        f"<summary><strong>{GROUP_TITLES[group]} ({len(entries)})</strong></summary>",
        "",
    ]
    for entry in entries:
        lines.append(render_group_entry(entry, group))
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def generate_markdown(catalog, output_file):
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(render_readme_intro(catalog))
        md_file.write('<a id="categories"></a>\n')
        md_file.write("## Categories\n\n")
        md_file.write(render_category_links(catalog))
        md_file.write("\n\n")

        for group in SECTION_ORDER:
            entries = group_entries(catalog, group)
            if not entries:
                continue
            md_file.write(render_group_section(group, entries))

        md_file.write(render_tag_guide(catalog))
        md_file.write(util.get_markdown_footer())


def parse_args():
    parser = argparse.ArgumentParser(description="Generate README.md from main.bib.")
    parser.add_argument("--input", default="main.bib", help="Input BibTeX file.")
    parser.add_argument("--output", default="README.md", help="Markdown output path.")
    return parser.parse_args()


def main():
    args = parse_args()
    bib_entries = load_bibtex(args.input)
    catalog = build_catalog(bib_entries)
    generate_markdown(catalog, args.output)
    print(f"README generated at {args.output}")


if __name__ == "__main__":
    main()
