import json
import datetime
from bluesky_repo import get_follows, get_followers
from commands.base_command import BaseCommand

class BuildCache(BaseCommand):
    def __init__(self, client, cache):
        BaseCommand.__init__(self, client, cache, "Build Cache")

    def run(self, _):
        followers = get_followers(self.client)
        follows = get_follows(self.client)
        cache = {
            'created': datetime.datetime.now().isoformat(),
            'followers':  [{"did": f.did, "handle": f.handle} for f in followers], 
            'follows':  [{"did": f.did, "handle": f.handle} for f in follows], 
            }
        with open('fcache.json', 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)
            