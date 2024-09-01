import time
from bluesky_helper import parse_post_url, WAIT_TIME_BETWEEN_LIKES
from commands.base_command import BaseCommand

class LikePostThread(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Like post thread")

    def run(self, args):
        (post_id, author_handle) = parse_post_url(args.element)
        post = self.client.get_post(post_id, author_handle)
        resp = self.client.get_post_thread(post.uri)
        num_replies = len(resp.thread.replies)
        for index, post in enumerate(resp.thread.replies):
            print("Liking reply " + str(index + 1) + " of " + str(num_replies) + " by " + post.post.author.handle)
            time.sleep(WAIT_TIME_BETWEEN_LIKES)
            self.client.like(post.post.uri, post.post.cid)
   