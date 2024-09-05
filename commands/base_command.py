class BaseCommand:
    def __init__(self, client, cache, title):
        self.client = client
        self.cache = cache
        self._title = title

    @property
    def title(self):
        return self._title
    