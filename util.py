import re


def _get_venue_field(entry):
    entry_type = entry["ENTRYTYPE"].lower()
    if entry_type == "article":
        return entry.get("journal", "")
    if entry_type == "inproceedings":
        return entry.get("booktitle", "")
    if entry_type == "misc":
        return entry.get("archiveprefix", "")
    return entry.get("journal") or entry.get("booktitle") or ""


def get_jabbr(entry):
    venue = _get_venue_field(entry)
    if not venue:
        return ""
    return _jabbr_mapping(venue)


def get_venue_display(entry):
    venue = _get_venue_field(entry)
    if not venue:
        return ""
    return get_jabbr(entry) or _clean_venue_text(venue)


colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]


def get_label_badge_link(label):
    color_code = colors[ord(label[0]) % len(colors)][1:]
    return f"https://img.shields.io/badge/-{label}-{color_code}.svg"


def get_label_color(label):
    return colors[ord(label[0]) % len(colors)]


def get_markdown_header():
    return (
        "# Awesome Neural Physics\n\n"
        "[This repository](https://github.com/awesome-physics/awesome-neural-physics) hosts a curated list of papers on **AI techniques for physics simulation** in computer graphics.\n\n"
        "If you find this list useful, please consider citing it and giving it a :star:. Feel free to share it with others!\n\n"
    )


def get_markdown_footer():
    return (
        "## Citation\n\n"
        "If you find this repository helpful, please consider citing it!\n\n"
        "```\n"
        "@misc{wang2024awesomelist,\n"
        "  title = {Awesome Neural Physics - A Curated List of Papers on AI Techniques for Physics Simulation in Computer Graphics},\n"
        "  author = {Hui Wang},\n"
        "  journal = {GitHub repository},\n"
        "  url = {https://github.com/awesome-physics/awesome-neural-physics},\n"
        "  year = {2023},\n"
        "}\n"
        "```\n"
    )


_raw_jabbr_map = {
    "ACM Transactions on Graphics (TOG)".casefold(): "TOG",
    "ACM Transactions on Graphics".casefold(): "TOG",
    "ACM Trans. Graph.".casefold(): "TOG",
    "IEEE Transactions on Visualization and Computer Graphics".casefold(): "TVCG",
    "Computer Graphics Forum".casefold(): "CGF",
    "Proceedings of the ACM on Computer Graphics and Interactive Techniques".casefold(): "PACMCGIT",
    "Proc. ACM Comput. Graph. Interact. Tech.".casefold(): "PACMCGIT",
    "Computational Visual Media".casefold(): "CVM",
    "Computer Animation and Virtual Worlds".casefold(): "CAVW",
    "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)".casefold(): "CVPR",
    "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition".casefold(): "CVPR",
    "The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)".casefold(): "CVPR",
    "The IEEE/CVF Conference on Computer Vision and Pattern Recognition".casefold(): "CVPR",
    "Advances in Neural Information Processing Systems".casefold(): "NeurIPS",
    "Conference on Neural Information Processing Systems".casefold(): "NeurIPS",
    "Proceedings of the International Conference on Learning Representations".casefold(): "ICLR",
    "International Conference on Learning Representations".casefold(): "ICLR",
    "ICML".casefold(): "ICML",
    "International Conference on Machine Learning".casefold(): "ICML",
    "Proceedings of the AAAI Conference on Artificial Intelligence".casefold(): "AAAI",
    "Proceedings of the european conference on computer vision (eccv)".casefold(): "ECCV",
    "European Conference on Computer Vision".casefold(): "ECCV",
    "Proceedings of the IEEE/CVF International Conference on Computer Vision".casefold(): "ICCV",
    "Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)".casefold(): "ICRA",
    "IEEE International Conference on Robotics and Automation (ICRA)".casefold(): "ICRA",
    "International Conference on Robotics and Automation (ICRA)".casefold(): "ICRA",
    "IROS".casefold(): "IROS",
    "ICCV".casefold(): "ICCV",
    "CVPR".casefold(): "CVPR",
    "RSS".casefold(): "RSS",
    "Siggraph".casefold(): "Siggraph",
    "Siggraph Asia".casefold(): "Siggraph Asia",
}


def _normalize_venue(journal_or_booktitle):
    lowered = journal_or_booktitle.casefold()
    lowered = lowered.replace("\\&", "&").replace("&amp;", "&")
    lowered = lowered.replace("\u2013", "-").replace("\u2014", "-")
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return lowered


def _strip_venue_prefixes(journal_or_booktitle):
    cleaned = re.sub(r"^\d{4}\s+", "", journal_or_booktitle)
    cleaned = re.sub(r"^proceedings of the ", "", cleaned)
    cleaned = re.sub(r"^proceedings of ", "", cleaned)
    cleaned = re.sub(r"^the ", "", cleaned)
    return cleaned.strip()


def _clean_venue_text(journal_or_booktitle):
    cleaned = journal_or_booktitle.replace("\\&", "&")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"^\d{4}\s+", "", cleaned)
    return cleaned


jabbr_map = {_normalize_venue(key): value for key, value in _raw_jabbr_map.items()}


def _jabbr_mapping(journal_or_booktitle):
    lowered = _normalize_venue(journal_or_booktitle)
    stripped = _strip_venue_prefixes(lowered)

    for candidate in (lowered, stripped):
        if candidate in jabbr_map:
            return jabbr_map[candidate]

    if stripped.startswith("arxiv"):
        return "Arxiv"
    if "acm transactions on graphics" in stripped or stripped.startswith("acm trans. graph."):
        return "TOG"
    if "computer graphics forum" in stripped:
        return "CGF"
    if "transactions on visualization and computer graphics" in stripped:
        return "TVCG"
    if "computer animation and virtual worlds" in stripped:
        return "CAVW"
    if "computational visual media" in stripped:
        return "CVM"
    if "proceedings of the acm on computer graphics and interactive techniques" in stripped:
        return "PACMCGIT"
    if "conference on computer vision and pattern recognition" in stripped:
        return "CVPR"
    if "international conference on computer vision" in stripped:
        return "ICCV"
    if "european conference on computer vision" in stripped:
        return "ECCV"
    if "conference on neural information processing systems" in stripped or "neural information processing systems" in stripped:
        return "NeurIPS"
    if "international conference on learning representations" in stripped:
        return "ICLR"
    if stripped == "icml" or "international conference on machine learning" in stripped:
        return "ICML"
    if "aaai conference on artificial intelligence" in stripped:
        return "AAAI"
    if "international conference on robotics and automation" in stripped:
        return "ICRA"
    if "intelligent robots and systems" in stripped:
        return "IROS"
    if "robotics: science and systems" in stripped:
        return "RSS"
    if "annual review of fluid mechanics" in stripped:
        return "ARFM"
    if "annual review of control, robotics, and autonomous systems" in stripped:
        return "ARCRAS"
    if "computers & fluids" in stripped:
        return "Comput. Fluids"
    if "virtual reality & intelligent hardware" in stripped:
        return "VRIH"
    if "computational science -- iccs" in stripped or "computational science - iccs" in stripped:
        return "ICCS"
    if "special interest group on computer graphics and interactive techniques conference conference papers" in stripped:
        return "Siggraph"
    if "siggraph asia" in stripped:
        return "Siggraph Asia"
    if "siggraph" in stripped:
        return "Siggraph"
    return ""
