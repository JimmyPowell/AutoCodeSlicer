import os
import re
import json


def process_files(input_dir, output_file):
    functions = []

    # 遍历 sourcecode 目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.cj'):
            file_path = os.path.join(input_dir, filename)

            with open(file_path, 'r', encoding='UTF-8') as file:
                lines = file.readlines()

            inside_function = False
            brace_count = 0
            function_lines = []

            for line in lines:
                stripped_line = line.strip()

                if re.findall("func", line):
                    inside_function = True
                    function_lines = []  # 重置当前函数的行缓存

                if inside_function:
                    # 更新大括号计数
                    brace_count += stripped_line.count("{")
                    brace_count -= stripped_line.count("}")

                    # 缓存函数体的行
                    function_lines.append(line)

                    # 当大括号计数为零时，函数结束
                    if brace_count == 0:
                        inside_function = False
                        function_lines_str = ''.join(function_lines)
                        functions.append({"function": function_lines_str})

    # 将结果保存到 JSONL 文件中
    with open(output_file, 'w', encoding='UTF-8') as output_file:
        for function in functions:
            json.dump(function, output_file)
            output_file.write('\n')

