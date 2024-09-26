from dataclasses import asdict, astuple, dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    # asdict(cls)transorma a dataclass em dicionario
    # astuple(cls) transorma a dataclass em tupla
    print(asdict(p1).keys()) 
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])