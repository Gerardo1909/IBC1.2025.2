# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: global
#     language: python
#     name: python3
# ---

# %%
import math
import random
import inspect
import warnings

respuestas = {}

# %% [markdown]
# # 1 - Preguntas sobre fundamentos
#
# Este notebook contiene una lista de preguntas junto con una lista exhaustiva de respuestas mutuamente contradictorias. A diferencia de los enunciados de tipo "multiple choise" en los que se pide seleccionar una única opción, aquí se pide que distribuyan creencias entre las diferentes opciones, asegurándose que el valor asignado sea positivo y la suma sea 1. La evaluación será el producto de las creencias asiganadas a las respuestas correctas. En caso de que la respuesta sea una variable aleatoria, se considerará la predicción típica a largo plazo, es decir, su media gométrica. Notar que un único cero en la secuencia anula todo el producto. Por ello, en caso de duda, no conviene que concentren toda su creencia en una sola opción, sino distribuir algo de creencia en todas las opciones que consideran posibles. Noten también que conviene asignar más a la opción en la que más creen, porque distribuir creencias en partes iguales entre todas las opciones no es mucho mejor que el azar (baseline).

# %% [markdown]
# ### 1.0 Moneda
#
# ¿Cuál será el resultado del lanzamiento de una moneda?
#
# 0. Cara
# 0. Sello

# %%
respuestas[(1,0,"Moneda")] = [
1/2, # 0. Cara
1/2, # 1. Sello
"Justifique brevemente: La probabilidad de que salga cara o sello es la misma, 1/2 para cada una.",
]

# %% [markdown]
# ### 1.1 Cajas
#
# Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. ¿Dónde está el regalo?
#
# 0. Caja 0
# 1. Caja 1
# 2. Caja 2
# 3. Otro lugar

# %%
respuestas[(1,1,"Cajas")] = [
1/3, # 0. Caja 0
1/3, # 1. Caja 1
1/3, # 2. Caja 2
0, # 3. Otro lugar
"Justifique brevemente: La probabilidad de que esté el regalo en una de ellas es la misma, 1/3 para cada una.",
]

# %% [markdown]
# ### 1.2 Mentir
#
# ¿Cuál de todas las opciones se considera una definición matemática del principio de no mentir?
#
# 0. Maxima incertidumbre (entropía)
# 0. Minima incertidumbre (entropía)
# 0. Maxima incertidumbre (entropía) dada la información disponible (restricciones)
# 0. Minima incertidumbre (entropía) dada la información disponible (restricciones)
# 0. Ninguna de las anteriores

# %%
respuestas[(1,2,"Mentir")] = [
0, # 0. Maxima incertidumbre (entropía)
0, # 1. Minima incertidumbre (entropía)
1/4, # 2. Maxima incertidumbre (entropía) dada la información disponible (restricciones)
2/4, # 3. Minima incertidumbre (entropía) dada la información disponible (restricciones)
1/4, # 4. Ninguna de las anteriores
"Justifique brevemente: Pensaría en principio que mínima incertidumbre con la información disponible ya que si tenemos los datos y los ocultamos (fingimos incertidumbre), entonces estaríamos mintiendo.",
]

# %% [markdown]
# ### 1.3 Universos
#
# Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Nos permiten reservar una caja. Luego, una persona elige una de las cajas que no contenga el regalo y no haya sido reservada. Supongamos que reservamos la caja 1. ¿Cuál de todos los universos paralelos va a ocurrir? ¿El regalo está en la caja 1 y nos muestran la caja 1? ¿El regalo está en la caja 1 y nos muestran la caja 2? ... ¿El regalo está en la caja 3 y nos muestran la caja 2? ¿El regalo está en la caja 3 y nos muestran la caja 3?
#
# 0. Regalo = 1, Abren = 1
# 1. Regalo = 1, Abren = 2
# 2. Regalo = 1, Abren = 3
# 3. Regalo = 2, Abren = 1
# 4. Regalo = 2, Abren = 2
# 5. Regalo = 2, Abren = 3
# 6. Regalo = 3, Abren = 1
# 7. Regalo = 3, Abren = 2
# 8. Regalo = 3, Abren = 3
#

