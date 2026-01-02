from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def ejecutar_teleportacion():
    # Inicializar circuito: 3 qubits y 3 bits clásicos
    # q0: Mensaje a enviar
    # q1: Recurso de Alice
    # q2: Recurso de Bob
    qc = QuantumCircuit(3, 3)

    # Preparar el estado a teletransportar (Estado |1>)
    qc.x(0)
    qc.barrier()

    # Crear par entrelazado entre Alice y Bob
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # Alice interactúa con su parte
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    # Alice mide sus qubits y envía resultados clásicos
    qc.measure([0, 1], [0, 1])
    qc.barrier()

    # Bob aplica correcciones según los bits clásicos recibidos
    qc.cx(1, 2)
    qc.cz(0, 2)

    # Verificación: Medir el qubit de Bob
    qc.measure(2, 2)

    # Ejecutar simulación
    simulador = AerSimulator()
    job = simulador.run(qc, shots=1024)
    resultado = job.result()
    conteos = resultado.get_counts()

    print("Resultados:", conteos)

    # Guardar diagrama del circuito
    qc.draw('mpl', filename='circuito_teleportacion.png')
    print("Imagen guardada: circuito_teleportacion.png")

    # Guardar histograma de resultados
    plot_histogram(conteos).savefig('histograma_teleportacion.png')
    print("Imagen guardada")

if __name__ == "__main__":
    ejecutar_teleportacion()
