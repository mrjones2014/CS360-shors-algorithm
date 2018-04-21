#!/usr/bin/env python3

import sys
import QuantumCircuits
import ExperimentUtils
import SignalUtils
import PrintUtils
import random

def run(args):
    experiment = ExperimentUtils.setup_experiment(args)
    program = experiment.qconf.program
    timeout = experiment.qconf.timeout
    if program == "find_period":
        N = int(input("Enter a value for N:\nN = "))
        a = input("Enter a value for a (or type 'rand' for random value between 2..N-1):\na = ")
        if a == "rand":
            a = random.randint(2, N-1)
        else:
            a = int(a)
        def run_expr():
            r = experiment.find_period(a, N)
            PrintUtils.printSuccess(f"Found period r={r} for a={a} and N={N}.")
        SignalUtils.tryExecuteWithTimeout(run_expr, timeout, f"Failed to find period within timeout: {timeout} seconds.")
        return
    elif program == "factorize_N":
        N = int(input("Enter a value N to factorize:\nN = "))
        def run_expr():
            factors = experiment.factorize_N(N)
            PrintUtils.printSuccess(f"Found factors: {factors[0]} X {factors[1]} = {N}")
        SignalUtils.tryExecuteWithTimeout(run_expr, timeout, f"Failed to factorize {N} within timeout: {timeout} seconds.")
        return
    else: 
        PrintUtils.printErr(f"FATAL: Failed to find program '{program}'!")    

if __name__ == "__main__":
    run(None)