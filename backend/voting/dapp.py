from os import environ
import logging
import requests
from datetime import datetime
import json
from voting.voting_platform import VotingPlatform

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

voting_platform = VotingPlatform()

def handle_advance(data):
    logger.debug(f"Received advance request data {data}")
    try:
        return 'uhul'
    except Exception as error:
        error_msg = f"Failed to process advance_request. {error}"
        logger.debug(error_msg, exc_info=True)
        return Error(error_msg)

def handle_inspect(data):
    logger.debug(f"Received advance request data {data}")
    try:
        return 'uhul'
    except Exception as error:
        error_msg = f"Failed to process advance_request. {error}"
        logger.debug(error_msg, exc_info=True)
        return Error(error_msg)

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
