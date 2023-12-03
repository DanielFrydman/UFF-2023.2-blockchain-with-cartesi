from voting.logger import Logger
from voting.voting_contract import VotingContract

class VotingPlatform:
    def __init__(self):
        self.voting_contracts = []

    def create_voting_contract(
        self,
        voting_duration: int,
        options: list[str],
        question: str
    ) -> VotingContract:
        contract = VotingContract(self, voting_duration, options, question)
        self.voting_contracts.append(contract)
        Logger().log(f"Voting contract {id(contract)} created")
        return contract

    def get_voting_contracts(self) -> list[VotingContract]:
        return self.voting_contracts

    def get_voting_contract(self, contract_id: int):
        contract = next((c for c in self.voting_contracts if id(c) == contract_id), None)
        if contract:
            return contract
        else:
            Logger().log(f"Voting contract with ID {contract_id} not found")

    def start_voting(self, contract_id: int):
        contract = self.get_voting_contract(contract_id)
        if contract:
            contract.start_voting()
        else:
            Logger().log(f"Voting contract with ID {contract_id} not found")

    def vote(self, contract_id: int, cpf: str, option: str):
        contract = self.get_voting_contract(contract_id)
        if contract:
            contract.vote(cpf, option)
        else:
            Logger().log(f"Voting contract with ID {contract_id} not found")

    def end_voting(self, contract_id: int):
        contract = self.get_voting_contract(contract_id)
        if contract:
            contract.end_voting()
        else:
            Logger().log(f"Voting contract with ID {contract_id} not found")
