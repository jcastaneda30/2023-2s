fila = []
 
while True:
  listicaTemporal = input().split()
  fan = listicaTemporal[0]
  preferencia = int(listicaTemporal[1])
 
  if fan == "0" and preferencia ==0:
    break
  if preferencia > len(fila):
    fila.append(preferencia)
 
  elif len(fila) == 0:
    fila.append(preferencia)
 
largoOG = len(fila)
 
for i in range(1,len(fila)):
  if fila[-i] < largoOG:
    largoOG-=1
    break
 
print(largoOG)