class QConfig: 
    def __init__(self, backend, shots, timeout, program=None):
        self.backend = backend
        self.shots = shots
        self.timeout = timeout
        self.program = program