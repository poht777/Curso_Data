
import os

#ENV = "DEV"
ENV = "PROD"


## server
host = "0.0.0.0"
port = int(os.environ.get("PORT", 5000))
##CSS
fontawesome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"

## info
app_name = "Predicctor del Precio de una Vivienda en CABA"
app_title = "TBH_Data"
contacts = "https://ar.linkedin.com/in/pablohonnorat"
code = "https://github.com/poht777/Curso_Data"
titulo_resultado = "El precio de la vivienda ha sido calculado en: "
about = "Selecciona las opciones para la vivienda y te mostraremos su precio!"
