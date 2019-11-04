from emp_reciclagem import Coordenadas
from dicionario import centros, calculoD

print(""" 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 Olá, Por favor informe o tipo de lixo que será reciclado:
 
 1 - Eletrônico
 2 - Papel
 3 - Metal
 4 - Plástico
 5 - Pilhas e baterias
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 
""")

#Checa se a escolha digitada é um numero!
while True:
    try:
        escolha = int(input('Escolha: '))
    except ValueError:
        print("Informe um Numero!!")
        continue
    break

#Checa se a escolha digitada esta entre 1 e 5
while escolha < 1 or escolha > 5:
    print("Numero invalido, Porfavor escolha um numero entre 1 e 5")
    escolha = int(input('Escolha: '))

lat = 0
long = 0

#Checa se o usuário esta informando apenas numeros na latitude e na longitude
while True:
    try:
        lat = float(input('Insira a Latitude: '))
        long = float(input('Insira a Longitude: '))
    except ValueError:
        print("Informe um Numero VALIDO!")
        continue
    else:
        localizacao_usuario = Coordenadas(lat, long)
        break

perto = -1
for reciclar in centros.get(escolha):
    distancia = calculoD(localizacao_usuario, reciclar)
    if distancia < perto or perto == -1:
        perto = distancia
        empresa_perto = reciclar

print(35 * '-')
print(f'Empresa mais proxima: {empresa_perto.nome_emp}')
print(f'Endereço: {empresa_perto.endereco}')
print(f'Telefone: {empresa_perto.telefone}')
print(f'E-mail: {empresa_perto.email}')
print(35 * '-')
