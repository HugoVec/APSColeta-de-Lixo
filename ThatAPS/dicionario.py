from math import asin, cos, pi, sin
from emp_reciclagem import EmpresaReciclagem

centros = {
    ## Lixo eletrônico
    1: [
        EmpresaReciclagem(-22.926866, -47.042982, 'Reversis - Reciclagem de Eletrônicos e Informática', 'Rua da Abolição, 1900 - Ponte Preta', '(19) 2511-6452', 'contato@reversis.com.br'),
        EmpresaReciclagem(-22.853557, -47.098641,'Eco vallore', 'R. Francisco Ceará Barbosa, 1091 - Campinas-SP', ' (19) 97172-5207', 'contato@ecovallore.com.br')
    ],

    ## Papel
    2: [
        EmpresaReciclagem(-22.934040, -47.105668, 'HT Papéis Barão - Coleta e reciclagem de resíduos', 'Av. Ruy Rodrigues, 394 - Jardim Novo Campos Eliseos', '(19) 3227-6830', 'atendimento@papeisbarao.com.br'),
        EmpresaReciclagem(-22.823907, -47.082995, 'Eco Ponto Barão Geraldo', 'Av. Santa Isabel, s/nº', '(19) 2116-0555', 'sac@campinas.sp.gov.br'),
    ],

    ## Metal
    3: [
        EmpresaReciclagem(-22.823907, -47.082995, 'Eco Ponto Barão Geraldo', 'Av. Santa Isabel, s/nº', '(19) 2116-0555', 'sac@campinas.sp.gov.br'),
        EmpresaReciclagem(-22.904581, -47.105445, 'Ecoponto Jardim Pacaembu','R. Dante Suriani, 2-382 - Chácara Cneo','(19) 2116-0555','sac@campinas.sp.gov.br'),
    ],

    ## Plástico
    4: [
        EmpresaReciclagem(-22.964434, -47.125034, 'CBJ Reciclagem de Plásticos Campinas', 'R. Itaóca, Jardim Aeroporto de Viracopos, Campinas - SP', '562', 'contato@cbjreciclagem.com.br'), 
        EmpresaReciclagem(-22.823907, -47.082995, 'Eco Ponto Barão Geraldo', 'Av. Santa Isabel, s/nº', '(19) 2116-0555', 'sac@campinas.sp.gov.br'),
        EmpresaReciclagem(-22.908946, -47.066973, 'Eco Ponto Região Central', 'Rua Francisco Theodoro, 1050, Vila Industrial', '(19) 2116-0555', 'sac@campinas.sp.gov.br'),
        EmpresaReciclagem(-22.936058, -47.118042, 'Ecoponto Vila União','R. Manoel Gomes Ferreira, 42 - Parque Tropical','(19) 2116-0555','sac@campinas.sp.gov.br'),


    ],

    ## Pilhas e baterias
    5: [
        EmpresaReciclagem(-22.898182, -47.093474, 'GMV Recycle', 'Rod. Lix da Cunha, 911 - Jardim Nova America', '(19) 3229-8138', 'certificado2@gmvrecycle.com.br'),
    ]

}


def calculoD(pontoA, pontoB):

    #Distancia entre os pontos
    #PontoA são as Coordenadas do Usuário
    #PontoB são as Coordenandas da Empresa de Recilcagem


    def _hav(x):
        return sin(x / 2) ** 2

    raio_terrestre = 6367.5
    ## Diferença, em radianos, entre as latitudes
    delta_lat = (pontoB.lat - pontoA.lat) * pi / 180

    ## Diferença, em radianos, entre as longitudes
    delta_lon = (pontoB.lon - pontoA.lon) * pi / 180

    ## Calcula, em km, a distancia entre os pontos
    return 2 * raio_terrestre * asin((_hav(delta_lat) + cos(pontoA.lat) * cos(pontoB.lat) * _hav(delta_lon)) ** 0.5)