# %%
respuestas[(1,3,"Universos")] = [
0, # 0. Regalo = 1, Abren = 1
1/4, # 1. Regalo = 1, Abren = 2
1/4, # 2. Regalo = 1, Abren = 3
0, # 3. Regalo = 2, Abren = 1
0, # 4. Regalo = 2, Abren = 2
1/4, # 5. Regalo = 2, Abren = 3
0, # 6. Regalo = 3, Abren = 1
1/4, # 7. Regalo = 3, Abren = 2
0, # 8. Regalo = 3, Abren = 3
"Justifique brevemente: No se puede abrir la caja que se reservó, eso quita todos los casos en donde se abre la caja 1, además también hay que quitar los casos en donde se abre la caja que tiene el regalo ya que esas no se abren. Dejándonos con 4 casos de igual probabilidad."
]
# %% [markdown]
# ### 1.4 Razonamiento
#
# Desde su descubierto, las reglas de la probabilidad han sido adoptadas como sistema de razonamiento en todas las ciencias con datos desde la física hasta las ciencias sociales. En los últimos años se ha producido enormes avances en el área de las ciencia de datos, el aprendizaje automático y la inteligencia artificial. ¿Cuándo se comenzó a usar por primer vez el actual sistema de razonamiento para contextos de incertidumbre?
#
# 0. Antes del siglo 17
# 1. Siglo 17
# 2. Siglo 18
# 3. Siglo 19
# 4. Siglo 20
# 5. Siglo 21
#
#
#

# %%
respuestas[(1,4,"Razonamiento")] = [
1/3, # 0. Antes del siglo 17
2/3, # 1. Siglo 17
0, # 2. Siglo 18
0, # 3. Siglo 19
0, # 4. Siglo 20
0, # 5. Siglo 21
"Justifique brevemente: Al ser descubiertas en el siglo 17, se podría afirmar que se empezó a utilizar desde ese momento.",
]

# %% [markdown]
# ### 1.5 Independencia
#
# Si P(A) = 0.4, P(B) = 0.5, y A y B son eventos independientes, ¿cuál es la probabilidad conjunta de P(A, B)?
#
# 0. 0.9
# 1. 0.1
# 2. 0.0
# 3. 0.2
# 4. Ninguna de las anteriores

# %%
respuestas[(1,5,"Independencia")] = [
0, # 0. 0.9
0, # 1. 0.1
0, # 2. 0.0
1, # 3. 0.2
0, # 4. Ninguna de las anteriores
"Justificar brevemente: La probabilidad conjunta de eventos independientes es el producto de las probabilidades individuales de ambos eventos.",
]

# %% [markdown]
# ### 1.6 Marginal
#
# Sean dos variables binarias, X e Y, con las siguientes probabilidades conjuntas, P(X=0, Y=0) = 0.1, P(X=1, Y=0) = 0.2, P(X=0, Y=1) = 0.3, P(X=1, Y=1) = 0.4 ¿Cuál es la probabilidad de P(Y = 1)?
#
#
# 1. P(Y=1): 0.10
# 1. P(Y=1): 0.15
# 1. P(Y=1): 0.20
# 1. P(Y=1): 0.25
# 1. P(Y=1): 0.30
# 1. P(Y=1): 0.35
# 1. P(Y=1): 0.40
# 1. P(Y=1): 0.45
# 1. P(Y=1): 0.50
# 1. P(Y=1): 0.55
# 1. P(Y=1): 0.60
# 1. P(Y=1): 0.65
# 1. P(Y=1): 0.70
# 1. P(Y=1): 0.75
# 1. P(Y=1): 0.80
# 1. P(Y=1): 0.85
# 1. P(Y=1): 0.90
# 1. Ninguna de las anteriores

# %%
respuestas[(1,6,"Marginal")] = [
0, # 0. P(Y=1): 0.10
0, # 1. P(Y=1): 0.15
0, # 2. P(Y=1): 0.20
0, # 3. P(Y=1): 0.25
0, # 4. P(Y=1): 0.30
0, # 5. P(Y=1): 0.35
0, # 6. P(Y=1): 0.40
0, # 7. P(Y=1): 0.45
0, # 8. P(Y=1): 0.50
0, # 9. P(Y=1): 0.55
0, # 10. P(Y=1): 0.60
0, # 11. P(Y=1): 0.65
1, # 12. P(Y=1): 0.70
0, # 13. P(Y=1): 0.75
0, # 14. P(Y=1): 0.80
0, # 15. P(Y=1): 0.85
0, # 16. P(Y=1): 0.90
0, # 17. Ninguna de las anteriores
"Justifique brevemente: La probabilidad marginal de Y=1 es la suma de las probabilidades conjuntas de todos los eventos donde Y=1.",
]


