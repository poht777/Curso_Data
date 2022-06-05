import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import xgboost

class Model():

    def __init__(self):
        ###Al crear el modelo, le cargo el archivo con el modelo entrenado
        self.modeloPred = xgboost.XGBRegressor() # init model

    #ejecucion del modelo
    def run(self, tipo, ubicacion, baños, habitaciones, ambientes, supcubierta, suptotal):
        ###Almaceno los datos recibidos
        datos_env = [ambientes, habitaciones, baños, suptotal, supcubierta, float(tipo), float(ubicacion)]
        
        ###Cargo el modelo entrenado
        self.modeloPred.load_model('~/python/House_price_predicction.bin') # load data
        
        ###Ejecuto el modelo, debo pasarle los datos como lista! por eso los corchetes sobre la variable
        best_price = self.modeloPred.predict([datos_env])
        
        ###Devuelvo el precio
        output = round(best_price[0], 3) #reverting transformations applied 
        if output<= 0:
            return ["Lo sentimos, el precio de esta vivienda no pudo ser estimado"]
        else:
            return [str(output) + " USD"]