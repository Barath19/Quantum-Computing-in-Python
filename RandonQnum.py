from projectq.ops import  H, Measure
from projectq import MainEngine
'''
This code creates a qubit and applies a Hadamard gate to put
the qubit in a superposition state. And then generate 10 random states(numbers)
by measuring the qubit

'''

def get_random_number(quantum_engine):
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number

random_numbers_list = []

quantum_engine = MainEngine() # initialises a new quantum backend

for i in range(10):
   
    random_numbers_list.append(get_random_number(quantum_engine))

quantum_engine.flush()# Flushes the quantum engine from memory
print('Random numbers', random_numbers_list)