# %% [markdown]
# ### 1.7 Condicional
#
# Sean dos variables binarias, X e Y, con las siguientes probabilidades conjuntas, P(X=0, Y=0) = 0.1, P(X=1, Y=0) = 0.2, P(X=0, Y=1) = 0.3, P(X=1, Y=1) = 0.4 ¿Cuál es la probabilidad de P(Y = 1|X = 1)?
#
#
# 1. P(Y=1|X=1): 1/2
# 1. P(Y=1|X=1): 1/3
# 1. P(Y=1|X=1): 2/3
# 1. P(Y=1|X=1): 1/4
# 1. P(Y=1|X=1): 2/4
# 1. P(Y=1|X=1): 3/4
# 1. P(Y=1|X=1): 1/5
# 1. P(Y=1|X=1): 2/5
# 1. P(Y=1|X=1): 3/5
# 1. P(Y=1|X=1): 4/5
# 1. P(Y=1|X=1): 1/6
# 1. P(Y=1|X=1): 2/6
# 1. P(Y=1|X=1): 3/6
# 1. P(Y=1|X=1): 4/6
# 1. P(Y=1|X=1): 5/6
# 1. Ninguna de las anteriores


# %%
respuestas[(1,7,"Condicional")] = [
0, # 0. P(Y=1|X=1): 1/2
0, # 1. P(Y=1|X=1): 1/3
1, # 2. P(Y=1|X=1): 2/3
0, # 3. P(Y=1|X=1): 1/4
0, # 4. P(Y=1|X=1): 2/4
0, # 5. P(Y=1|X=1): 3/4
0, # 6. P(Y=1|X=1): 1/5
0, # 7. P(Y=1|X=1): 2/5
0, # 8. P(Y=1|X=1): 3/5
0, # 9. P(Y=1|X=1): 4/5
0, # 10. P(Y=1|X=1): 1/6
0, # 11. P(Y=1|X=1): 2/6
0, # 12. P(Y=1|X=1): 3/6
0, # 13. P(Y=1|X=1): 4/6
0, # 14. P(Y=1|X=1): 5/6
0, # 15. Ninguna de las anteriores
"Justifique brevemente: Definición de probabilidad condicional en donde, P(Y = 1|X = 1) = P(X=1, Y=1)/P(X=1).",
]


# %% [markdown]
# ### 1.8 Overfitting
#
# En el área de aprendizaje automático e inteligencia artificial se ha descubierto un problema que se conoce con el nombre de overfitting. ¿El overfitting es/era un problema propio del sistema de razonamiento para contextos de incertidumbre?
#
# 0. No
# 1. Sí


# %%
respuestas[(1,8,"Overfitting")] = [
9/10, # 0. No
1/10, # 1. Si
"",
]

# %% [markdown]
# ### 1.9 Evaluación
#
# En el área de aprendizaje automático e inteligencia artificial existe una gran cantidad de métricas distintas para evaluar los modelos alternativos. ¿En principio, existe una forma correcta, universal, de evaluar los modelos? 
#
# 0. NO
# 1. Sí

# %%
respuestas[(1,9,"Evaluación")] = [
1, # 0. No
0, # 1. Si
"Justifique brevemente: No existe una única forma, un ejemplo es que una métrica para evaluar la regresión no es aplicable a la clasificación.",
]

# %% [markdown]
# ### 1.10 Predicción
#
# Históricamente todas las ciencias con datos, desde la física hasta las ciencias sociales, explicaron el mundo a través de teorías causales. Los recientes avances en el área de aprendizaje automático e inteligencia artificial, sin embargo, se produjeron por el desarrollo de algoritmos altamente predictivos sin ninguna interpretación causal. ¿Por qué?
#
# 0. El modelo causal correcto nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
# 1. El modelo causal correcto a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
# 2. El modelo causal correcto nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
# 3. Los modelos causales solo explican, no predicen.
# 4. Ninguna de las anteriores

# %%
respuestas[(1,10,"Predicción")] = [
0, # 0. El modelo causal correcto nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
3/5, # 1. El modelo causal correcto a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
1/5, # 2. El modelo causal correcto nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
0, # 3. Los modelos causales solo explican, no predicen.
1/5, # 4. Ninguna de las anteriores
"Justifique brevemente: El modelo causal correcto puede ser mejor o peor que los complejos algoritmos de AI/ML dependiendo del contexto y la naturaleza de los datos.",
]

