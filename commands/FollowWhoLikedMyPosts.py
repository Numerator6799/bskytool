from bluesky_helper import get_follows
from commands.BaseCommand import BaseCommand
from commands.FollowWhoLikedPost import FollowWhoLikedPost

class FollowWhoLikedMyPosts(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow who liked all my posts")
    
    def run(self, args):
        subcommand = FollowWhoLikedPost(self.client)
        #follows = get_follows(self.client)
        feed = self.client.get_author_feed(self.client.me.handle)
        for _, feed_item in enumerate(feed.feed):
            if feed_item.post.author.handle != self.client.me.handle:
                print("Not user's post, skipping...")
                continue
            subcommand.follow_who_liked_post(feed_item.post)