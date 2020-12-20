from pydantic import BaseModel


class Ingreso(BaseModel):
    id: int
    fechaNuevoIngreso:str
    tipoIngreso: str
    valor: float
    entidadPagadora:str
    descripcion: str




ingresos = {
    1: Ingreso (id=1 , fechaNuevoIngreso = "20-11-2020", tipoIngreso="Venta Ganado",valor=1000000, entidadPagadora="AsoGanaderos", descripcion= "lote de ganado"),
    2: Ingreso (id=2 , fechaNuevoIngreso = "22-11-2020", tipoIngreso="Sueldo",valor=1980000, entidadPagadora="ACV", descripcion= "Sunrise Dry Doc"),
    3: Ingreso (id=3 , fechaNuevoIngreso = "01-12-2020", tipoIngreso="Venta APP",valor=6000000, entidadPagadora="Google", descripcion= "Aplicacion nueva")



}



def obtener_Ingresos():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_ingresos=[]

    for e in ingresos:
        lista_ingresos.append(ingresos[e])
    return lista_ingresos




def agregar_ingreso(ingreso: Ingreso):
    if ingreso.id in ingresos:
        return False
    else:
        ingresos[ingreso.id]= ingreso
        return True