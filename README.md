# Laboratorio: Minimax y Poda Alfa-Beta

## Descripción
Este proyecto implementa los algoritmos Minimax y Poda Alfa-Beta para resolver un árbol de decisión simplificado.

## Objetivo
Comparar el resultado y la eficiencia de Minimax frente a Poda Alfa-Beta.

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
```bash
python -m src.main
```

## Pruebas
```bash
pytest --cov=src --cov-report=term-missing
```

## Preguntas de análisis

### 1. ¿Por qué Minimax y Alfa-Beta devuelven el mismo valor?

Ambos algoritmos buscan la mejor decisión suponiendo que MAX intenta obtener la puntuación más alta y MIN la más baja. Alfa-Beta aplica las mismas reglas que Minimax, pero deja de explorar una rama cuando ya sabe que esa rama no puede cambiar la decisión final. Por eso obtiene el mismo valor, aunque puede evaluar menos hojas.

### 2. ¿Cuándo Alfa-Beta reduce más nodos?

Reduce más nodos cuando examina primero las ramas que conducen a buenos resultados para MAX y a malos resultados para MIN. Así encuentra pronto límites que permiten descartar otras ramas. Si el árbol está bien ordenado, la poda puede ahorrar mucho trabajo.

### 3. ¿Qué ocurre si el árbol está mal ordenado?

El resultado final sigue siendo el mismo que con Minimax, pero Alfa-Beta puede podar menos ramas y terminar evaluando más nodos. El orden afecta la eficiencia de la búsqueda, no la decisión correcta.

### 4. ¿Cómo se aplicaría este algoritmo en ajedrez, damas o tres en raya?

Cada posición del juego se representa como un nodo y cada movimiento posible como una rama. Las posiciones finales reciben una puntuación: por ejemplo, favorable para MAX, desfavorable para MIN o empate. El algoritmo explora movimientos alternos y elige el que ofrece el mejor resultado suponiendo que el rival también juega de manera racional. En juegos grandes se limita la profundidad y se usa una función de evaluación.

## Conclusión

Minimax permite elegir una jugada considerando las respuestas racionales del rival. Alfa-Beta conserva la decisión de Minimax y ahorra evaluaciones cuando puede descartar ramas que no cambiarían el resultado.
