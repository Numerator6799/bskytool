from bluesky_helper import get_paginated, follow_all
from commands.BaseCommand import BaseCommand

class FollowLikeActorsFromPost(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow who liked post")
    
    def run(self):
        element_id=input("Post id: ")
        author_handle=input("Author handle (leave blank to use " + self.client.me.handle + "): ")
        if len(author_handle) == 0:
            author_handle=self.client.me.handle
        post = self.client.get_post(element_id, author_handle)
        print("Getting all likes for post " + post.value.text + ". Please wait...")
        likes = get_paginated(func=self.client.get_likes, cid=post.uri, list_prop="likes")
        print("Got " + str(len(likes)) + " likes")
        users = [like.actor for like in likes]
        follow_all(users, self.client)