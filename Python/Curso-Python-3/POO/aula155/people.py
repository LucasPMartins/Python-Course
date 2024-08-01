import accounts

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, name: str):
        self._name = name


    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name} {attrs}'

class Client(People):
    def __init__(self, name: str, age: int, account) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None

if __name__ == '__main__':
    c1 = Client('Lucas',20,None)
    c1.account = accounts.AccountCurrent(111,222,0,0)
    print(c1)
    print(c1.account)
    c2 = Client('Maria',20,None)
    c2.account = accounts.AccountSaving(112,223,100)
    print(c2)
    print(c2.account)