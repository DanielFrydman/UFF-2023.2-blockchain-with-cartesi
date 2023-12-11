import ast
import json
from collections import Counter
from datetime import datetime, timedelta
from dataService import create_voting_contract_table, \
                        create_voting_contract, \
                        start_voting_contract, \
                        end_voting_contract, \
                        get_voting_contract_by_id, \
                        voting_list_by_status, \
                        update_votes


def initialize_voting_contract():
    create_voting_contract_table()
    return 'Table created'


def create_voting(title, options, voting_duration_in_seconds):
    return create_voting_contract(title, options, voting_duration_in_seconds)


def start_voting(voting_contract_id):
    voting_contract = get_voting_contract_by_id(voting_contract_id)
    voting_duration_in_seconds = voting_contract.get('voting_duration_in_seconds', 0)
    start_date = datetime.now()
    end_date = start_date + timedelta(seconds=voting_duration_in_seconds)
    return start_voting_contract(voting_contract_id, start_date, end_date)


def end_voting(voting_contract_id):
    voting_contract = get_voting_contract_by_id(voting_contract_id)
    votes =  _votes(voting_contract)
    results = _calculate_results(votes)
    return end_voting_contract(voting_contract_id, results)

def _calculate_results(votes):
    vote_counts = Counter(vote['option'] for vote in votes)
    winner = max(vote_counts, key=vote_counts.get)
    results = {option: vote_counts[option] for option in vote_counts}
    results['winner'] = winner
    return results


def vote(cpf, option, voting_contract_id):
    voting_contract = get_voting_contract_by_id(voting_contract_id)

    if not _is_voting_period_valid(voting_contract):
        return f"Cannot vote at the moment. The voting period is not valid for {voting_contract.get('title')}"
    elif not _option_exists(voting_contract, option):
        return f"Option: {option} does not exists for {voting_contract.get('title')}. Valid options: {voting_contract.get('options', [])}"
    elif not _cpf_has_voted(voting_contract, cpf):
        votes = _votes(voting_contract)
        votes.append({"cpf": cpf, "option": option})
        update_votes(voting_contract_id, votes)
        return f"{cpf} has just voted in {voting_contract.get('title')}"
    else:
        return f"{cpf} already voted in {voting_contract.get('title')}"

def _is_voting_period_valid(voting_contract):
    start_date_str = voting_contract.get('start_date')
    end_date_str = voting_contract.get('end_date')

    if start_date_str and end_date_str:
        format_str = "%Y-%m-%d %H:%M:%S.%f"
        start_date = datetime.strptime(start_date_str, format_str)
        end_date = datetime.strptime(end_date_str, format_str)

        current_time = datetime.now()
        return start_date <= current_time <= end_date
    else:
        return False

def _option_exists(voting_contract, option):
    return any(voting_option == option for voting_option in ast.literal_eval(voting_contract.get('options', [])))

def _cpf_has_voted(voting_contract, cpf):
    return any(vote['cpf'] == cpf for vote in _votes(voting_contract))

def _votes(voting_contract):
    votes = voting_contract.get('votes', [])
    return json.loads(votes)


def waiting_to_start_voting_list():
    return voting_list_by_status('waiting_to_start')


def in_progress_voting_list():
    return voting_list_by_status('in_progress')


def finished_voting_list():
    return voting_list_by_status('finished')
