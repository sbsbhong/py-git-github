class makeAttribute:
    def __init__(self, value):
        self.value = value

class Attribute:
    def __init__(self, data):
        self._data = data
    
    def check_and_add_attribute(self, dict:dict, key:dict):
        if key in dict: return makeAttribute(dict[key])
        else: return makeAttribute(None)
        
    @property
    def raw_data(self):
        self._raw_data = makeAttribute(self._data)
        return self._raw_data.value

    @property
    def id(self):
        self._id = self.check_and_add_attribute(self._data, 'id')
        return self._id.value

    @property
    def name(self):
        self._name = self.check_and_add_attribute(self._data, 'name')
        return self._name.value

    @property
    def full_name(self):
        self._full_name = self.check_and_add_attribute(self._data, 'full_name')
        return self._full_name.value

    @property
    def commit(self):
        self._commit = self.check_and_add_attribute(self._data, 'commit')
        return self._commit.value

    @property
    def commit_sha(self):
        self._commit_sha = self.check_and_add_attribute(self.commit, 'sha')
        return self._commit_sha.value
    
    @property
    def commit_url(self):
        self._commit_url = self.check_and_add_attribute(self.commit, 'url')
        return self._commit_url.value
