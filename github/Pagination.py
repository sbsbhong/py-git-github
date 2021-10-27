from .Attribute import Attribute

class Pagination:
    def add_attribute(self, data):
        if isinstance(data, list):
            all_items = []
            [all_items.append(Attribute(item)) for item in data]
            return all_items
        else:
            print("List가 아니다")

    def __init__(self, data:list, requester:object, router:str, per_page:int):
        self._data = self.add_attribute(data)
        self._requester = requester
        self._router = router
        self._per_page = per_page

    @property
    def data(self):
        return self._data

    def instance_name(self, index):
        if len(self._data) < index:
            return

        return self._data[index].name