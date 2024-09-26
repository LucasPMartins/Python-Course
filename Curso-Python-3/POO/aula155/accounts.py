from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, number: int, balance: float = 0.0) -> None:
        self.agency = agency
        self.number = number
        self.balance = balance

    @abstractmethod
    def withdraw(self, valor: float) -> float: ...

    def deposit(self, valor: float) -> float:
        self.balance += valor
        self.details(f'(DEPÓSITO DE R${valor:.2f})')
        return self.balance

    def details(self, msg='') -> None:
        print(f'O seu saldo é R${self.balance:.2f} {msg}')
        print('----===========##############==========----')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.number!r}, {self.balance!r})'
        return f'{class_name} {attrs}'


class AccountCurrent(Account):
    def __init__(self, agency: int, number: int, balance: float = 0.0, limite: float = 0.0) -> None:
        super().__init__(agency, number, balance)
        self.limite = limite

    def withdraw(self, valor: float) -> float:
        valor_pos_saque = self.balance - valor
        limite_max = -self.limite
        if valor_pos_saque >= limite_max:
            self.balance -= valor
            self.details(f'(SAQUE R${valor:.2f})')
        print('Não foi possível realizar a operação de saque!')
        print(f'Seu limite é R${-self.limite:.2f}')
        self.details(f'(SAQUE NEGADO DE R${valor:.2f})')
        return self.balance
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.number!r}, '\
                f'{self.balance!r}, {self.limite!r})'
        return f'{class_name} {attrs}'


class AccountSaving(Account):
    def __init__(self, agency, number, balance=0) -> None:
        super().__init__(agency, number, balance)

    def withdraw(self, valor: float) -> float:
        valor_pos_saque = self.balance - valor
        if valor_pos_saque >= 0:
            self.balance -= valor
            self.details(f'(SAQUE R${valor:.2f})')
        print('Não foi possível realizar a operação de saque!')
        self.details(f'(SAQUE NEGADO DE R${valor:.2f})')
        return self.balance


if __name__ == '__main__':
    cp1 = AccountSaving(111, 222)
    cp1.withdraw(1)
    cp1.deposit(1)
    cp1.withdraw(1)
    print('----=====================----')
    cc1 = AccountCurrent(333, 444, 0, 100)
    cc1.withdraw(1)
    cc1.deposit(1)
    cc1.withdraw(1)
    cc1.withdraw(1)
    cc1.withdraw(98)
    cc1.withdraw(1)
    print('----=====================----')
