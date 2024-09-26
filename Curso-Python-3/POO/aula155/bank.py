import accounts,people

class Bank:
    def __init__(self, 
                 agency: list[int] | None = None,
                 client: list[people.People] | None = None,
                 account: list[accounts.Account] | None = None
                 ) -> None:
        self.agencys = agency or []
        self.clients = client or []
        self.accounts = account or []

    def _valid_agency(self,agency: int) -> bool:
        if agency in self.agencys:
            print('Validando agência...', True)
            return True
        print('Validando agência...', False)
        return False

    def _valid_client(self, client: people.People) -> bool:
        if client in self.clients:
            print('Validando cliente...', True)
            return True
        print('Validando cliente...', False)
        return False

    def _valid_account(self,account) -> bool:
        if account in self.accounts:
            print('Validando conta...', True)
            return True
        print('Validando conta...', False)
        return False

    def _valid_account_client(self,client: people.Client, account: accounts.Account)-> bool :
        if account is client.account:
            print('Validando conta do cliente...', True)
            return True
        print('Validando conta do cliente...', False)
        return False
    
    def valid(self, client, account:accounts.Account) -> bool :
        return self._valid_account(account) and \
               self._valid_agency(account.agency) and \
               self._valid_client(client) and \
               self._valid_account_client(client ,account)
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencys!r}, {self.accounts!r}, {self.clients!r})'
        return f'{class_name} {attrs}'

if __name__ == '__main__':
    c1 = people.Client('Lucas',20,None)
    cc1 = accounts.AccountCurrent(111,222,0,0)
    c1.account = cc1
    c2 = people.Client('Maria',20,None)
    cp2 = accounts.AccountSaving(112,223,100)
    c2.account = cp2
    banco = Bank()
    banco.clients.extend([c1,c2])
    banco.accounts.extend([cc1,cp2])
    banco.agencys.extend([111,222])

    if banco.valid(c1,cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)
