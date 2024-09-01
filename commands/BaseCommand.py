class BaseCommand:
    def __init__(self, client, title):
        self.client = client
        self._title = title

    @property
    def title(self):
        return self._title