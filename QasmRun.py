#!/usr/bin/env python3

import ArgumentParser
import ExperimentUtils
from IBMQuantumExperience import IBMQuantumExperience



if __name__ == "__main__":
    # look for options from command line arguments
    (apiToken, backend, shots, timeout) = ArgumentParser.parseArgs()
    # if apiToken not passed as command line arg, look for file
    if apiToken is None:
        try:
            apiToken = open("./.qiskit_api_token", "r").read()
        except:
            apiToken = None
    # if apiToken still not found, read from input
    if apiToken is None or apiToken == "":
        apiToken = input("Enter your IBM Quantum Experience API token: \n> ")
    
    print("API token set...")
    api = IBMQuantumExperience(apiToken, verify=True)
    print("API engine created...")
    inputfile = ExperimentUtils.request_input_file()
    qasm = open(inputfile, "r").read()
    jobs = [{'qasm': qasm}]
    print(f"QASM code read from {inputfile}...")
    backends = ExperimentUtils.build_backend_dict(api.available_backends())
    if backend is None:
        print("Available backends:")
        for key, value in backends.items():
            print(f"    {key}: {value}")
        backend = ExperimentUtils.get_backend(backends[int(input("Enter the number of the backend to use: \n> "))], backends)
    else:
        backend = ExperimentUtils.get_backend(backend, backends)
    print(f"Attempting to execute QASM code on backend '{backend}'...")
    try:
        executionId = api.run_job(jobs, backend=backend, shots=shots)["qasms"][0]["executionId"]
        print(f"Successfully dispatched job with execution ID: {executionId} ...")
        result = api.get_result_from_execution(executionId)
        print(result)
    except:
        print(f"Failed to execute QASM file '{inputfile}' on backend '{backend}'!")