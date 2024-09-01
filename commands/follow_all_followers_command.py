from bluesky_helper import get_page_and_run, follow_all
from commands.base_command import BaseCommand

class FollowAllFollowersCommand(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow my followers")

    def run(self, _):
        get_page_and_run(
            page_func=self.client.get_followers,
            cid=self.client.me.handle,
            list_prop="followers",
            action=lambda followers: follow_all(followers, self.client, skip_check_following=True)
            )
    