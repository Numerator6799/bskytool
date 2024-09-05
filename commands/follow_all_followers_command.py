from bluesky_repo import get_page_and_run, follow_all
from commands.base_command import BaseCommand

class FollowAllFollowersCommand(BaseCommand):
    def __init__(self, client, cache):
        BaseCommand.__init__(self, client, cache, "Follow my followers")

    def run(self, _):
        get_page_and_run(
            page_func=self.client.get_followers,
            cid=self.client.me.handle,
            list_prop="followers",
            action=lambda followers: follow_all(followers, self.client, self.cache["follows"])
            )
    