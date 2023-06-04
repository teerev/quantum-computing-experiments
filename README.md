# quantum-computing-experiments
Toy models in quantum computing using qiskit.

## bell-state.py

This is a two qubit system initialised in a non-entangled purely classical state. Qubit 0 is passed to a Hadamard gate to put it into a state of full superposition. Then both qubits are passed through a CNOT gate to achieve a fully entangled Bell state (1/sqrt(2))(|00> + |11>). The Bell state is measured 1000 times and the state "collapses" to |00> and |11> with equal probability, illustrated by counting the |00> and |11> outcomes.

