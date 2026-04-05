import argparse
import html
import re
from pathlib import Path
from urllib.parse import quote, urlparse

import util


SECTION_ORDER = ["fluid", "cloth", "softbody", "rigidbody", "multiphys", "survey"]
PRIMARY_GROUPS = SECTION_ORDER[:-1]
GROUP_TITLES = {
    "fluid": "Fluid",
    "cloth": "Cloth",
    "softbody": "Softbody",
    "rigidbody": "Rigidbody",
    "multiphys": "Multiphys",
    "survey": "Surveys",
}

SECTION_DESCRIPTIONS = {
    "fluid": "Neural physics papers on fluid simulation, reconstruction, control, and differentiable methods.",
    "cloth": "Papers on cloth, garments, and apparel-related dynamics, reconstruction, and avatar-centric modeling.",
    "softbody": "Work on deformable objects, elasticity, fracture, soft robots, and learned physical models for soft materials.",
    "rigidbody": "Methods for articulated rigid bodies, robotics, contact-rich motion, and rigid object dynamics.",
    "multiphys": "Papers that span multiple physical domains or focus on coupled systems and general simulation frameworks.",
    "survey": "Survey and review papers that help map the broader neural physics landscape.",
}

HIGH_LEVEL_CATEGORY_ORDER = [
    "differentiable_simulation",
    "neural_representation",
    "neural_solver",
    "reconstruction",
    "control",
    "optimization",
    "embodied_ai",
    "engine",
    "fracture",
    "contact",
    "sound",
    "avatar",
    "survey",
    "tutorial",
]

CATEGORY_METADATA = {
    "differentiable_simulation": {
        "display": "Differentiable Simulation",
        "description": "Pipelines whose forward pass is an explicit physical simulator, with gradients propagated through that simulator.",
    },
    "neural_representation": {
        "display": "Neural Representation",
        "description": "Physics-aware neural state, field, or latent representations used to model physical processes.",
    },
    "neural_solver": {
        "display": "Neural Solver",
        "description": "Works where the solve, update, or simulation computation is replaced or driven by a learned solver.",
    },
    "reconstruction": {
        "display": "Reconstruction",
        "description": "Recovering geometry, motion, state, or parameters from observations.",
    },
    "control": {
        "display": "Control",
        "description": "Control-centered methods such as policy design, MPC, or action optimization for physical systems.",
    },
    "optimization": {
        "display": "Optimization",
        "description": "Target-driven optimization of shape, topology, parameters, trajectories, or initial states.",
    },
    "embodied_ai": {
        "display": "Embodied AI",
        "description": "Validation in robotic or embodied settings such as manipulation, locomotion, or embodied interaction.",
    },
    "engine": {
        "display": "Engine",
        "description": "Clearly reusable engines, frameworks, or toolkits rather than one-off task-specific methods.",
    },
    "fracture": {
        "display": "Fracture",
        "description": "Fracture, crack propagation, or material failure is a central simulation phenomenon.",
    },
    "contact": {
        "display": "Contact",
        "description": "Contact interaction is one of the main technical axes of the paper.",
    },
    "sound": {
        "display": "Sound",
        "description": "Acoustics or sound is a primary simulation phenomenon.",
    },
    "avatar": {
        "display": "Avatar",
        "description": "Human-avatar-centric settings such as clothed humans or body-driven garment dynamics.",
    },
    "survey": {
        "display": "Survey",
        "description": "Survey or review papers.",
    },
    "tutorial": {
        "display": "Tutorial",
        "description": "Tutorial, course, or lecture-note style entries.",
    },
}

TAG_DISPLAY_OVERRIDES = {
    "3dgs": "3DGS",
    "cnn": "CNN",
    "gan": "GAN",
    "gnn": "GNN",
    "nerf": "NeRF",
    "real2sim": "Real2Sim",
    "reinforce_learning": "Reinforcement Learning",
}

LEGACY_LABEL_TO_CATEGORY = {
    "diffsim": "differentiable_simulation",
    "differentiable_simulation": "differentiable_simulation",
    "neural_representation": "neural_representation",
    "neural_simulation": "neural_solver",
    "reconstruction": "reconstruction",
    "control": "control",
    "optimization": "optimization",
    "embodied_ai": "embodied_ai",
    "engine": "engine",
    "fracture": "fracture",
    "contact": "contact",
    "sound": "sound",
    "avatar": "avatar",
    "survey": "survey",
    "tutorial": "tutorial",
}

LEGACY_LABEL_TO_TAG = {
    "RL": "reinforce_learning",
    "interaction": "user_interaction",
    "real2sim": "real2sim",
    "reinforce_learning": "reinforce_learning",
    "neural_material": "neural_material",
    "neural_operator": "neural_operator",
    "world_models": "world_models",
    "nerf": "nerf",
    "NeRF": "nerf",
    "3dgs": "3dgs",
    "3DGS": "3dgs",
    "style_transfer": "style_transfer",
    "super_resolution": "super_resolution",
    "superresolution": "super_resolution",
    "hair": "hair",
    "mpm": "mpm",
    "benchmark_dataset": "benchmark_dataset",
}

