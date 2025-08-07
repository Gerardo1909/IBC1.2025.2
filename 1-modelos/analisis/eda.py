#!/usr/bin/env python
# coding: utf-8

# # EDA - NoMontyHall

# ## Carga inicial

# In[18]:


import pandas as pd 
import matplotlib.pyplot as plt
import os 


# In[19]:


ruta_no_monty = os.path.join('..', 'data', 'NoMontyHall.csv')


no_monty_df = pd.read_csv(ruta_no_monty)

no_monty_df.head()


# In[20]:


no_monty_df.info()


# Convierto a categorias dados los valores que toman las variables:

# In[21]:


for column in no_monty_df.columns:
    if no_monty_df[column].dtype != 'object':
        no_monty_df[column] = no_monty_df[column].astype('category')


# Cambio los nombres de las columnas para hacer más amigable a la vista el análisis exploratorio:

# In[22]:


no_monty_df.rename(columns={
    'c' : 'CajaElegida',
    's' : 'CajaAbierta',
    'r' : 'CajaRegalo'
}, inplace=True)


# ## Análisis exploratorio

# In[23]:


no_monty_df.describe()


# Obtengo proporciones de interés:

# In[24]:


coincide_abierta_regalo = no_monty_df[no_monty_df.CajaAbierta == no_monty_df.CajaRegalo].shape[0] / no_monty_df.shape[0]
coincide_elegida_regalo = no_monty_df[no_monty_df.CajaElegida == no_monty_df.CajaRegalo].shape[0] / no_monty_df.shape[0]
coincide_elegida_abierta = no_monty_df[no_monty_df.CajaElegida == no_monty_df.CajaAbierta].shape[0] / no_monty_df.shape[0]


# Armo gráfico:

# In[27]:


plt.figure(figsize=(10, 6))
plt.bar(['CajaAbierta = CajaRegalo', 'CajaElegida = CajaRegalo', 'CajaElegida = CajaAbierta'], 
        [coincide_abierta_regalo, coincide_elegida_regalo, coincide_elegida_abierta], 
        color=['blue', 'orange', 'green'])
plt.tight_layout()
plt.show()


# **Este gráfico nos deja ver algo bastante interesante**: el presentador solo abre la caja de nosotros cuando sabe que esa no tiene regalo.
# 
# Se puede verificar mirando a detalle los casos en donde la caja elegida y la abierta coinciden:

# In[26]:


no_monty_df[no_monty_df.CajaElegida == no_monty_df.CajaAbierta]


# ## Interpretación y proposición de modelo causal

# Entonces sabemos que no es Monty Hall ya que puede abrir la caja que elegimos, **pero eso solo va a pasar si la caja no tiene el regalo**. Esto nos dejaría
# con dos posibles escenarios:
# 
# 1. Si abre la caja que elegimos, entonces las otras dos tienen igual probabilidad de contener el regalo.
# 
# 2. Si NO abre la caja que elegimos, **fue por algo** y entonces nuestra caja tiene más probabilidad de ser la que contenga el regalo.
# 
# En Monty Hall ocurría que si nosotros cambiabamos de puerta doblábamos la chance de abrirla y ver el auto, esto porque el presentador
# no podía abrir la puerta que eligió el participante ni la puerta en donde estaba el auto, logrando así que la otra puerta aumentara
# sus posibilidades **porque por alguna razón el presentador no la eligió**.
# 
# Podemos pensarlo como que la puerta distinta a la que el particpante elige tuvo la oportunidad de "someterse a prueba" pero el presentador
# no hizo tal cosa y terminó eligiendo la puerta en donde seguro estaba la cabra. Ahí el porque se dobla la probabilidad.

# ### Posible modelo causal

# En base a lo que planteaba antes para este caso donde no hay Monty Hall, pensé en el siguiente modelo causal:
# 
# ```mermaid
# flowchart TD
#     A[Ubicación regalo] --> B(Caja Abierta)
#     C[Caja elegida] 
# ```
# 
# Notar que no se toma en cuenta a la caja elegida, el presentador solo debe considerar la caja en donde está el regalo.
