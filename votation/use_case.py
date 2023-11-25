# Exemplo de uso
platform = VotingPlatform()

# Criar contrato de votação
contract1 = platform.create_voting_contract(uint256(60))  # 60 segundos de duração
contract2 = platform.create_voting_contract(uint256(120)) # 120 segundos de duração

# Criar eleitores
voter1_balance = Balance(address("0x123"))
voter2_balance = Balance(address("0x456"))

voter1 = Voter(address("0x123"), voter1_balance)
voter2 = Voter(address("0x456"), voter2_balance)

# Iniciar votações
contract1.start_voting()
contract2.start_voting()

# Eleitores votam
contract1.vote(voter1, "OptionA")
contract1.vote(voter2, "OptionB")

contract2.vote(voter1, "OptionX")
contract2.vote(voter2, "OptionY")

# Encerrar votações
contract1.end_voting()
contract2.end_voting()