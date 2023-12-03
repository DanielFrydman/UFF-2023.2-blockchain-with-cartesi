from datetime import datetime, timedelta
from voting.logger import Logger
from voting.voter import Voter
from voting.vote import Vote

class VotingContract:
    def __init__(
        self,
        platform: 'VotingPlatform',
        voting_duration_in_seconds: int,
        options: list[str],
        question: str
    ):
        self.platform = platform
        self.voting_duration_in_seconds = voting_duration_in_seconds
        self.start_date = None
        self.end_date = None
        self.options = options
        self.question = question
        self.votes = {}
        self.results = {}
        self.status = 'waiting_to_start'

    def start_voting(self):
        self.end_date = self.start_date + timedelta(seconds=int(self.voting_duration))
        self.status = 'started'
        Logger().log(f"Voting started for contract {id(self)}")

    def vote(self, cpf: str, option: str):
        if datetime.now() >= self.start_date and datetime.now() <= self.end_date:
            voter = self._create_voter(cpf)

            if self.votes[voter.address] != None:
                return Logger().log(f"Voter {voter.cpf} has already voted")
            if option not in self.options:
                return Logger().log(f"Invalid option: {option}")

            vote = Vote(option, voter)
            voter.place_vote(vote)
            self.votes[voter.address] = vote
            Logger().log(f"Vote recorded for contract {id(self)}")
        else:
            Logger().log("Voting is not currently allowed")

    def end_voting(self):
        Logger().log(f"Voting ended for contract {id(self)}")
        self.results = {"total_votes": len(self.votes), "options": {}}
        for option in self.options:
            self.results["options"][option] = list(self.votes.values()).count(option)
        self.status = 'finished'
        return self.results

    def _create_voter(self, cpf: str):
        return Voter(cpf)
        