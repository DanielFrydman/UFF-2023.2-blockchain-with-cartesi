# Copyright 2022 Cartesi Pte. Ltd.
#
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from os import environ
import logging
import requests
import json
from actions import *
from votingService import *

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")


def to_hex(value):
    return "0x" + value.encode().hex()


def add_notice(message):
    message = to_hex(message)
    print("Adding notice")
    response_data = requests.post(rollup_server + "/notice", json={"payload": message})
    print(f"Received notice status {response_data.status_code} body {response_data.json()}")
    return True


def call_finish():
    print("Finishing")
    response_data = requests.post(rollup_server + "/finish", json={"status": "accept"})
    print(f"Received finish status {response_data.status_code}")
    return response_data


def handle_advance(data):
    body = data
    print(f"Received advance request body {body}")
    initialize_voting_contract()

    payload = bytes.fromhex(body["payload"][2:]).decode()
    print(payload)

    if payload == '':
        print('Default call')
        add_notice(json.dumps({'message': 'Default request'}))
        return "accept"

    payload = json.loads(payload)

    if payload['action'] == CREATE_VOTING:
        result = create_voting(payload['title'], payload['options'], payload['voting_duration_in_seconds'])
    elif payload['action'] == START_VOTING:
        result = start_voting(payload['voting_contract_id'])
    elif payload['action'] == END_VOTING:
        result = end_voting(payload['voting_contract_id'])
    elif payload['action'] == VOTE:
        result = vote(payload['cpf'], payload['option'], payload['voting_contract_id'])
    elif payload['action'] == WAITING_TO_START_VOTING_LIST:
        result = waiting_to_start_voting_list()
    elif payload['action'] == IN_PROGRESS_VOTING_LIST:
        result = in_progress_voting_list()
    elif payload['action'] == FINISHED_VOTING_LIST:
        result = finished_voting_list()
    else:
        result = {}

    print(result)
    print("Result type: " + type(result).__name__)
    add_notice(json.dumps(result))
    return "accept"


def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")
    logger.info("Adding report")
    report = {"payload": data["payload"]}
    response_data = requests.post(rollup_server + "/report", json=report)
    logger.info(f"Received report status {response_data.status_code}")
    return "accept"


handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}


finish = {"status": "accept"}
while True:
    logger.info("Sending finish")
    response = call_finish()
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
