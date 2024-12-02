import os
import git
import shutil

def clone_repository(repo_url):
    repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
    clone_dir = os.path.join("cloned_repo", repo_name)

    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    git.Repo.clone_from(repo_url, clone_dir)
    return repo_name, clone_dir
