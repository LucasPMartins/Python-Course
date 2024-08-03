# 10 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e 
# métodos que:
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel, valorLitro, quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra 
# a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível
#  e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade 
# de combustível total na bomba.


class BombaCombustivel:
    def __init__(self, tipo: str, valorLitro: float, qtd: float) -> None:
        self.tipo = tipo
        self.valorLitro = valorLitro
        self.qtd = qtd

    def abastecerPorValor(self, valor: float):
        qtd_litros = valor/self.valorLitro
        qtd_resto = self.qtd - qtd_litros
        if qtd_resto < 0:
            self.aviso(qtd_litros,qtd_resto)
        else:
            self.nota_fical(qtd_litros,valor)
        self.mostrarBomba()

    def abastecerPorLitro(self, litro: float):
        valor = litro * self.valorLitro
        qtd_resto = self.qtd - litro
        if qtd_resto < 0:
            self.aviso(litro,qtd_resto)
        else:
            self.nota_fical(litro,valor)
        self.mostrarBomba()

    def nota_fical(self, qtd_litros, valor):
        print('----------=========== NOTA FISCAL ===========----------')
        print(f'O automovel foi abastecido com {qtd_litros:.2f}!')
        print(f'Total a pagar: R${valor:.2f}')
        self.qtd -= qtd_litros
        print('-----------=============#######=============-----------\n')

    def aviso(self,qtd_litros,qtd_resto):
        print('-----------============= AVISO =============-----------')
        print(f'O automovel foi abastecido somente com {self.qtd:.2f}!')
        print(f'Quantidade de combustivel na bomba insuficente para abastecer: '\
              f'{qtd_litros:.2f} litros')
        valor_devolver = -qtd_resto * self.valorLitro
        print(f'Deve-se retornar R${valor_devolver:.2f} para o cliente,')
        print(f'ou o mesmo deve pagar somente R${self.qtd * self.valorLitro:.2f}!')
        self.qtd = 0.0
        print('-----------=============#######=============-----------\n')

    def mostrarBomba(self):
        print(f"A bomba de combustível do tipo {self.tipo} contém {self.qtd} litros!\n\
              Preço por litro: R${self.valorLitro:.2f}")

    def alterarValor(self, valor: float):
        if valor < 0:
            raise ValueError('O preço da bomba deve ser positivo')
        self.valorLitro = valor

    def alterarCombustivel(self, tipo: str):
        if tipo == '' or len(tipo) < 3:
            raise ValueError('O tipo da bomba deve ser um valor valído')
        self.tipo = tipo

    def alterarQuantidadeCombustivel(self, valor: float):
        if valor < 0:
            raise ValueError('A quantidade de combustível da bomba deve ser positivo')
        self.qtd += valor