# %% [markdown]
# ### 1.11 Diversificación
#
# Una casa de apuestas 3 a Cara y 1.2 a Sello por el lanzamiento de monedas normales con 0.5 de probabilidad de que salga Cara o Sello. Supongamos que nos ofrecen jugar 1000 veces, apostando todos nuestros recursos en cada paso temporal. ¿Qué proporción apostaría a Cara? Notar que el resto se asigna a Sello. Notar además que si apostamos todo a Cara y sale Sello perdemos todos los recursos y no podemos volver a jugar.
#
# 0. Recursos asignados a Cara: 0.0
# 1. Recursos asignados a Cara: 0.1
# 2. Recursos asignados a Cara: 0.2    
# 3. Recursos asignados a Cara: 0.3
# 4. Recursos asignados a Cara: 0.4
# 5. Recursos asignados a Cara: 0.5
# 6. Recursos asignados a Cara: 0.6
# 7. Recursos asignados a Cara: 0.7
# 8. Recursos asignados a Cara: 0.8
# 9. Recursos asignados a Cara: 0.9
# 10. Recursos asignados a Cara: 1.0

# %%
respuestas[(1,11,"Diversificación")] = [
0, # 0. Recursos asignados a Cara: 0.0
0, # 1. Recursos asignados a Cara: 0.1
0, # 2. Recursos asignados a Cara: 0.2
1/5, # 3. Recursos asignados a Cara: 0.3
1/5, # 4. Recursos asignados a Cara: 0.4
1/5, # 5. Recursos asignados a Cara: 0.5
1/5, # 6. Recursos asignados a Cara: 0.6
1/5, # 7. Recursos asignados a Cara: 0.7
0, # 8. Recursos asignados a Cara: 0.8
0, # 9. Recursos asignados a Cara: 0.9
0, # 10. Recursos asignados a Cara: 1.0
"Justifique brevemente: Si apostamos todo a algunas de las caras y estas en algún turno no salen (que va a pasar) entonces perdemos todo. Eso descarta el 0 y el 1 y nos quedarían los valores medios, que para asegurar que si perdemos no sea tan grave prefiero que estén entre 0.3 y 0.7 para no considerar extremos.",
]

# %% [markdown]
# ### 1.12 Apuesta individual
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello. Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello. Notar que la esperanza (media aritmética) es positiva (1,05). ¿Nos conviene jugar?
#
# 0. NO
# 1. Sí

# %%
respuestas[(1,12,"Apuesta individual")] = [
1/3, # 0. No
2/3, # 1. Sí
"Justifique brevemente: Si la esperanza es positiva (1,05) entonces a las 1000 tiradas habríamos tenido un rendimiento positivo.",
]

# %% [markdown]
# ### 1.13 Fondo común
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello. Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello. A diferencia del caso anterior, aquí nos vemos en la obligación en cada paso temporal junto con otras 100 personas a dividir todos nuestros recursos en partes iguales. Es decir, en cada paso temporal cada persona tira la su propia moneda, actualiza sus propios recursos individuales, los pone en el fondo común, se dividen en partes iguales y volvemos a empezar. ¿Este simple hecho, mejora o empeora nuestra tasa de crecimiento de nuestros recursos?
#
# 0. Empeora
# 1. Neutro
# 2. Mejora


# %%
respuestas[(1,13,"Fondo común")] = [
1/5, # 0. Empeora
3/5, # 1. Neutro
1/5, # 1. Mejora
"Justifique brevemente: En principio pensaría que es más neutro dado que no sufriríamos una gran pérdida ya que se promediaría con el resto pero a su vez si obtenemos una gran ganancia esto también se promediaría de la misma forma. Además hay que considerar que no se aclara en el enunciado si todos parten con 'todos los recursos' iguales o similares.",
]

# %% [markdown]
# ### 1.14 Tragedia de los comunes
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello. Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello. Supongamos que para nuestras apuestas contamos con el apoyo de otras 100 personas que están aportando en cada paso temporal a un fondo que se divide en partes iguales. ¿Nos conviene aportar al fondo común o nos conviene dejar de aportar y seguir recibiendo la cuota del fondo común?
#
# 0. Nos conviene aportar al fondo común
# 1. Es indistinto
# 2. Nos conviene dejar de aportar mientras seguimos recibiendo la cuota del fondo común


# %%
respuestas[(1,14,"Tragedia de los comunes")] = [
1/4, # 0. Nos conviene aportar al fondo común
1/4, # 1. Es indistinto
2/4, # 1. Nos conviene dejar de aportar mientras seguimos recibiendo la cuota del fondo común
"Justifique brevemente: Si dejamos de aportar seguiriamos recibiendo la cuota, así que parece ser la mejor opción.",
]


