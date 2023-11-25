from datetime import datetime, timedelta

class VotingContract:
    def __init__(self, platform_address: address, voting_duration: uint256):
        self.platform_address = platform_address
        self.voting_duration = voting_duration
        self.start_date = None
        self.end_date = None
        self.options = []
        self.votes = []

    def start_voting(self):
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(seconds=int(self.voting_duration))
        Logger().log(f"Voting started for contract {id(self)}")

    def vote(self, voter: Voter, option: str):
        if datetime.now() >= self.start_date and datetime.now() <= self.end_date:
            if option in self.options:
                voter.place_vote(option)
                vote = Vote(option, voter)
                self.votes.append(vote)
                Logger().log(f"Vote recorded for contract {id(self)}")
            else:
                Logger().log(f"Invalid option: {option}")
        else:
            Logger().log("Voting is not currently allowed")

    def end_voting(self):
        Logger().log(f"Voting ended for contract {id(self)}")
        # fazer calculo offchain?


    def get_results(self):
        results = {"total_votes": len(self.votes), "choices": {}}
        for choice in set(self.votes.values()):
            results["choices"][choice] = list(self.votes.values()).count(choice)
        return results
