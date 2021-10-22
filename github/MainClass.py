from .Requester import Requester
from .ApiRouter import ApiRouter

DEFAULT_BASE_URL = "http://api.github.com"
DEFAULT_PER_PAGE = 30


class Github:
    def __init__(self, base_url: str = DEFAULT_BASE_URL, id_or_token: str = None, password: str = None, per_page: str = DEFAULT_PER_PAGE):
        self._base_url = base_url
        self._id_or_token = id_or_token
        self._password = password
        self._per_page = per_page
        self._requester = Requester(id_or_token, password, base_url)
        self._router = ApiRouter(id_or_token, password)

    @property
    def per_page(self):
        return self._per_page

    @per_page.setter
    def per_page(self, value):
        self._per_page = value

        return self._per_page

    def _paging_responese(self): pass

    def get_repos(self, org: str): pass
    
    def get_org(self, org: str):
        router = self._router
        router.api_get_org(org)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path)

        return res

    def get_repo(self, repo_fullname: str):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_get_repo(org, repo)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path)

        return res

    def patch_repo(self, repo_fullname: str, update_data:dict):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_patch_repo(org, repo)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path, update_data)

        return res
