## Project Description
This project is a versatile and user-friendly voting system that allows individuals to both create and participate in various voting sessions. The system accommodates a wide range of voting scenarios, empowering users to engage in decision-making processes efficiently.


## Key Features
### Create Votings:
Users can initiate new voting sessions, defining questions, available options, and the duration of the voting period.

### Participate in Votings:
Individuals can actively participate in existing voting sessions by casting their votes for the available options.

### Dynamic Questioning:
The system supports the creation of voting sessions with diverse questions, making it suitable for a broad spectrum of use cases.

### Flexible Options:
Voters can choose from a range of options presented in each voting session, offering flexibility and inclusivity.

### Duration Configuration:
Creators have the flexibility to set the duration of each voting session, tailoring the system to suit the specific needs of different scenarios.


## Technologies Used
### Sunodo:
A key component in building a secure and efficient voting system.

### Python:
The primary programming language for developing the system's backend and logic.

### Cartesi:
A technology integral to enhancing the system's scalability and security.

### SQLite3:
The chosen database management system for storing and retrieving voting-related data.

### Angular:
The frontend of the system is built using Angular, a powerful and popular frontend framework, providing a dynamic and responsive user interface.


## Building the environment

To run the system, clone the repository as follows:

```shell
git clone git@github.com:DanielFrydman/UFF-2023.2-blockchain-with-cartesi.git
```

Then, build the back-end for the voting example:

```shell
cd UFF-2023.2-blockchain-with-cartesi/
make machine
```


## Running the environment in host mode

During the development of an application, it is crucial to have the ability to test and debug it seamlessly. In the context of our voting system project.

To run the environment in host mode, follow these steps:

```shell
docker-compose -f docker-compose.yml -f docker-compose-host.yml up --build
```

The server is written in Python, so make sure you have python3 installed. In order to start the server, run the following commands in a dedicated terminal:

```shell
cd backend/server/
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt
ROLLUP_HTTP_SERVER_URL="http://127.0.0.1:5004" python3 voting.py
```

This will run the voting server and send the corresponding notices to port `5004`. The final command, which effectively starts the server.

P.S.: You can use a tool like [entr](https://eradman.com/entrproject/) to restart it automatically when the code changes, It's very usefull! For example: 

```shell
ls *.py | ROLLUP_HTTP_SERVER_URL="http://127.0.0.1:5004" entr -r python3 voting.py
```

After the server successfully starts, it should print an output like the following:

```
INFO:__main__:HTTP rollup_server url is http://127.0.0.1:5004
INFO:__main__:Sending finish
```

After that, you can interact with the application normally [as explained bellow](#interacting-with-the-application).

When you add an input, you should see something like:

```shell
INFO:__main__:Received finish status 200
INFO:__main__:Received advance request data {'metadata': {'msg_sender': '0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266', 'epoch_index': 0, 'input_index': 0, 'block_number': 0, 'timestamp': 0}, 'payload': '0x63617274657369'}
INFO:__main__:Adding notice
INFO:__main__:Received notice status 200 body b'{"index":0}'
INFO:__main__:Sending finish
```

If you need to stop the containers and remove any associated volumes, run this:

```shell
docker-compose -f docker-compose.yml -f docker-compose-host.yml down -v
```


## Interacting with the application (By Angular Frontend)

TO DO


## Interacting with the application (By Terminal)

Go to a separate terminal window, switch to the `contracts` directory, and run `yarn`:

```shell
cd backend/contracts/
yarn
```

If you want to create a voting, use this query:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"CREATE_VOTING", "title": YOUR_TITLE_IN_STRING, "options": [OPTION_ONE_IN_STRING, OPTION_TWO_IN_STRING, ...], "voting_duration_in_seconds": DURATION }'
```

If you want to start the voting:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"START_VOTING", "voting_contract_id": ID }'
```

If you want to finish the voting:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"END_VOTING", "voting_contract_id": ID }'
```

If you want to vote:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"VOTE", "cpf": CPF_IN_STRING, "option": OPTION_IN_STRING, "voting_contract_id": ID }'
```

If you want to get all votings that is waiting to start:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"WAITING_TO_START_VOTING_LIST" }'
```

If you want to get all votings that is in progress:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"IN_PROGRESS_VOTING_LIST" }'
```

If you want to get all votings that is finished:

```shell
npx hardhat --network localhost voting:addInput --input '{ "action":"FINISHED_VOTING_LIST" }'
```

Finally, note that you can check the available options for all Hardhat tasks using the `--help` switch:

```shell
npx hardhat --help
```
