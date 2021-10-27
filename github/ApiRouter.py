"""class Router:
    def __init__(self, func):
        self._func = func
    
    def __call__(self, *args):
        pass"""


class ApiRouter:
    def __init__(self, id_or_token: str, password:str):
        self._base_headers = {
            'Accept': "application/vnd.github.v3+json",
            #token {}".format(id_or_token)
            'Authorization': "{} {}".format(id_or_token, password)
        }

    def return_headers(self, add_element: dict = None):
        if add_element is not None:
            headers = self._base_headers
            headers.update(add_element)

            return headers

        return self._base_headers
#=================================================================
    def set_get(self):
        self.type = 'GET'
        self.headers = self.return_headers()

    def set_patch(self):
        self.type = 'PATCH'
        self.headers = self.return_headers({'Content-Type': 'application/json'})
#=================================================================
    def api_get_org(self, org: str):
        self.set_get()
        self.path = "/orgs/{ORG}".format(ORG=org)

    def api_get_repos(self, org: str):
        self.set_get()
        self.path = "/orgs/{ORG}/repos".format(ORG=org)

    def api_get_repo(self, org: str, repo: str):
        self.set_get()
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)

    def api_patch_repo(self, org: str, repo: str, update_data:dict):
        self.set_patch()
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)
    
    def api_get_branches(self, org: str, repo: str):
        self.set_get()
        self.path = "/repos/{ORG}/{REPO}/branches".format(ORG=org, REPO=repo)

    def api_get_branch(self, org: str, repo: str, branch:str):
        self.set_get()
        self.path = "/repos/{ORG}/{REPO}/branches/{BRANCH}".format(ORG=org, REPO=repo, BRANCH=branch)