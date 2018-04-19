import argparse
from projectq.cengines import MainEngine
from projectq.backends import Simulator, IBMBackend

def makeEngine(compilerEngines):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    if (args.user is not None or args.password is not None):
        if (args.user is not None and args.password is not None):
            return MainEngine(IBMBackend(use_hardware=True, user=args.user, password=args.password), compilerEngines)
        else:
            raise ValueError("Password is required! usage: python ./shor.py -u username -p password")
    else:
        return MainEngine(Simulator(), compilerEngines)