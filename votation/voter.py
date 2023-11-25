class Voter:
    def __init__(self, address: address, balance: Balance):
        self.address = address
        self.balance = balance
        self.votes = []

    def place_vote(self, option: str):
        vote = Vote(option, self)
        self.votes.append(vote)
        Logger().log(f"Vote placed by {self.address} for option {option}")
