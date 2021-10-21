from github.Requester import Requester
from .ApiRouter import ApiRouter

default_base_url = "http://github.com/api/v3"
default_per_page = 30

class Github:
    def __init__(self, base_url:str=default_base_url, id_or_token:str=None, password:str=None, per_page:str=default_per_page):
        self._base_url = base_url
        self._id_or_token = id_or_token
        self._password = password
        self.per_page = per_page
        self._requester = Requester(id_or_token, base_url)
        self._router = ApiRouter(id_or_token)
    
    def _paging_responese(self):pass

    def get_repos(self, org:str):pass

    def get_repo(self, repo_fullname:str):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_get_repo(org, repo)

        res = self._requester.request_to_hub(router.headers, router.type, router.path)
        
        return res

    def patch_repo(self, repo_fullname:str):pass