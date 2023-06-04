# !pip install qiskit

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# creat a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# apply Hadamard gate to qubit 0 to put it into superposition of |0> and |1>
qc.h(0)

# CNOT gate to fully entangle the two qubits
qc.cx(0, 1)

# measure the qubits
qc.measure([0,1], [0,1])

# create a quantum simulator and run the circuit 1000 times
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)

result = job.result()
counts = result.get_counts(qc)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
print(qc.draw(output='text'))

