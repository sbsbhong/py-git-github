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

    def set_get_method(self):
        self.type = 'GET'
        self.headers = self.return_headers()

    def set_patch_method(self, update_data):
        self.type = 'GET'
        self.headers = self.return_headers({'Content-Type': 'application/json'})

## Organization
    def api_get_org(self, org: str):
        self.set_get_method()
        self.path = "/orgs/{ORG}".format(ORG=org)

## Repository
    def api_get_repos(self, org: str):
        self.set_get_method()
        self.path = "/repos/{ORG}/repos".format(ORG=org)

    def api_get_repo(self, org: str, repo: str):
        self.set_get_method()
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)

    def api_patch_repo(self, org: str, repo: str):
        self.set_patch_method()
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)

