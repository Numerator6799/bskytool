import sys
import argparse
import os
import json
from console_helper import print_error
from bluesky_repo import create_authenticated_client
from helpers import get_credentials
from commands.follow_all_followers_command import FollowAllFollowersCommand
from commands.follow_who_liked_post import FollowWhoLikedPost
from commands.follow_who_liked_my_posts import FollowWhoLikedMyPosts
from commands.like_post_thread import LikePostThread
from commands.build_cache import BuildCache

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

# Initialize cache
cache = None

file_path = 'fcache.json'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        cache = json.load(f)
    print("Cache loaded.")
else:
    print("JSON file does not exist.")

client=create_authenticated_client(username, password)
commands = {
    "ffollowers": FollowAllFollowersCommand(client, cache),
    "fpostlikes": FollowWhoLikedPost(client, cache),
    "fallmypostlikes": FollowWhoLikedMyPosts(client, cache),
    "likethread": LikePostThread(client, cache),
    "bcache": BuildCache(client, cache)
}

if args.command not in commands.keys():
    print_error("Invalid command")
    sys.exit(1)

commands[args.command].run(args)
