from .Requester import Requester
from .ApiRouter import ApiRouter
from .Pagination import Pagination
from .Repository import Repository


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

    def _paging_responese(self, headers:dict, type:str, api_route:str, updata_data:str=None, total_page:int=None, success_code:int=200):
        page = 1
        res_store:list = []

        while True:
            route = api_route + "?per_page={}&page={}".format(self._per_page, page)
            res = self._requester.request_to_hub(headers, type, route, updata_data, success_code)

            [res_store.append(item) for item in res]

            if len(res) is not self._per_page:
                break
            
            page += 1

        return res_store

    def get_org(self, org: str):
        router = self._router
        router.api_get_org(org)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path)

        return res

    def get_repos(self, org: str):
        router = self._router
        router.api_get_repos(org)

        res = self._paging_responese(router.headers, router.type, router.path)

        return Pagination(res, self._requester, self._router, self._per_page)
    
    def get_branches(self, repo_fullname: str):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_get_branches(org, repo)

        res = self._paging_responese(router.headers, router.type, router.path)

        return Pagination(res, self._requester, self._router, self._per_page)

    def get_repo(self, repo_fullname: str):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_get_repo(org, repo)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path)
        
        return Repository(self._requester, self._router, res, self._per_page)

    def patch_repo(self, repo_fullname: str, update_data:dict):
        [org, repo] = repo_fullname.split('/')

        router = self._router
        router.api_patch_repo(org, repo, update_data)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path, update_data)

        return Repository(self._requester, self._router, res, self._per_page)
    
    
