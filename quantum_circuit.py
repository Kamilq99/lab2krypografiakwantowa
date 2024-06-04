import qiskit

# Inicjalizacja qubitów
q = qiskit.QuantumCircuit(6)

# Stosowanie bramek Hadamarda na qubity 90-95
q.h(2)
q.h(3)
q.h(4)
q.h(5)

# Stosowanie bramek CNOT na qubity 90 i 91, 91 i 92, 92 i 93, 93 i 94, 94 i 95
q.cx(2, 3)
q.cx(3, 4)
q.cx(4, 5)

# Stosowanie bramki X na qubit qe
q.x(0)

# Pomiar qubitów 90-96
q.measure_all()

# Uruchamianie symulatora
backend = qiskit.Aer.get_backend('qvm')
job = qiskit.execute(q, backend, shots=1024)
result = job.result().get_counts()

# Wyświetlanie wyników
print(result)