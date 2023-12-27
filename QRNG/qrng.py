import cirq
from matplotlib import pyplot as plt

def quantum_random_number_generator(num_bits):
    # Create a quantum circuit with the given number of qubits
    qubits = cirq.LineQubit.range(num_bits)
    circuit = cirq.Circuit()

    # Apply a Hadamard gate to create a superposition of all possible states
    ops = [cirq.H(q) for q in qubits]
    circuit.append(ops)

    # Measure qubits to collapse the superposition into classical bits
    circuit.append(cirq.measure(q, key=f'qubit-{i}') for i, q in enumerate(qubits))

    # Simulate the circuit
    s = cirq.Simulator()
    samples = s.run(circuit, repetitions=1)

    # Extract and concatenate the measurement results to form the random number
    bit_list =''.join(str(samples.measurements[f'qubit-{i}'][0]) for i in range(num_bits)).strip('[]').split('][')
    random_number = int(''.join(bit_list), 2)

    return random_number

def display_randomness(n):
    generated_numbers = list()
    
    for i in range(n):
        generated_numbers.append(quantum_random_number_generator(num_bits))
    
    plt.plot(generated_numbers)
    plt.show()


# Main Function
if __name__ == "__main__":
    print("Enter the number of qubits to simulate")
    num_bits = int(input())
    print("Press g to generate a random number or r to display randomness")
    x = input()
    if x == "g":
        generated_number = quantum_random_number_generator(num_bits)
        print(f"Generated Quantum Random Number (using {num_bits} qubits): {generated_number}")
    elif x == "r":
        print("How many times do you want to run the simulation?")
        n = int(input())
        display_randomness(n)
    else:
        print("Invalid input, application terminating")
        exit()
