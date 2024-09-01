import sys
import argparse
from console_helper import print_error
from bluesky_helper import create_authenticated_client
from helpers import get_credentials
from commands.FollowAllFollowersCommand import FollowAllFollowersCommand
from commands.FollowWhoLikedPost import FollowWhoLikedPost
from commands.FollowWhoLikedMyPosts import FollowWhoLikedMyPosts
from commands.LikePostThread import LikePostThread

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
