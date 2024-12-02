import os
import shutil


def find_and_copy_cj_files(root_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.cj'):
                cj_file_path = os.path.join(subdir, file)
                destination_path = os.path.join(output_dir, file)

                shutil.copy2(cj_file_path, destination_path)
                print(f"Copied {cj_file_path} to {destination_path}")
