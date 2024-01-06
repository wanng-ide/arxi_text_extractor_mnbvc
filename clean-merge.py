import os
import re
import jsonlines
import pypandoc
from tqdm import tqdm

def tex_table_to_md(latex_table):
    return pypandoc.convert_text(latex_table, 'markdown_mmd', format='latex') # markdown_strict

def replace_latex_with_md(content):
    tables = re.findall(r'\\begin{tabular}.*?\\end{tabular}', content, re.DOTALL)
    for table in tables:
        markdown_table = tex_table_to_md(table)
        content = content.replace(table, markdown_table)
    return content

def process_files(folder_path):
    results = []
    dirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    for dir_name in tqdm(dirs, desc="Processing folders"):
        md_file_path = os.path.join(folder_path, dir_name, 'md_output', 'index.md')
        if os.path.exists(md_file_path):
            with open(md_file_path, 'r') as file:
                content = file.read()
                updated_content = replace_latex_with_md(content)
                results.append({"id": dir_name, "markdown": updated_content})
        else:
            results.append({"id": dir_name, "markdown": "[EMPTY]"})
    return results

def save_results_to_jsonl(results, output_file):
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(results)

# Replace this with your folder path
folder_path = 'parse-files'
output_file = 'output.jsonl'

results = process_files(folder_path)
save_results_to_jsonl(results, output_file)
