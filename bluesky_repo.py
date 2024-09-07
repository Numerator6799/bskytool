import sys
import time
from atproto import Client # type: ignore
from console_helper import print_info, print_success, print_error

WAIT_TIME_BETWEEN_PAGINATED_CALLS=1
WAIT_TIME_BETWEEN_FOLLOWS=1
WAIT_TIME_BETWEEN_LIKES=1

def create_authenticated_client(username, password):
    print_info("Authenticating with user " + username)
    client = Client(base_url='https://bsky.social')
    client.login(username, password)
    print_success("Welcome, " + client.me.handle)
    return client

def get_paginated(func, cid, list_prop):
    print_info("Please wait...")
    stop = False
    items = []
    cursor=None
    while not stop:
        print(".")
        resp = func(cid, cursor=cursor, limit=100)
        time.sleep(WAIT_TIME_BETWEEN_PAGINATED_CALLS)
        items = items + resp[list_prop]
        cursor = resp.cursor
        if cursor is None:
            stop = True
    return items

def get_page_and_run(page_func, cid, list_prop, action):
    stop = False
    cursor=None
    while not stop:
        print("Getting next " + list_prop + "...")
        resp = page_func(cid, cursor=cursor, limit=100)
        time.sleep(WAIT_TIME_BETWEEN_PAGINATED_CALLS)
        action(resp[list_prop])
        cursor = resp.cursor
        if cursor is None:
            stop = True

def get_follows(client):
    print_info("Getting current follows")
    follows = get_paginated(func=client.get_follows, cid=client.me.handle, list_prop="follows")
    print_success("Got " + str(len(follows)) + " follows")
    return follows

def get_followers(client):
    print_info("Getting current followers")
    followers = get_paginated(func=client.get_followers, cid=client.me.handle, list_prop="followers")
    print_success("Got " + str(len(followers)) + " followers")
    return followers

def follow_all(users,
               client,
               current_follows,
               handle_prop="handle",
               did_prop="did"):
    for _, candidate_follow in enumerate(users):
        already_follow=False
        for _, follow in enumerate(current_follows):
            if follow["handle"] == candidate_follow[handle_prop]:
                already_follow=True
                break
        if already_follow:
            print_success("You already follow " + candidate_follow[handle_prop])
        else:
            print("Following " + candidate_follow[handle_prop])
            client.follow(candidate_follow[did_prop])
            time.sleep(WAIT_TIME_BETWEEN_FOLLOWS)


def parse_post_url(url):
    if url is None:
        print_error("Post url is required: -e <url>")
        sys.exit(1)
    parts = url.split('/')
    author_handle=parts[4]
    post_id=parts[6]
    return(post_id, author_handle)
