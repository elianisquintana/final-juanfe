#COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd

#2. traer los datos
from data.simulador import generar_ventas

#3. convertir los datos en un DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())

#4. aplciar los filtros (5)
#print(dataFrame)

#yo como administrador de la tienda quiero abtener las ventas de enero  de viviana agudelo
filtroUno=dataFrame.query("vendedor=='Viviana Agudelo'")
#print(filtroUno)

#yo como administrador de la tienda quiero ver ventas con mas de tres productos
filtroDos=dataFrame.query("cantidad >=3")
#print(filtroDos)

#yo como administrador de la tienda quiero ver ventas con valores de mas de 900 mil pesos
filtroTres=dataFrame.query("total>900000")
#print(filtroTres)

#yo como administrador de la tienda quiero ver las ventas de las camisetas polo
filtroCuatro=dataFrame.query("producto=='camiseta POLO'")
#print(filtroCuatro)

#yo como administrador de la tienda quiero ver las ventas de los productos que menos se venden
filtroCinco=dataFrame.query("cantidad <=1")
print(filtroCinco)