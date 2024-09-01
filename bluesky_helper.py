import time
from atproto import Client # type: ignore
from console_helper import bcolors, printc

WAIT_TIME_BETWEEN_PAGINATED_CALLS=1
WAIT_TIME_BETWEEN_FOLLOWS=1

def create_authenticated_client(username, password):
    printc("Authenticating with user " + username, bcolors.OKCYAN)
    client = Client(base_url='https://bsky.social')
    client.login(username, password)
    printc("Welcome, " + client.me.handle, bcolors.OKGREEN)
    return client

def get_paginated(func, cid, list_prop):
    printc("Getting a very big list, please wait...", bcolors.GRAY)
    stop = False
    list = []
    cursor=None
    while not stop:
        print(".")
        resp = func(cid, cursor=cursor, limit=100)
        time.sleep(WAIT_TIME_BETWEEN_PAGINATED_CALLS)
        list = list + resp[list_prop]
        cursor = resp.cursor
        if cursor == None:
            stop = True
    return list

def get_follows(client):
    follows = get_paginated(func=client.get_follows, cid=client.me.handle, list_prop="follows")
    print("Got " + str(len(follows)) + " follows")
    return follows

def follow_all(list, client, current_follows=[], handle_prop="handle", did_prop="did"):
    # maybe getting followers for comparison is not needed, 
    # but let's try to avoid too many calls to follow
    follows=current_follows
    if len(follows) == 0:
        follows = get_follows(client)
    for _, candidate_follow in enumerate(list):
        already_follow=False
        for _, follow in enumerate(follows):
            if follow.handle == candidate_follow[handle_prop]:
                already_follow=True
                break
        if already_follow:
            printc("You already follow " + candidate_follow[handle_prop], bcolors.OKGREEN)
        else:
            print("Following " + candidate_follow[handle_prop])
            client.follow(candidate_follow[did_prop])
            time.sleep(WAIT_TIME_BETWEEN_FOLLOWS)

