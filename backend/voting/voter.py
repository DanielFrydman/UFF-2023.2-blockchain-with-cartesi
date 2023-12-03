from voting.vote import Vote
from voting.logger import Logger

class Voter:
    def __init__(self, cpf: str):
        self.cpf = cpf
        self.votes = []

    def place_vote(self, vote: Vote):
        self.votes.append(vote)
        Logger().log(f"Vote placed by {self.address} for option {option}")
