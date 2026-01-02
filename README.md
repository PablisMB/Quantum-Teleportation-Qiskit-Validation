# Validación de Teleportación Cuántica con Qiskit

Este repositorio contiene el código fuente y la documentación asociada al artículo de investigación **"Entrelazamiento Cuántico y sus Aplicaciones en la Computación Cuántica"**.

El proyecto implementa una validación experimental del protocolo de teleportación cuántica utilizando el framework Qiskit y el simulador `AerSimulator`.

## Contenido del Repositorio

* `teleportacion.py`: Script de Python que ejecuta el circuito de teleportación, valida la transmisión del estado |1> y genera las visualizaciones.
* `QuantumEntanglementMerinoBarreraPablo.pdf`: Artículo científico completo con la fundamentación teórica, análisis de resultados y discusión del estado del arte (2026).
* `circuito_teleportacion.png`: Diagrama esquemático del circuito generado.
* `histograma_teleportacion.png`: Resultados estadísticos de la fidelidad del estado transmitido.

## Requisitos

El código ha sido validado en **Python 3.11**.

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
