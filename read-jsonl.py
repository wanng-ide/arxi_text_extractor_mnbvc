import jsonlines
import os

def read_and_save_markdown(input_file, output_folder):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 读取jsonl文件并保存非空Markdown内容
    with jsonlines.open(input_file) as reader:
        for obj in reader:
            if obj["markdown"] != "[EMPTY]":
                file_path = os.path.join(output_folder, f"{obj['id']}.md")
                with open(file_path, 'w') as file:
                    file.write(obj["markdown"])

# 输入文件和输出文件夹路径
input_file = 'output.jsonl'
output_folder = 'check-md-files'

read_and_save_markdown(input_file, output_folder)
