# Proyecto: Modelo de ML para prediccion de precio en mercado inmobiliario. 


## **Problema**

Valuar las propiedades es un proceso difícil y, a veces, subjetivo. Para ello, proponemos crear un modelo de Machine Learning que, dadas ciertas características de la propiedad habitacional, prediga su precio de venta en USD sobre los barrios de la Ciudad Autónoma de Buenos Aires, Argentina.

En este proyecto vamos a trabajar con un dataset de propiedades en venta publicado en el portal [Properati](www.properati.com.ar).

# **Integrantes**:
  - Mateo Tealdi
  - Pablo Bergolo
  - Pablo Honnorat

# 1. Características a utilizar

### ¿Qué datos nos ayudarían a trabajar en el problema?¿Por qué?

1. Los datos utiles que nos ayudarían a tasar las propiedades prodian ser: 
      - Ubicacion (Separadas en las 15 comunas de CABA)
      - Tipos de propiedad (Separada en 3 categorias unicamente Casas, Departamentos y PHs)
      - Ambientes
      - Habitaciones
      - Baños
      - Superficie del inmueble (superfice construida y superfice disponible)
 
El objetivo de este proyecto es crear un modelo de machine learning que permite facilitar el proceso de valuación de propiedades, es decir el **precio**; con una mirada mas objetiva de la información que se posee de las mismas y no con la subjetividad que se maneja el mercado argentino.

Tanto en cuanto espacio ocupa, en que barrio se ubica y que tipo de inmuebles permiten al consumidor determinar un valor de la propiedad.

Al mismo tiempo estableceremos parámetros base que nos ayudarán a centrar los valores y no tener diferencias que nos desequilibren el modelo.

Estaremos prediciendo entonces:
  - Operaciones de Venta 
  - Expresadas en Dólares (USD)
  - Unicamente en Argentina
  - Sobre los barrios de la Capital Federal. 

## You may also test a working version of the app here: https:// a confirmar .herokuapp.com/