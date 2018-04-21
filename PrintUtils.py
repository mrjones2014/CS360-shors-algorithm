class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = BOLD + UNDERLINE + OKGREEN

def printErr(str):
    print(f"{bcolors.FAIL}{str}{bcolors.ENDC}")

def printSuccess(str):
    print(f"{bcolors.OKGREEN}{str}{bcolors.ENDC}")

def printInfo(str):
    print(f"{bcolors.OKBLUE}{str}{bcolors.ENDC}")

def printWarning(str):
    print(f"{bcolors.WARNING}{str}{bcolors.ENDC}")

def printHeader(str):
    print(f"{bcolors.HEADER}{str}{bcolors.ENDC}")