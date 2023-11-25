from os import environ
import logging
import requests
from datetime import datetime, timedelta

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

voting_platform = VotingPlatform()

def handle_advance(data):
    logger.info(f"Received advance request data {data}")

    if data["request_type"] == "advance_state":
        contract_id = data["contract_id"]
        contract = next((c for c in voting_platform.voting_contracts if id(c) == contract_id), None)
        if contract:
            contract.start_voting()

            results = contract.get_results()
            logger.info(f"Voting results for contract {contract_id}: {results}")

    return "accept"

def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")

    if data["request_type"] == "inspect_state":
        contract_id = data["contract_id"]
        contract = next((c for c in voting_platform.voting_contracts if id(c) == contract_id), None)
        if contract:
            return {
                "contract_id": contract_id,
                "start_time": contract.start_time.isoformat(),
                "end_time": contract.end_time.isoformat(),
                "votes": contract.votes
            }

    return "accept"

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
