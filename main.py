import sys
from console_helper import bcolors, printc
from bluesky_helper import create_authenticated_client
from commands.FollowAllFollowersCommand import FollowAllFollowersCommand
from commands.FollowWhoLikedPost import FollowWhoLikedPost
from commands.FollowWhoLikedMyPosts import FollowWhoLikedMyPosts

#TODO: locale
if(len(sys.argv) < 3):
    printc("Username and password required", bcolors.FAIL)
    exit(1)

client=create_authenticated_client(sys.argv[1], sys.argv[2])
commands = {
    1: FollowAllFollowersCommand(client),
    2: FollowWhoLikedPost(client),
    3: FollowWhoLikedMyPosts(client)
}

print("What would you like to do?")
for index, (key, value) in enumerate(commands.items()):
    print(str(key) + " - " + value.title)
#TODO: validate user input
choice = int(input("Enter your choice: "))

commands[choice].run()
    
    