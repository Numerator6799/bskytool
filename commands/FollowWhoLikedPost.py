from bluesky_helper import get_paginated, follow_all
from commands.BaseCommand import BaseCommand

class FollowWhoLikedPost(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow who liked post")
    
    def run(self):
        post_id=input("Post id: ")
        author_handle=input("Author handle (leave blank to use " + self.client.me.handle + "): ")
        if len(author_handle) == 0:
            author_handle=self.client.me.handle
        post = self.client.get_post(post_id, author_handle)
        self.follow_who_liked_post(post)

    def follow_who_liked_post(self, post, current_follows=[]):
        print("Getting all likes for post. Please wait...")
        likes = get_paginated(func=self.client.get_likes, cid=post.uri, list_prop="likes")
        print("Got " + str(len(likes)) + " likes")
        users = [like.actor for like in likes]
        follow_all(users, self.client, current_follows)