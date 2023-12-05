from dataService import create_voting_contract_table, \
                        create_voting_contract, \
                        get_voting_contract_by_id, \
                        waiting_to_start_voting_list, \
                        started_voting_list, \
                        finished_voting_list

def initialize_voting_contract():
    create_voting_contract_table()
    return 'Table created'

def create_voting(question, options, voting_duration_in_seconds):
    voting = create_voting_contract(question, options, voting_duration_in_seconds)
    return f"Voting #{voting} created"

def start_voting(voting_contract_id):
    start_voting(voting_contract_id)
    return "Voting started"

def end_voting(voting_contract_id):
    voting_contract = get_voting_contract_by_id(voting_contract_id)
    # voting_contract.votes ...
    # results = ...
    end_voting(voting_contract_id, results)
    return "Voting finished"

def vote(cpf, option, voting_contract_id):
    voting_contract = get_voting_contract_by_id(voting_contract_id)
    if pode_votar:
        # update do hash com votos vote = ...
        vote(vote, voting_contract_id)
        return f"#{cpf} has just voted in #{voting_contract}"
    else:
        return f"#{cpf} already voted in #{voting_contract}"

def waiting_to_start_voting_list():
    all_waiting_to_start_votings = waiting_to_start_voting_list()
    # retornar apenas ID, question, data inicio e data fim
    return all_waiting_to_start_votings

def started_voting_list():
    all_started_votings = started_voting_list()
    # retornar apenas ID, question, data inicio e data fim
    return all_started_votings

def finished_voting_list():
    all_finished_votings = finished_voting_list()
    # retornar apenas ID, question, data inicio e data fim
    return all_finished_votings