LEGACY_LABELS_TO_DROP = {"sim2real"}

README_RECENT_LIMIT = 5
PUBLIC_SITE_URL = "https://awesome-physics.github.io/awesome-neural-physics/"
PAPER_HOSTS = {
    "arxiv.org",
    "computer.org",
    "dl.acm.org",
    "doi.org",
    "dx.doi.org",
    "ieeexplore.ieee.org",
    "link.springer.com",
    "ojs.aaai.org",
    "openaccess.thecvf.com",
    "openreview.net",
    "papers.nips.cc",
    "proceedings.mlr.press",
    "pubmed.ncbi.nlm.nih.gov",
    "sciencedirect.com",
    "www.computer.org",
    "www.sciencedirect.com",
}
CODE_HOSTS = {
    "bitbucket.org",
    "github.com",
    "gitlab.com",
}


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
        "category": extract_bib_value(entry_text, "category"),
        "tag": extract_bib_value(entry_text, "tag"),
        "keywords": extract_bib_value(entry_text, "keywords"),
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


def split_csv_values(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def split_labels(value):
    return split_csv_values(value)


def dedupe_preserve(items):
    seen = set()
    ordered = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


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


def canonicalize_url(url):
    return (url or "").strip().rstrip("/")


def doi_url_from_value(value):
    value = (value or "").strip()
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return value.rstrip("/")
    return f"https://doi.org/{value}".rstrip("/")


def infer_link_label(url):
    parsed = urlparse((url or "").strip())
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    path_segments = [segment for segment in path.split("/") if segment]

    if host in {"doi.org", "dx.doi.org"}:
        return "DOI"
    if host in CODE_HOSTS:
        return "Code"
    if host.endswith(".github.io"):
        return "Project"
    if host in PAPER_HOSTS:
        return "Paper"
    if any(segment in path_segments for segment in {"abs", "pdf", "article", "paper", "publication"}):
        return "Paper"
    return "Project"


def collect_external_links(entry):
    links = []
    seen = set()

    def add_link(label, url):
        normalized = canonicalize_url(url)
        if not normalized or normalized in seen:
            return
        seen.add(normalized)
        links.append((label, url))

    paper_url = entry.get("paper_url", "").strip()
    if paper_url:
        add_link(infer_link_label(paper_url), paper_url)

    project_url = entry.get("project_url", "").strip()
    if project_url:
        project_label = infer_link_label(project_url)
        add_link("Code" if project_label == "Code" else "Project", project_url)

    doi_url = doi_url_from_value(entry.get("doi", ""))
    if doi_url:
        add_link("DOI", doi_url)

    return links


def legacy_labels_to_metadata(labels):
    categories = []
    tags = []
    for label in labels:
        if label in LEGACY_LABELS_TO_DROP:
            continue
        if label in PRIMARY_GROUPS:
            categories.append(label)
            continue
        mapped_category = LEGACY_LABEL_TO_CATEGORY.get(label)
        if mapped_category:
            categories.append(mapped_category)
            continue
        mapped_tag = LEGACY_LABEL_TO_TAG.get(label)
        if mapped_tag:
            tags.append(mapped_tag)
            continue
        categories.append(label)
    return dedupe_preserve(categories), dedupe_preserve(tags)


def extract_metadata(bib_entry):
    explicit_categories = dedupe_preserve(split_csv_values(bib_entry.get("category", "")))
    explicit_tags = dedupe_preserve(split_csv_values(bib_entry.get("tag", "")))
    if explicit_categories or explicit_tags:
        return explicit_categories, explicit_tags
    return legacy_labels_to_metadata(split_labels(bib_entry.get("label", "")))


def primary_group(categories):
    for category in PRIMARY_GROUPS:
        if category in categories:
            return category
    if "survey" in categories:
        return "survey"
    return ""


def secondary_categories(categories, group):
    return [
        category
        for category in categories
        if category != group and category not in PRIMARY_GROUPS
    ]


def sort_key(entry):
    return (-entry["year_sort"], entry["title"].casefold())


def humanize_identifier(value):
    value = value.strip()
    if not value:
        return ""
    override = TAG_DISPLAY_OVERRIDES.get(value)
    if override:
        return override
    return " ".join(word.upper() if len(word) <= 3 else word.capitalize() for word in value.split("_"))


def get_category_display(category):
    return CATEGORY_METADATA.get(category, {}).get("display", humanize_identifier(category))


def get_category_description(category):
    return CATEGORY_METADATA.get(category, {}).get("description", "")


def get_tag_display(tag):
    return humanize_identifier(tag)


def stable_badge_color(value, kind):
    palettes = {
        "category": ["1f77b4", "2f6db3", "3a86b8", "4c78a8", "2a9d8f", "457b9d"],
        "tag": ["ff7f0e", "e76f51", "f4a261", "bc6c25", "8ab17d", "6d597a"],
    }
    colors = palettes[kind]
    checksum = sum(ord(char) for char in value)
    return colors[checksum % len(colors)]


def render_badge(label, value, kind):
    return (
        f"![{label}]("
        f"https://img.shields.io/badge/-{quote(label)}-{stable_badge_color(value, kind)}.svg?style=flat-square)"
    )


def build_catalog(bib_entries):
    catalog = []
    for bib_entry in bib_entries:
        categories, tags = extract_metadata(bib_entry)
        group = primary_group(categories)
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
            "categories": categories,
            "secondary_categories": secondary_categories(categories, group),
            "tags": tags,
            "primary_group": group,
            "abstract": clean_abstract_text(bib_entry.get("abstract", "")),
        }
        catalog.append(entry)
    return sorted(catalog, key=sort_key)


