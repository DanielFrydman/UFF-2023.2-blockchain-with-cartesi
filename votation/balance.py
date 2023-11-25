from cartesi.util import uint256, address

class Balance:
    def __init__(self, account: address):
        self.account = account
        self.balance = uint256(0)

    def get_balance(self) -> uint256:
        return self.balance

    def transfer(self, to: address, amount: uint256):
        if self.balance >= amount:
            self.balance -= amount
            Logger().log(f"Transferred {amount} to {to}")
        else:
            Logger().log("Insufficient funds")
