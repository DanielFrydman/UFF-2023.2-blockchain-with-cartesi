from cartesi.util import uint256

class VotingPlatform:
    def __init__(self):
        self.voting_contracts = []

    def create_voting_contract(self, voting_duration: uint256) -> VotingContract:
        contract = VotingContract(self, voting_duration)
        self.voting_contracts.append(contract)
        Logger().log(f"Voting contract {id(contract)} created")
        return contract

    def get_voting_contracts(self) -> list[VotingContract]:
        return self.voting_contracts