def group_entries(catalog, group):
    entries = [entry for entry in catalog if entry["primary_group"] == group]
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


def collect_secondary_category_counts(catalog):
    counts = {}
    for entry in catalog:
        for category in entry["secondary_categories"]:
            counts[category] = counts.get(category, 0) + 1
    return counts


def collect_tag_counts(catalog):
    counts = {}
    for entry in catalog:
        for tag in entry["tags"]:
            counts[tag] = counts.get(tag, 0) + 1
    return counts


def format_inline_categories(categories):
    if not categories:
        return ""
    return " ".join(f"`{get_category_display(category)}`" for category in categories)


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
        "A curated list of papers on the seamless fusion of neural models and physics simulation. "
        "It follows the field from injecting neural capabilities into classical solvers to embedding physical simulators directly within neural architectures.\n\n"
        f"> Best browsing experience: use the [interactive index]({PUBLIC_SITE_URL}) for search, filtering, and tag-based lookup.\n\n"
        f"[Interactive Index]({PUBLIC_SITE_URL}) | [BibTeX](main.bib) | [Tag Guide](#tag-guide) | [Citation](#citation)\n\n"
    )

def render_contents(catalog):
    counts = section_counts(catalog)
    lines = ["## Contents", ""]
    lines.extend(
        f"- [{GROUP_TITLES[group]} ({counts[group]})](#{group})"
        for group in SECTION_ORDER
        if counts[group]
    )
    lines.extend(
        [
            "- [Tag Guide](#tag-guide)",
            "- [Citation](#citation)",
            "",
        ]
    )
    return "\n".join(lines)


def render_keyword_guide(catalog):
    tag_counts = collect_tag_counts(catalog)
    if not tag_counts:
        return ""
    ordered_tags = sorted(
        tag_counts.items(),
        key=lambda item: (-item[1], get_tag_display(item[0]).casefold()),
    )
    lines = ["<a id=\"tag-guide\"></a>", "## Tag Guide", ""]
    lines.append("Reader-facing tags used in the list for quick scanning and search.")
    lines.extend(["", "| Tag | Count |", "| --- | --- |"])
    for tag, count in ordered_tags:
        lines.append(f"| {get_tag_display(tag)} | {count} |")
    lines.append("")
    return "\n".join(lines)


def render_group_entry(entry):
    info = format_info_line(entry)
    link_parts = [f"[[{label}]]({url})" for label, url in collect_external_links(entry)]

    first_line_parts = [f"**{entry['title']}**"]
    if info:
        first_line_parts.append(info)
    lines = ["* " + " | ".join(first_line_parts) + "  "]

    author_text = entry.get("author_text", "").strip()
    if author_text:
        lines.append(f"  *{author_text}*  ")

    if link_parts:
        lines.append("  " + " ".join(link_parts) + "  ")

    meta_parts = [
        render_badge(get_category_display(category), category, "category")
        for category in entry["secondary_categories"]
    ]
    meta_parts.extend(
        render_badge(get_tag_display(tag), tag, "tag")
        for tag in entry["tags"]
    )
    if meta_parts:
        lines.append("  " + " ".join(meta_parts))
    return "\n".join(lines)


def render_group_section(group, entries):
    lines = [f'<a id="{group}"></a>', f"## {GROUP_TITLES[group]} ({len(entries)})", ""]
    description = SECTION_DESCRIPTIONS.get(group, "")
    if description:
        lines.extend([description, ""])
    for index, entry in enumerate(entries):
        if index:
            lines.extend(["<br>", ""])
        lines.append(render_group_entry(entry))
        lines.append("")
    return "\n".join(lines)


def generate_markdown(catalog, output_file):
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(render_readme_intro(catalog))
        md_file.write(render_contents(catalog))
        md_file.write("\n")

        for group in SECTION_ORDER:
            entries = group_entries(catalog, group)
            if not entries:
                continue
            md_file.write(render_group_section(group, entries))

        keyword_guide = render_keyword_guide(catalog)
        if keyword_guide:
            md_file.write(keyword_guide)
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
