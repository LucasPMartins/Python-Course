# Método especial __call__
# callable é algo que pode ser excutadp com parênteses
# Em classes normais , __call__ faz a instância de uma
# classe 'callable'


class CallMe:
    def __init__(self, nome) -> None:
        self.nome = nome

    def __call__(self, *args, **kwds) -> int:
        print(args, 'está chamando', self.nome)
        return 123


call1 = CallMe('23123123123')
retorno = call1(1, 2, 3, 4)
print(retorno)
