# Wiracochas-3
Grupo para los proyectos de la Universidad Andina del cusco

# Proyecto de Análisis de Deserción Estudiantil

Este proyecto utiliza un conjunto de datos de estudiantes para predecir la deserción utilizando varios algoritmos de machine learning, como la Regresión Logística, Árboles de Decisión, Random Forest, K-Nearest Neighbors, Support Vector Machines, y Gradient Boosting.

## Estructura del Proyecto

- `data_cleaning.py`: Este script se encarga de limpiar y normalizar el conjunto de datos.
- `model.py`: Este script contiene varios modelos de machine learning para la predicción de deserción estudiantil. Compara el rendimiento de los modelos y muestra sus métricas de evaluación.

## Dataset

El conjunto de datos utilizado en este proyecto incluye las siguientes variables:
- `Edad`: Edad del estudiante.
- `Promedio_calificaciones_semestre_anterior`: Promedio de calificaciones en el semestre anterior.
- `Asignaturas_reprobadas`: Número de asignaturas reprobadas.
- `Asignaturas_aprobadas`: Número de asignaturas aprobadas.
- `Numero_semestres_matriculado`: Número de semestres en los que el estudiante se ha matriculado.
- `Asistencia`: Porcentaje de asistencia del estudiante.
- `Distancia_universidad`: Distancia de la casa del estudiante a la universidad.
- `Desercion`: Variable objetivo que indica si el estudiante ha desertado.

## Requisitos

Para ejecutar este proyecto necesitarás instalar las dependencias listadas en `requirements.txt`. Para instalarlas, usa el siguiente comando:

```bash
pip install -r requirements.txt
