try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

def install(package):
   pipmain(['install', package])

def installQISKit():
    install('qiskit')