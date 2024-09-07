from commands.base_command import BaseCommand
from commands.follow_who_liked_post import FollowWhoLikedPost

class FollowWhoLikedMyPosts(BaseCommand):
    def __init__(self, client, cache):
        BaseCommand.__init__(self, client, cache, "Follow who liked all my posts")

    def run(self, _):
        subcommand = FollowWhoLikedPost(self.client, self.cache)
        #follows = get_follows(self.client)
        #TODO: handle feed pages
        feed = self.client.get_author_feed(self.client.me.handle)
        for _, feed_item in enumerate(feed.feed):
            if feed_item.post.author.handle != self.client.me.handle:
                print("Not user's post, skipping...")
                continue
            subcommand.follow_who_liked_post(feed_item.post)
