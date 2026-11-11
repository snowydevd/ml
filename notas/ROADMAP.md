# ROADMAP: clasificador de imágenes de autos / motos / car meets

Objetivo: entrenar un modelo binario que diga si una imagen tiene que ver con autos, motos o car meets (**positivo**) o no (**negativo**). Caso de uso: filtrar las imágenes que se suben a los eventos de Gridd.

## Mi nivel (leer antes de armar cada guía)

**Soy principiante en machine learning.** Soy desarrollador full-stack (TypeScript, Node, React) y sé programar, pero:

- Mi Python está oxidado y nunca usé NumPy, pandas, matplotlib ni scikit-learn en serio
- Sé álgebra y derivadas básicas, pero casi nada de estadística
- No conozco ningún concepto de ML: modelo, entrenamiento, pérdida, gradiente, overfitting, métricas… todo es nuevo

Cómo quiero que me enseñen:

- **Explica cada concepto la primera vez que aparece**, aunque parezca obvio: qué es, para qué sirve y por qué se usa acá
- Usa **analogías y ejemplos con números chicos** (3 o 4 datos calculados a mano) antes de la fórmula general
- Cuando aparezca una fórmula, explica qué significa cada símbolo en palabras
- Si algo de Python o NumPy es raro viniendo de JavaScript (slicing, broadcasting, `axis`), avísame y compáralo con JS
- **Pasos chicos**: prefiero muchas guías cortas a una guía larga
- En cada paso, agrega un `print` o un gráfico para que **vea** el resultado, no solo que el código corra

## Convenciones del proyecto

- Scripts `.py` con celdas `# %%` dentro de `src/` (se ejecutan por celda en VS Code, como un notebook)
- Explicaciones y respuestas teóricas en `notas/NN_tema.md`, escritas con mis palabras
- Datos en `data/` (no se versionan)
- Primero lo implemento a mano y después lo comparo con la librería
- Entorno: CachyOS, fish (`source venv/bin/activate.fish`)

## Módulos

Cada módulo se divide en varias guías de wanna-learn (`/want-to-learn Módulo N, clase M de ROADMAP.md: ...`).

| # | Tema | Qué aprendo / construyo | Tiempo | Estado |
|---|---|---|---|---|
| 1 | Python y NumPy para ML | Repaso de Python desde JS. Arrays, `shape`, indexing, operaciones vectorizadas, broadcasting. pandas para leer un CSV y explorarlo. matplotlib para graficar | 2 sem | ⬜ |
| 2 | ¿Qué es "aprender"? Regresión lineal | Qué es un modelo, qué son los parámetros, qué es la pérdida (MSE). Derivadas como "hacia dónde bajar". Gradient descent desde cero y el efecto del learning rate. Train/test split y por qué existe. Escalado de features | 3 sem | ⬜ |
| 3 | Clasificación binaria | De predecir números a predecir sí/no. Sigmoide, probabilidad, umbral. Binary cross-entropy. Regresión logística desde cero. Matriz de confusión, accuracy, precision, recall | 2–3 sem | ⬜ |
| 4 | Imágenes como datos | Una imagen es una matriz de números. Pillow + NumPy: cargar, redimensionar, normalizar. Primer clasificador de autos con regresión logística sobre píxeles, y entender por qué funciona mal | 2 sem | ⬜ |
| 5 | Redes neuronales | Neurona = regresión logística. Capas, activaciones. Backpropagation explicado paso a paso con números chicos. MLP desde cero y después en PyTorch | 3 sem | ⬜ |
| 6 | CNNs | Qué es una convolución (con ejemplos visuales), pooling, data augmentation. CNN chica entrenada con mi dataset | 2–3 sem | ⬜ |
| 7 | Transfer learning | Usar un modelo que ya vio millones de imágenes. Fine-tuning de ResNet / MobileNet. Embeddings de CLIP + regresión logística | 2 sem | ⬜ |
| 8 | Evaluación en serio | Overfitting, validación, análisis de errores con negativos difíciles, elección del umbral para moderación en Gridd | 1–2 sem | ⬜ |
| 9 | Deploy | Exportar a ONNX, servir con FastAPI, integrar con Gridd | 1–2 sem | ⬜ |

Ritmo: 5–8 h por semana. Los tiempos son orientativos: si algo no me cierra, me quedo más tiempo ahí.

## Definición de las etiquetas

> ⚠️ PENDIENTE: definir antes del Módulo 4.

- **Positivo seguro:** foto donde aparece un auto o una moto
- **A definir:** flyers de eventos (mucho texto y quizás ningún auto), interiores, motores, llantas sueltas, memes de autos, autos de juguete o maquetas, dibujos
- **Negativos difíciles** (los incluyo a propósito): bicicletas, camiones y buses, garajes o estacionamientos vacíos, rutas sin autos, gente en un estacionamiento, talleres sin vehículos a la vista

## Tarea paralela: dataset (desde el Módulo 3)

- Estructura: `data/raw/positivos/` y `data/raw/negativos/`
- Meta inicial: ~500 imágenes por clase, con al menos un 30 % de negativos difíciles
- Fuentes: fotos propias de car meets, COCO y Open Images (clases *car* y *motorcycle*)
- Si una imagen es ambigua, la anoto en `data/dudosas.md` en lugar de etiquetarla al azar

## GPU

> ⚠️ PENDIENTE: confirmar si tengo GPU NVIDIA local. Si no, desde el Módulo 6 uso Kaggle Notebooks o Google Colab.

## Referencias (para principiantes)

- **Para empezar:** [Kaggle Learn: Python, Pandas, Intro to ML](https://www.kaggle.com/learn) (cursos cortos y gratis); StatQuest (YouTube), que explica cada concepto con dibujos
- **Módulo 1:** [NumPy: absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html), [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html), [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html)
- **Módulos 2–3:** [Andrew Ng: ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction), curso 1; [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- **Módulo 5:** 3Blue1Brown, serie *Neural Networks* (YouTube); [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
- **Módulos 6–7:** [CS231n notes](https://cs231n.github.io/), [fast.ai course](https://course.fast.ai/), [PyTorch: Transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- **Libro (de consulta):** *Hands-On Machine Learning* (Géron)
- **Módulo 9:** [ONNX Runtime](https://onnxruntime.ai/docs/), [FastAPI docs](https://fastapi.tiangolo.com/)
