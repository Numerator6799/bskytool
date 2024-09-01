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
    GRAY = '\033[15m'

def printc(message, color):
    print(color + message + bcolors.ENDC)

def print_info(message):
    printc(message, bcolors.OKCYAN)

def print_success(message):
    printc(message, bcolors.OKGREEN)

def print_error(message):
    printc(message, bcolors.FAIL)