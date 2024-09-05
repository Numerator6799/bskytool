from bluesky_repo import get_page_and_run, follow_all, parse_post_url
from commands.base_command import BaseCommand

class FollowWhoLikedPost(BaseCommand):
    def __init__(self, client, cache):
        BaseCommand.__init__(self, client, cache, "Follow who liked post")

    def run(self, args):
        (post_id, author_handle) = parse_post_url(args.element)
        post = self.client.get_post(post_id, author_handle)
        self.follow_who_liked_post(post)

    def follow_who_liked_post(self, post):
        get_page_and_run(
            page_func=self.client.get_likes,
            cid=post.uri,
            list_prop="likes",
            action=lambda likes: self.get_users_and_follow_all(likes)
            )

    def get_users_and_follow_all(self, likes):
        users = [like.actor for like in likes]
        follow_all(users, self.client, self.cache["follows"])
        