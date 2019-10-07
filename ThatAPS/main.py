from emp_reciclagem import Coordenadas
from dicionario import centros,calculoD

print(""" 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 Olá, Porfavor informe o time de lixo que será reciclado:
 
 1 - Eletrônico
 2 - Papel
 3 - Metal
 4 - Plástico
 5 - Pilhas e baterias
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 
""")
escolha = int(input('Escolha: '))

while( escolha < 1 or escolha > 5):
    print("Numero invalido, Porfavor escolha um numero entre 1 e 5")
    escolha = int(input('Escolha: '))

localizacao_usuario = Coordenadas(-22.927063, -47.042617) #PENSAR EM ALGUMA FORMA DE PEDIR A LOCALIZAÇÃO PRO USUÁRIO

perto = -1
for reciclar in centros.get(escolha):
    distancia = calculoD(localizacao_usuario, reciclar)
    if distancia < perto or perto == -1:
        perto = distancia
        empresa_perto = reciclar

print(f'A empresa mais perto é {empresa_perto.nome_emp}')


















