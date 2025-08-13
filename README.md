# Ta-Te-Ti en Python

**Autor:** Joaquin Vanrell  
**Carrera:** Ingeniería en Informática — Universidad de Mendoza  
**Materia:** Computación I — Año 2025

---

## 📌 Descripción
Este proyecto implementa el clásico juego **Ta-Te-Ti** (Tres en Línea) para dos jugadores, ejecutado en consola.  
El diseño sigue un enfoque de **Programación Orientada a Objetos (POO)** con separación clara entre:

- **Modelo**: lógica y reglas del juego.
- **Interfaz de Consola (CLI)**: interacción con el usuario.
- **Pruebas unitarias**: validación del correcto funcionamiento del modelo.

---

## 🛠 Ejecución del programa

- python -m src.main

## 🛠 Ejecución de los tets

- python -m unittest

## 🏗 Diseño de Clases
# 1. Jugador

- Atributos:

nombre (str)
ficha (str) → 'X' o '0'
estado (str) → Jugando / Ganador / Perdedor / Empate

Representa a un jugador y su estado en la partida.

2. Tablero

- Atributos:
contenedor → lista 3x3 con las fichas.

- Métodos:
colocar_ficha → Valida y coloca la ficha.
chequear_ganador → Detecta si hay 3 en línea.
chequear_empate → Detecta si el tablero está lleno sin ganador.

Responsable de todas las reglas del juego.

3. Tateti

- Coordina:
Turnos entre jugadores.
Traducción de entrada del usuario (1–3 a índices 0–2).
Llamadas al tablero para colocar fichas y verificar estados.
No contiene lógica de validación interna del tablero (delegada a Tablero).

4. main.py (CLI)

Muestra el tablero en consola.
Solicita jugadas.
Captura excepciones para mostrar mensajes claros.

## Estructura del Proyecto

├── src
│   ├── main.py          # CLI del juego
│   ├── tateti.py        # Lógica del juego y control de turnos
│   ├── tablero.py       # Modelo y validaciones del tablero
│   ├── jugador.py       # Clase Jugador
│   ├── excepciones.py   # Excepciones personalizadas
│
├── test
│   ├── test_jugador.py
│   ├── test_tablero.py
│   ├── test_tateti.py
│   └── test_excepciones.py
│
└── README.md

