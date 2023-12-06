import sqlite3
import json


SELECT_QUERY = "SELECT * FROM voting_contracts WHERE id = ?"


def create_voting_contract_table():
    conn = init_conn()
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='voting_contracts';")
    table_exists = cur.fetchone()

    if not table_exists:
        query_create_table = '''
            CREATE TABLE voting_contracts (
                id INTEGER PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                options TEXT NOT NULL,
                voting_duration_in_seconds INTEGER NOT NULL,
                start_date DATETIME DEFAULT NULL,
                end_date DATETIME DEFAULT NULL,
                votes TEXT NOT NULL DEFAULT '[]',
                results TEXT NOT NULL DEFAULT '{}',
                status TEXT NOT NULL DEFAULT 'waiting_to_start'
            );
        '''
        cur.execute(query_create_table)
        conn.commit()
        print("Table 'voting_contracts' created.")
    else:
        # cur.execute("DROP TABLE IF EXISTS voting_contracts;")
        # conn.commit()
        print("Table 'voting_contracts' already exists.")

    conn.close()


def create_voting_contract(title, options, voting_duration_in_seconds):
    options_str = json.dumps(options)
    query = 'INSERT INTO voting_contracts (title, options, voting_duration_in_seconds)' \
            'VALUES (?, ?, ?)'
    values = (title, options_str, voting_duration_in_seconds)
    return update_data(query, values, SELECT_QUERY)


def start_voting_contract(voting_contract_id, start_date, end_date):
    query = 'UPDATE voting_contracts SET status = "in_progress", start_date = ?, end_date = ? WHERE id = ?'
    values = (start_date, end_date, voting_contract_id)
    return update_data(query, values, SELECT_QUERY)


def end_voting_contract(voting_contract_id, results):
    results_str = json.dumps(results)
    query = 'UPDATE voting_contracts SET status = "finished", results = ? WHERE id = ?'
    values = (results_str, voting_contract_id)
    return update_data(query, values, SELECT_QUERY)


def update_votes(voting_contract_id, votes):
    votes_str = json.dumps(votes)
    query = 'UPDATE voting_contracts SET votes = ? WHERE id = ?'
    values = (votes_str, voting_contract_id)
    return update_data(query, values)


def voting_list_by_status(status):
    query = 'SELECT * FROM voting_contracts WHERE status=?'
    values = (status,)
    return select_data(query, values)


def get_voting_contract_by_id(voting_contract_by_id):
    query = 'SELECT * FROM voting_contracts WHERE id=?'
    values = (voting_contract_by_id,)
    result = select_data(query, values)
    return result[0] if result else None


def update_data(query, values=None, select_query=None):
    conn = init_conn()

    try:
        with conn:
            cur = conn.cursor()
            if values:
                cur.execute(query, values)
            else:
                cur.execute(query)

            voting_contract_id = cur.lastrowid if cur.lastrowid != 0 else values[1]

            if select_query:
                cur.execute(select_query, (voting_contract_id,))
                result = cur.fetchone()
            else:
                result = None

            return {'message': 'Success', 'result': result}
    except Exception as e:
        result = "EXCEPTION: " + e.__str__()
        print("NOTICE EXCEPTION" + e.__str__())
        return {'error': result}
    finally:
        conn.close()


def select_data(query, params=None):
    conn = init_conn()

    try:
        with conn:
            cur = conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            result = cur.fetchall()
            return result
    except Exception as e:
        result = "EXCEPTION: " + e.__str__()
        print("NOTICE EXCEPTION" + e.__str__())
        return result
    finally:
        conn.close()

def init_conn():
    conn = sqlite3.connect('voting_system.db')
    conn.row_factory = dict_factory
    return conn


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
