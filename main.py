import sys
import time
from atproto import Client # type: ignore

WAIT_TIME_BETWEEN_PAGINATED_CALLS=3
WAIT_TIME_BETWEEN_FOLLOWS=3
#TODO: split into another file

def get_paginated(func, cid, list_prop):
    stop = False
    list = []
    cursor=None
    while not stop:
        print(".", end=" ")
        resp = func(cid, cursor=cursor, limit=100)
        time.sleep(WAIT_TIME_BETWEEN_PAGINATED_CALLS)
        list = list + resp[list_prop]
        cursor = resp.cursor
        if cursor == None:
            stop = True
    return list

def follow_all(list, client, handle_prop="handle", did_prop="did"):
    # maybe getting followers for comparison is not needed, but let's try to avoid
    # too many calls to follow
    follows = get_paginated(func=client.get_follows, cid=client.me.handle, list_prop="follows")
    print("Got " + str(len(follows)) + " follows")
    for index, p in enumerate(list):
        already_follow=False
        for index2, follow in enumerate(follows):
            if follow.handle == p[handle_prop]:
                already_follow=True
                break
        if already_follow:
            print(bcolors.OKGREEN + "You already follow " + p[handle_prop] + bcolors.ENDC)
        else:
            print("Following " + p[handle_prop])
            client.follow(p[did_prop])
            time.sleep(WAIT_TIME_BETWEEN_FOLLOWS)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#TODO: validate args
username = sys.argv[1]
#TODO: locale
print(bcolors.OKCYAN + "Authenticating with user " + username + bcolors.ENDC)
client = Client(base_url='https://bsky.social')
client.login(username, sys.argv[2])
print(bcolors.OKGREEN + "Welcome, " + client.me.handle + bcolors.ENDC)
#TODO: menu array, validate user input
print("What would you like to do?")
print("1 - Follow my followers")
print("2 - Follow who liked a post or comment")
# print("3 - Like all comments in post")
choice = int(input("Enter your choice:"))

#TODO: commands, command mapping
if choice == 1:

    followers = get_paginated(func=client.get_followers, cid=client.me.handle, list_prop="followers")
    print("Got " + str(len(followers)) + " followers")
    follows = get_paginated(func=client.get_follows, cid=client.me.handle, list_prop="follows")
    print("Got " + str(len(follows)) + " follows")
    follow_all(followers, client)
if choice == 2:
    element_id=input("Element id:")
    author_handle=input("Author handle:")
    post = client.get_post(element_id, author_handle)
    print("Getting all likes for post " + post.value.text + ". Please wait...")
    likes = get_paginated(func=client.get_likes, cid=post.uri, list_prop="likes")
    print("Got " + str(len(likes)) + " likes")
    users = [like.actor for like in likes]
    follow_all(users, client)
    
    