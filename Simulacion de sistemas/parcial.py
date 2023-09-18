import random,statistics,math
def intConf(muestra):
  mediaMuestra = statistics.mean(muestra)
  desviacionMuestra = statistics.stdev(muestra)
  precision = 1.96*(desviacionMuestra/math.sqrt(len(muestra)))
  res = [mediaMuestra, desviacionMuestra, (mediaMuestra-precision, mediaMuestra+precision)]
  return res

def Tipodia():
    r = random.random()
    tipoDeDia = ["Bueno","Regular","Malo"]
    acumuladaDia = [0.35,0.73,1]
    for i in range(len(tipoDeDia)):
        if r <= acumuladaDia[i]:
            return tipoDeDia[i]
        
def demandaDia():
    cantidadDemandada = [40,50,60,70,80,90,100]
    probabilidadBueno = [0,0.05,0.19,0.4,0.75,0.93,1]
    probabilidadRegular = [0.1,0.28,0.68,0.88,0.96,1,0]
    probabilidadMalo = [0.44,0.67,0.86,0.98,1,0,0]
    dia = Tipodia()
    if dia == "Bueno":
        for i in range(len(cantidadDemandada)):
            r = random.random()
            if r <= probabilidadBueno[i]:
                return cantidadDemandada[i]
    if dia == "Regular":
        for i in range(len(cantidadDemandada)):
            r = random.random()
            if r <= probabilidadRegular[i]:
                return cantidadDemandada[i]
    if dia == "Malo":
        for i in range(len(cantidadDemandada)):
            r = random.random()
            if r <= probabilidadMalo[i]:
                return cantidadDemandada[i]

def GananciastortasDia(tortasCompradas):
    tortaUnidad = 23
    precioVenta = 40
    salvamento  = 4
    indemizacion= 10
    tortasDemandaDia = demandaDia()
    gastos = tortasCompradas*tortaUnidad
    ganancias = 0
    if(tortasCompradas>=tortasDemandaDia):
        sobrantes  =tortasCompradas-tortasDemandaDia
        ganancias +=tortasDemandaDia*precioVenta
        ganancias += sobrantes*salvamento
    else:
        faltantes  =tortasDemandaDia-tortasCompradas
        ganancias +=tortasCompradas*precioVenta
        gastos    +=faltantes*indemizacion
    utilidades = ganancias-gastos
    return utilidades,tortasDemandaDia

promedioPorUnidad = []
sdPorUnidad = []
tortas = []
for i in range(40,101):
    general = []
    for j in range(1000):
        valor = GananciastortasDia(i)
        general.append(valor[0])
    data = intConf(general)
    tortas.append(i)
    promedioPorUnidad.append(data[0])
    sdPorUnidad.append(data[1])
print("tortas[i]  promedioPorUnidad[i]")

# for i in range(len(tortas)):
#     print(f"{tortas[i]}         {promedioPorUnidad[i]}")
tortasDemanda=[]
promedioPorUnidadDemanda = []
intPorUnidadDemanda = []
for j in range(1000):
    valor = GananciastortasDia(i)
    tortasDemanda.append(valor[1])
data2 = intConf(tortasDemanda)
promedioPorUnidadDemanda = data2[0]
intPorUnidadDemanda = data2[2]
print(f"({intPorUnidadDemanda[0]}, {intPorUnidadDemanda[1]})")