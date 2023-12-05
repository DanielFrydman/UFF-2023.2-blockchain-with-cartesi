import sqlite3


def increase_votes(candidate_id):
    query = 'update candidates set votes = votes + 1 where id = "' + candidate_id + '";'
    return update_data(query)


def vote_candidate(user, candidate_id):
    query = 'insert into voting_info (user, candidate_id) values ("' + user + '", "' + candidate_id + '");'
    return update_data(query)


def voted_candidate(user):
    query = 'select * from voting_info where user = "' + user + '"'
    voted = select_data(query)
    if len(voted) == 0:
        return {'error': 'You did not vote yet'}

    return voted[0]

def create_voting_contract_table():
    conn = init_conn()
    cur = conn.cursor()
    sql_query = "SELECT name FROM sqlite_master WHERE type='table';"
    result = cur.execute(sql_query)
    tables = result.fetchall()
    if len(tables) == 0:
        print("Metadata does not exist")
        # criar tabela aqui
        query_create_table = "CREATE TABLE voting_contracts(id text NOT NULL, question text NOT NULL, " \
                             "options voting_duration_in_seconds start_date end_date votes results" \
                             "status text NOT NULL DEFAULT waiting_to_start);"
        cur.execute(query_create_table)
        conn.commit()
        conn.close()
    else:
        print("Metadata exists")


def create_voting_contract(question, options, voting_duration_in_seconds):
    query = 'insert into voting_contracts (question, options, voting_duration_in_seconds)' \
            'values ("' + question + '", "' + options + '", "' + voting_duration_in_seconds + '");'
    return update_data(query)


def start_voting(voting_contract_id):
    query = 'update voting_contracts set status = started where id = "' + voting_contract_id + '";'
    return update_data(query)


def end_voting(voting_contract_id, results):
    query = 'update voting_contracts set status = finished and results = "' + results + '" where id = "' + voting_contract_id + '";'
    return update_data(query)


def vote(cpf, option, voting_contract_id):
    # apendar no array um hash { cpf: '...', option: '... }
    query = 'update voting_contracts set votes = "' + results + '"'
    return update_data(query)


def waiting_to_start_voting_list():
    query = 'select * from voting_contracts where status="' + 'waiting_to_start' + '"'
    return select_data(query)


def started_voting_list():
    query = 'select * from voting_contracts where status="' + 'started' + '"'
    return select_data(query)


def finished_voting_list():
    query = 'select * from voting_contracts where status="' + 'finished' + '"'
    return select_data(query)


def get_voting_contract_by_id(voting_contract_by_id):
    query = 'select * from voting_contracts where id="' + voting_contract_by_id + '"'
    return select_data(query)


def update_data(query):
    conn = init_conn()

    try:
        with conn:
            cur = conn.cursor()
            cur.execute(query)
            return {'message': 'Success'}
    except Exception as e:
        result = "EXCEPTION: " + e.__str__()
        print("NOTICE EXCEPTION" + e.__str__())
        return {'error': result}


def select_data(query):
    conn = init_conn()

    try:
        with conn:
            cur = conn.cursor()
            result = cur.execute(query)
            return result.fetchall()
    except Exception as e:
        result = "EXCEPTION: " + e.__str__()
        print("NOTICE EXCEPTION" + e.__str__())
        return result


def init_conn():
    conn = sqlite3.connect('voting_system.db')
    conn.row_factory = dict_factory
    return conn


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
