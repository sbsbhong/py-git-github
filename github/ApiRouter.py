class ApiRouter:
    def __init__(self, id_or_token:str):
        self._base_headers = {
            'Accept'        : "application/vnd.github.v3+json",
            'Authorization' : "token {}".format(id_or_token)
        }


    def return_headers(self, add_element:dict=None):
        if add_element is not None:
            headers = self._base_headers
            headers.update(add_element)

            return headers
        
        return self._base_headers


    def api_get_repos(self, org:str):
        self.type = 'GET'
        self.path = "/repos/{ORG}/repos".format(ORG=org)
        self.headers = self.return_headers()


    def api_get_repo(self, org:str, repo:str):
        self.type = 'GET'
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)
        self.headers = self.return_headers()
    

    def api_patch_repo(self, org:str, repo:str):
        self.type = 'PATCH'
        self.path = "/repos/{ORG}/{REPO}".format(ORG=org, REPO=repo)
        self.headers = self.return_headers({'Content-Type' : 'application/json'})