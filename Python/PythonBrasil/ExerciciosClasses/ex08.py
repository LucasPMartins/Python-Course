# 8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho 
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa 
# ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo 
# menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.bucho:list[str] = []

    def comer(self, alimento) -> None:
        self.bucho.append(alimento)

    def ver_bucho(self) -> None:
        if self.bucho:
            print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")
        else:
            print(f"O bucho de {self.nome} está vazio.")

    def digerir(self) -> None:
        if self.bucho:
            print(f"{self.nome} digeriu: {self.bucho.pop(0)}")
        else:
            print(f"{self.nome} não tem nada no bucho para digerir.")

# Programa de teste
def main():
    # Criação de dois macacos
    macaco1 = Macaco("Macaco1")
    macaco2 = Macaco("Macaco2")
    
    # Alimentando os macacos com 3 alimentos diferentes
    macaco1.comer("Banana")
    macaco1.ver_bucho()
    macaco1.comer("Maçã")
    macaco1.ver_bucho()
    macaco1.comer("Laranja")
    macaco1.ver_bucho()
    
    macaco2.comer("Melancia")
    macaco2.ver_bucho()
    macaco2.comer("Abacaxi")
    macaco2.ver_bucho()
    macaco2.comer("Manga")
    macaco2.ver_bucho()
    
    # Digerindo alimentos
    macaco1.digerir()
    macaco1.ver_bucho()
    
    macaco2.digerir()
    macaco2.ver_bucho()
    
    # Macaco1 come Macaco2
    macaco1.comer("Macaco2")
    macaco1.ver_bucho()

if __name__ == "__main__":
    main()