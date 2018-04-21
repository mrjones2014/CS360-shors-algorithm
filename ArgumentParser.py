import argparse

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apitoken", help="The IBM Quantum Experience API token to use if running on hardware backend.")
    parser.add_argument("-b", "--backend", help="The quantum backend to run the experiment on.")
    parser.add_argument("-s", "--shots", default=1, help="Number of shots to run for the experiment.")
    parser.add_argument("-t", "--timeout", help="Total time to wait until execution stops.")
    parser.add_argument("-p", "--program", help="Which quantum program to run.")
    parser.add_argument('-d', action='store_true', help="Use the default backend (default simulator).") 
    args = parser.parse_args()
    if args.d is True:
        args.backend = 1
    return args