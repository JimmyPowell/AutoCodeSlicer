import os
from clone_repo import clone_repository
from code_slicer import process_files
from copy_cj_files import find_and_copy_cj_files
import os
def main():
    repo_url = input("请输入仓库地址: ")
    repo_name, clone_dir = clone_repository(repo_url)

    sourcecode_dir = 'sourcecode'
    find_and_copy_cj_files(clone_dir, sourcecode_dir)

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"{repo_name}.jsonl")
    process_files(sourcecode_dir, output_file)

    print(f"处理完成，结果保存在 {output_file}")

if __name__ == "__main__":
    main()