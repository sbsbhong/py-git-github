from .Attribute import Attribute
from .Pagination import Pagination
from .Branch import Branch

        

class Repository:
    def __init__(self, requester:object, router:object, data:dict, per_page:int):
        self._requester = requester
        self._router = router
        self._data = Attribute(data)
        self._per_page = per_page
    
    @property
    def data(self):
        return self._data

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

    def get_braches(self):
        [org, repo] = self.data.full_name.split('/')

        router = self._router
        router.api_get_branches(org, repo)

        res = self._paging_responese(router.headers, router.type, router.path)

        return Pagination(res, self._requester, self._router, self._per_page)
    
    def get_branch(self, branch:str):
        [org, repo] = self.data.full_name.split('/')

        router = self._router
        router.api_get_branch(org, repo, branch)

        res = self._requester.request_to_hub(
            router.headers, router.type, router.path)

        return Branch(self._requester, self._router, res, self._per_page)