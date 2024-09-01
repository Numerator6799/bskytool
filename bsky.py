import argparse
from console_helper import print_error
from bluesky_helper import create_authenticated_client
from helpers import get_credentials
from commands.FollowAllFollowersCommand import FollowAllFollowersCommand
from commands.FollowWhoLikedPost import FollowWhoLikedPost
from commands.FollowWhoLikedMyPosts import FollowWhoLikedMyPosts

#TODO: locale
#TODO: linting
#TODO: tests
#TODO: GH workflow
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
}

if args.command not in commands.keys():
    print_error("Invalid command")
    exit(1)

commands[args.command].run(args)