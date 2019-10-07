
class EmpresaReciclagem():
    def __init__(self, lat, lon, nome_emp, endereco, telefone, email):
        self.lat = lat
        self.lon = lon
        self.nome_emp = nome_emp
        self.endereco = endereco
        self.telefone = telefone
        self.email = email


class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
