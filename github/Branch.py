from .Attribute import Attribute

class Branch:
    def __init__(self, requester:object, router:object, data:dict, per_page:int):
        self._requester = requester
        self._router = router
        self._data = Attribute(data)
        self._per_page = per_page
    
    @property
    def data(self):
        return self._data