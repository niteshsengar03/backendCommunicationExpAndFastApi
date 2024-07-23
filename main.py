from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
with open('pvout_output_ridge_model.pkl', 'rb') as file: 
    model = pickle.load(file)
with open('pvout_output_ridge_model.pkl', 'rb') as file:
    model_pvout=pickle.load(file)
with open('dif_output_ridge_model.pkl', 'rb') as file:
    model_dif=pickle.load(file)
with open('dni_output_ridge_model.pkl', 'rb') as file:
    model_dni=pickle.load(file)
with open('ghi_output_ridge_model.pkl', 'rb') as file:
    model_ghi=pickle.load(file)
with open('gti_output_ridge_model.pkl', 'rb') as file:
    model_gti=pickle.load(file)
with open('temp_output_ridge_model.pkl', 'rb') as file:
    model_temp=pickle.load(file)
with open('opta_output_ridge_model.pkl', 'rb') as file:
    model_opta=pickle.load(file)

app = FastAPI()

class Item(BaseModel):
    x: int
    y: int

@app.post("/sum")
async def calculate_sum(item: Item):
    x= item.x
    y = item.y
    l=[(x,y)]
    df = pd.DataFrame(l,columns=['x','y'])
    df_opta=df.copy()
    df1=df.copy()
    df1['opta']=model_opta.predict(df_opta)
    df['dif']=model_dif.predict(df1)
    df['ghi']=model_ghi.predict(df1)
    df['gti']=model_gti.predict(df1)
    df['dni']=model_dni.predict(df1)
    df['temp']=model_temp.predict(df1)
    df['opta']=model_opta.predict(df_opta)
    pvout=model_pvout.predict(df)
    print(pvout)
    prediction = pvout
    prediction_list = prediction.tolist()  # Assuming prediction is a numpy array
    return {"prediction": prediction_list}
    # prediction = model.predict(df)
    # return {"prediction": prediction}
   