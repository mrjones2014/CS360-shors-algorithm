#!/usr/bin/env python3

from QuantumCircuits import QuantumPrograms
from qiskit import QuantumProgram
from QConfig import QConfig
from SignalUtils import tryExecuteWithTimeout
from random import randint
import time
import sys

def setup_quantum_program():
    timeout = 210 # 3.5 minutes
    # timeout = 80 # for debugging
    shots = 1024
    backend = 'local_qasm_simulator'
    program = 'factorize_N'

    engine = QuantumProgram()
    apiToken = None
    try:
        apiToken = open("./.qiskit_api_token", "r").read()
    except:
        apiToken = input("Enter your IBM Quantum Experience API token: \n> ")

    engine.set_api(apiToken, 'https://quantumexperience.ng.bluemix.net/api')
    config = QConfig(backend, shots, timeout, program)
    return QuantumPrograms(engine, config)

def run_benchmark(qp: QuantumPrograms, numberToFactor: int):
    initial = time.perf_counter()
    qp.factorize_N(numberToFactor)
    return (time.perf_counter() - initial)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    console = sys.stdout
    sys.stdout = None # stifle program output
    num_inputs = 10
    results = { 15: [] }

    for i in range(1, num_inputs):
        results[random_with_N_digits(i + 2)] = []

    num_trials = 10
    # num_trials = 3 # for debugging

    engine = setup_quantum_program()

    for i in results.keys():
        for j in range(0, num_trials):
            def run_experiment():
                res = run_benchmark(engine, i)
                results[i].append(res)
            tryExecuteWithTimeout(run_experiment, engine.qconf.timeout, f"Failed to factorize {i} within {engine.qconf.timeout} seconds.")
            if len(results[i]) <= j:
                results[i].append(-1) # use value of -1 to indicate timeout failure
    sys.stdout = console
    for i in results.keys():
        print(f"N={i}")
        count = 1
        resultSum = 0
        numNonZeroResults = 0
        for j in results[i]:
            if j > 0:
                numNonZeroResults += 1
                resultSum += j
            print(f"    Trial#{count}: {j}")
        results[i] = (resultSum / numNonZeroResults) # average of trials for each number
    try:
        sys.exit()
    except:
        try:
            quit()
        except:
            pass
