from console_helper import print_error

#TODO: try to get from environment variables
def get_credentials(args):
    if args.username is None:
        print_error("Username and password required")
        exit(1)
    return (args.username, args.password)