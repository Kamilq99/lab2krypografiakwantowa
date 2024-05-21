 
from qiskit import QuantumCircuit, Aer, execute

# Inicjalizacja obwodu kwantowego
qc = QuantumCircuit(7)

# Krok 1: Implementacja bramek Hadamarda dla qubitów q0 - q5
for i in range(6):
    qc.h(i)

# Krok 2: Sens działania bramek Hadamarda dla qubitów q0 - q5
# Bramki Hadamarda wprowadzają qubity w superpozycję stanów |0⟩ i |1⟩

# Krok 3: Implementacja operatora wyroczni z bramek CNOT
# W tym przypadku, użyjemy bramek CNOT na qubitach q6 i q0 - q5
for i in range(6):
    qc.cx(6, i)

# Krok 4: Sens logiczny operatora wyroczni z bramek CNOT
# Operator wyroczni pozwala na wykonanie operacji kontrolowanej, gdzie stan jednego qubitu (kontrolującego) 
# wpływa na stan innego qubitu (docelowego) zgodnie z regułami bramek CNOT.

# Krok 5: Rola qubitu q6 i bramki X
# Qubit q6 pełni rolę docelową dla operacji kontrolowanej przez pozostałe qubity.
# Pierwsza operacja bramki X na qubicie q6 jest wymagana, aby przygotować go do operacji kontrolowanej.

# Krok 6: Zaprojektowanie i symulacja własnego operatora wyroczni
# Tutaj możesz zaimplementować własne operatory wyroczni na podstawie wymagań i zinterpretować ich działanie.

# Wyświetlenie obwodu
print(qc)

# Symulacja obwodu na komputerze klasycznym
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()

# Wyświetlenie wyników symulacji
counts = result.get_counts(qc)
print("\nCounts:", counts)
