"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""
import argparse
from pathlib import Path
from typing import List, Optional
from bs4 import BeautifulSoup
from tqdm import tqdm
import htmlmin
from .latexml_parser import parse_latexml, _clean_html_whitespace
from .markdown import format_document


def check_file_path(paths: List[Path], wdir: Optional[Path] = None) -> List[str]:
    """
    Checks if the given file paths exist.

    Args:
        paths: A list of file paths.
        wdir: The working directory. If None, the current working directory is used.

    Returns:
        A list of file paths that exist.
    """
    files = []
    for path in paths:
        if type(path) == str:
            if path == "":
                continue
            path = Path(path)
        pathsi = [path] if wdir is None else [path, wdir / path]
        for p in pathsi:
            if p.exists():
                files.append((p.resolve()))
            elif "*" in path.name:
                files.extend([(pi.resolve()) for pi in p.parent.glob(p.name)])
    return list(set(files))

def convert_html_to_markdown(html_paths: List[Path], output_dir: Path):
    """
    Converts a list of HTML files to Markdown files.

    Args:
        html_paths: A list of Paths to the HTML files.
        output_dir: A Path to the directory where the Markdown files should be saved.
    """
    html_files = check_file_path(html_paths)
    for f in html_files:
        with open(f, "r", encoding="utf-8") as file:
            html = BeautifulSoup(
                htmlmin.minify(
                    file.read().replace("\xa0", " "),
                    remove_all_empty_space=True,
                ),
                features="html.parser",
            )

        try:
            doc = parse_latexml(html)
        except ValueError as e:
            print(e)
            continue

        if doc is None:
            continue

        out, fig = format_document(doc, keep_refs=True)
        outp = output_dir / (f.stem + ".md")
        with open(outp, "w", encoding="utf-8") as outfile:
            outfile.write(out)

# Example usage
if __name__ == "__main__":
    html_files = [Path("/path/to/html1.html"), Path("/path/to/html2.html")]
    output_directory = Path("/path/to/output")
    convert_html_to_markdown(html_files, output_directory)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--html", type=Path, nargs="+", help="HTML file", required=True)
#     parser.add_argument("--out", type=Path, help="Output file", required=True)
#     args = parser.parse_args()
#     args.html = check_file_path(args.html)
#     for f in tqdm(args.html):
#         html = BeautifulSoup(
#             htmlmin.minify(
#                 open(f, "r", encoding="utf-8").read().replace("\xa0", " "),
#                 remove_all_empty_space=1,
#             ),
#             features="html.parser",
#         )
#         try:
#             doc = parse_latexml(html)
#         except ValueError as e:
#             print(e)
#             continue
#         if doc is None:
#             continue
#         out, fig = format_document(doc, keep_refs=True)
#         outp = (args.out if args.out.is_dir() else args.out.parent) / (f.stem + ".mmd")
#         with open(outp, "w", encoding="utf-8") as f:
#             f.write(out)
