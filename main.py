import sys
from atproto import Client

#TODO: split into another file
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
choice = int(input("Enter your choice:"))

#TODO: commands, command mapping
if choice == 1:
    #TODO: pagination
    resp = client.get_followers(client.me.handle, cursor=None, limit=100)
    followers = resp.followers
    print("Got " + str(len(followers)) + " followers")
    resp = client.get_follows(client.me.handle, cursor=None, limit=100)
    follows = resp.follows
    print("Got " + str(len(follows)) + " follows")
    for index, follower in enumerate(followers):
        already_follow=False
        for index2, follow in enumerate(follows):
            if follow.handle == follower.handle:
                already_follow=True
                break
        if already_follow:
            print(bcolors.OKGREEN + "You already follow " + follower.handle + bcolors.ENDC)
        else:
            print("Following " + follower.handle)
            client.follow(follower.did)



