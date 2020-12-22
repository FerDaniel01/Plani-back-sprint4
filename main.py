from fastapi import FastAPI
from fastapi import HTTPException
import egresosdb
import ingresosdb

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [

    "https://planifinanzas-ui-versionfinal.herokuapp.com"

 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/transacciones/")
async def obtener_transacciones():
    transacciones = egresosdb.obtener_Transaciones()
    return transacciones

@app.get("/ingresos/")
async def obtener_ingresos():
    ingresos = ingresosdb.obtener_Ingresos()
    return ingresos

    

@app.post("/transacciones/agregar/")
async  def agregar_transaccion(transaccion:egresosdb.Transaccion):
    agregada_exitosamente=egresosdb.agregar_transaccion(transaccion)
    if agregada_exitosamente:
        return {"mensaje":"Transacción agregada exitosamente"}
    else:
        raise  HTTPException(status_code=400, detail="Error, el id de la transaccion ya existe ")


@app.post("/ingresos/nuevo/")
async def agregar_Ingreso(ingreso:ingresosdb.Ingreso):
    agregado_exitosamente=ingresosdb.agregar_ingreso(ingreso)
    if agregado_exitosamente:
        return{"mensaje": "Ingreso agregado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="Error, el id del ingreso ya exixte ")