import sys
import os
from console_helper import print_error

#TODO: try to get from environment variables
def get_credentials(args):
    username = os.getenv("BSKY_USERNAME")
    if username is None:
        username=args.username
    if username is None:
        print_error("Username required")
        sys.exit(1)
    password = os.getenv("BSKY_PASSWORD")
    if password is None:
        password=args.password
    if password is None:
        print_error("Password required")
        sys.exit(1)
    return (username, password)
