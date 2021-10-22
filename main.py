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

org = gh.get_org('TEAM-STARDUSTS')
repo = gh.get_repo('TEAM-STARDUSTS/early-adopter')
