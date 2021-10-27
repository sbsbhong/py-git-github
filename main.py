import os
from dotenv import load_dotenv
from github import Github

load_dotenv(verbose=True)

USER_ID = os.environ.get('USER_ID')
USER_PASSWORD = os.environ.get('USER_PASSWORD')

# Login to use personal token
#gh = Github(id_or_token={TOKEN})

# Login
gh = Github(id_or_token=USER_ID, password=USER_PASSWORD)

if __name__ == '__main__':

    org = gh.get_org('TEAM-STARDUSTS')
    repos = gh.get_repos('TEAM-STARDUSTS')
    repo = gh.get_repo('TEAM-STARDUSTS/early-adopter')
    branches = gh.get_branches('TEAM-STARDUSTS/early-adopter')
    branches = repo.get_braches()
    branch = repo.get_branch('master')

    for repo in repos.data:
        print(repo.full_name)