import sys
import argparse
from console_helper import print_error
from bluesky_helper import create_authenticated_client
from helpers import get_credentials
from commands.follow_all_followers_command import FollowAllFollowersCommand
from commands.follow_who_liked_post import FollowWhoLikedPost
from commands.follow_who_liked_my_posts import FollowWhoLikedMyPosts
from commands.like_post_thread import LikePostThread

#TODO: cache
#TODO: locale
#TODO: session reuse: https://github.com/MarshalX/atproto/blob/main/examples/advanced_usage/session_reuse.py
#TODO: tests + gh workflow
parser = argparse.ArgumentParser(
    prog="bsky",
    description="Tool for BlueSky tricks",
    epilog="Thanks for using the tool!")

parser.add_argument('command')
parser.add_argument('-e', '--element', required=False)
parser.add_argument('-u', '--username', required=False)
parser.add_argument('-p', '--password', required=False)
parser.add_argument('-f', '--follow', required=False, action="store_true")
args=parser.parse_args()

(username, password) = get_credentials(args)

client=create_authenticated_client(username, password)
commands = {
    "ffollowers": FollowAllFollowersCommand(client),
    "fpostlikes": FollowWhoLikedPost(client),
    "fallmypostlikes": FollowWhoLikedMyPosts(client),
    "likethread": LikePostThread(client)
}

if args.command not in commands.keys():
    print_error("Invalid command")
    sys.exit(1)

commands[args.command].run(args)
