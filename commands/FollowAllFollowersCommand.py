from bluesky_helper import get_paginated, follow_all
from commands.BaseCommand import BaseCommand

class FollowAllFollowersCommand(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow my followers")
    
    def run(self):
        followers = get_paginated(func=self.client.get_followers, cid=self.client.me.handle, list_prop="followers")
        print("Got " + str(len(followers)) + " followers")
        follow_all(followers, self.client)