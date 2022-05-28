import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBRegressor

class Model():

    def __init__(self):
        ###Al crear el modelo, le cargo los datos necesarios
        datos = pd.read_csv('/wd/python/properati_filtrado.csv')
        self.datos = pd.DataFrame(data = datos)

    @staticmethod
    def evaluate(self, dat_predict): 
        ###Guardo las variables
        DF = self.datos
        modelo = XGBRegressor()

        # Separación de la variable target del dataset
        X = DF.drop('price',axis=1)
        Y = DF.price   #Target

        # Se normalizan los valores de las variables bajo análisis
        sc = StandardScaler()
        X_sc = sc.fit_transform(X)

        ###Entrenamiento
        modelo.fit(X_sc,Y)

        ### Prediccion
        price = modelo.predict(dat_predict)
        
        #debe devolver el precio
        return price

    #ejecucion del modelo
    def run(self, tipo, ubicacion, baños, habitaciones, ambientes, supcubierta, suptotal):
        ###Almaceno los datos recibidos
        datos_env = [ambientes, habitaciones, baños, suptotal, supcubierta, float(tipo), float(ubicacion)]
        ###Ejecuto el modelo, debo pasarle los datos como lista! por eso los corchetes sobre la variable
        best_price = self.evaluate(self, [datos_env])
        
        ###Devuelvo el precio
        output = round(best_price[0], 3) #reverting transformations applied 
        if output<= 0:
            return ["Lo sentimos, el precio de esta vivienda no pudo ser estimado"]
        else:
            return [str(output) + " USD"]

