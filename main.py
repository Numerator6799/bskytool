import sys
import time
from console_helper import bcolors, printc
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
            printc("You already follow " + p[handle_prop], bcolors.OKGREEN)
        else:
            print("Following " + p[handle_prop])
            client.follow(p[did_prop])
            time.sleep(WAIT_TIME_BETWEEN_FOLLOWS)



#TODO: validate args
username = sys.argv[1]
#TODO: locale
printc("Authenticating with user " + username, bcolors.OKCYAN)
client = Client(base_url='https://bsky.social')
client.login(username, sys.argv[2])
printc("Welcome, " + client.me.handle, bcolors.OKGREEN)
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
    
    