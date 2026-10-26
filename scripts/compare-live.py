"""Compare the local theme with a theme exported from Blogger.

Blogger's export re-encodes characters (e.g. an em dash becomes &#8212;),
self-closes empty elements and inlines its default widget includables
(comments, threaded_comments, post, ...). None of that is a real edit, so a
plain text diff is unreadable. This parses both files as XML, drops the
Blogger defaults the local theme doesn't define, and prints what is left.

Usage (Theme -> Backup in Blogger first, then):
    python scripts/compare-live.py path/to/theme-265273498279233553.xml

No output means the live theme has nothing the local file is missing.
"""

import difflib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

B = "{http://www.google.com/2005/gml/b}"
LOCAL = Path(__file__).resolve().parent.parent / "pwavwe-papers-editorial-theme.xml"


def includable_ids(root):
    return {w.get("id"): {i.get("id") for i in w.iter(B + "includable")}
            for w in root.iter(B + "widget")}


def drop_blogger_defaults(live, local):
    keep = includable_ids(local)
    for widget in live.iter(B + "widget"):
        wanted = keep.get(widget.get("id"), set())
        for child in list(widget):
            if child.tag == B + "includable" and child.get("id") not in wanted:
                widget.remove(child)


def flatten(root):
    lines = []

    def text_lines(value, indent, mark):
        if value and value.strip():
            for line in value.strip().splitlines():
                lines.append(indent + mark + line.strip())

    def walk(el, depth):
        indent = "  " * depth
        attrs = " ".join(f"{k}={v}" for k, v in sorted(el.attrib.items()))
        lines.append(f"{indent}<{el.tag.split('}')[-1]} {attrs}>")
        text_lines(el.text, indent, "| ")
        children = list(el)
        # Blogger reorders includables alphabetically; compare them by id.
        includables = sorted((c for c in children if c.tag == B + "includable"),
                             key=lambda c: c.get("id"))
        for child in [c for c in children if c.tag != B + "includable"] + includables:
            walk(child, depth + 1)
        text_lines(el.tail, indent, "~ ")

    walk(root, 0)
    return lines


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    live = ET.parse(sys.argv[1]).getroot()
    local = ET.parse(LOCAL).getroot()
    drop_blogger_defaults(live, local)
    diff = list(difflib.unified_diff(flatten(live), flatten(local),
                                     "live", "local", n=2, lineterm=""))
    print("\n".join(diff))
    sys.exit(1 if diff else 0)


if __name__ == "__main__":
    main()
