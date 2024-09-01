from bluesky_helper import get_page_and_run, follow_all
from console_helper import print_info, print_success, print_error
from commands.BaseCommand import BaseCommand

class FollowWhoLikedPost(BaseCommand):
    def __init__(self, client):
        BaseCommand.__init__(self, client, "Follow who liked post")
    
    def run(self, args):
        if args.element is None:
            print_error("Post url is required: -e <url>")
            exit(1)
        parts = args.element.split('/')
        author_handle=parts[4]
        post_id=parts[6]
        post = self.client.get_post(post_id, author_handle)
        self.follow_who_liked_post(post)

    def follow_who_liked_post(self, post, current_follows=[]):
        get_page_and_run(
            page_func=self.client.get_likes, 
            cid=post.uri, 
            list_prop="likes",
            action=lambda likes: self.get_users_and_follow_all(likes)
            )
        

    def get_users_and_follow_all(self, likes):
        users = [like.actor for like in likes]
        follow_all(users, self.client, skip_check_following=True)
        