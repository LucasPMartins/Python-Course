# 6 - Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o 
# volume. Certifique-se de que o número do canal e o nível do volume permanecem 
# dentro de faixas válidas.

class TV:
    def __init__(self, canal:int = 1,volume: int = 5) -> None:
        self._canal = canal
        self.volume = volume
    
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    @property
    def canal(self):
        return self._canal
    @canal.setter
    def canal(self,canal):
        if 0 < canal < 250:
            self._canal = canal

if __name__ == '__main__':
    tv = TV(1,1)
    tv.aumentarVolume()
    print('volume:',tv.volume)
    tv.aumentarVolume()
    tv.aumentarVolume()
    tv.aumentarVolume()
    tv.aumentarVolume()
    tv.aumentarVolume()
    tv.aumentarVolume()
    tv.aumentarVolume()
    print('volume:',tv.volume)
    tv.diminuirVolume()
    tv.diminuirVolume()
    tv.diminuirVolume()
    print('volume:',tv.volume)
    tv.canal = 12
    print('Canal:',tv.canal)