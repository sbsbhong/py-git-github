import os
from dotenv import load_dotenv
from github import Github

load_dotenv(verbose=True)

USER_ID = os.environ.get('USER_ID')
USER_PASSWORD = os.environ.get('USER_PASSWORD')

def camel_to_snake(name:list):
    hyphen = '-'
    name[0] = name[0].lower()
    uppercase = []
    converted_name:list = []

    for item in name:
        if item is hyphen:
            converted_name.append(item)

        elif item.isupper():
            uppercase.append(item.lower())

        elif item.islower():
            if uppercase:
                if len(uppercase) > 1:
                    for i in range(1, len(uppercase)):
                        converted_name.append(uppercase.pop(0))

                        if len(uppercase) == 1:
                            break
                        
                converted_name.append(hyphen)
                converted_name.append(uppercase.pop())

            converted_name.append(item)
    return converted_name

def change_delimiter_to_hypen(name:str):
    name = list(name)
    space, underbar, comma, hyphen = ' ', '_', ',', '-'
    changed_delimiter_name:list = []

    for index, item in enumerate(name):
        if item.isalpha():
            changed_delimiter_name.append(item)

        elif item is space or underbar or comma: 
            changed_delimiter_name.append(hyphen)
            name[index + 1] = name[index + 1].lower() # Hyphen 뒤의 알파벳 --> 소문자

    return changed_delimiter_name

def change_name_suit_git(name:str):
    changed_delimiter_name:list = change_delimiter_to_hypen(name)
    converted_name:list = camel_to_snake(changed_delimiter_name)

    return ''.join(converted_name)
    
gh = Github(id_or_token=USER_ID, password=USER_PASSWORD)

if __name__ == '__main__':
    repos = gh.get_repos('HMEC8').data

    for repo in repos:
        print(repo.full_name)
        new_repo_name:str = change_name_suit_git(repo.name) # PyGitGithub_ChangeRepoName --> py-git-github-change-repo-name

        gh.patch_repo(repo.full_name, {
            'name' : new_repo_name
        })

        print("{} --> {}".format(repo.name, new_repo_name))
    