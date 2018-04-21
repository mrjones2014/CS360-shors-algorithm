import signal

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def handler(signum, frame):
    raise Exception()

def tryExecuteWithTimeout(func, timeout, failMessage):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    try:
        func()
    except Exception as ex:
        print(f"{bcolors.FAIL}{failMessage}{bcolors.ENDC}")