# Python Chat Room

A Python single-chat-room server using Websocket with MongoDB as the database 


### Docker setup (Recommended)

#### Prerequisite
1. [Docker](https://www.docker.com/products/docker-desktop)

#### Instruction
1. Create an .env.docker file and add the values that need to be overwritten in `main/config.py`. For example:
```
MONGO_URI=mongodb://mongodb:27017
```
2. Spin up all service using docker-compose
```
docker-compose up --build
```

### Manual setup

#### Prerequisite
1. [Python3](https://www.python.org/downloads/)
2. [MongoDB](https://www.mongodb.com/try/download/community)

#### Instruction
1. Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Create an .env file and add the values that need to be overwritten in `main/config.py`. For example:
```
MONGO_URI=mongodb://localhost:27017
```


4. Start the server locally (listening on 8000)
```
./start_server.sh
```
or
```
uvicorn main:app --port 8000 --reload
```

API documentation could be found at http://localhost:8000/redoc


### Test the app
1. Install Websocket test client [wscat](https://www.npmjs.com/package/wscat)
([Nodejs](https://nodejs.org/en/download/) is required)

2. Install API testing tool [Postman](https://www.postman.com/downloads/)

3. Import `python_chat_server.postman_collection.json` in Postman. [Instruction can be found here](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/)

4. Create a user using POST /auth. Response should look like
```
{
    "id": "{{YOUR_USER_ID}}",
    "name": "Hiep"
}
```

5. Using the id to connect to chat server. From your terminal
```
$ wscat --connect ws://localhost:8000/chat/{{YOUR_USER_ID}}
```

6. Repeat step 4 and 5 to have multiple users in your chat room (You should have multiple terminal tab open)

7. Start sending chat message in `wscat` console and expect the message is sent to other clients


### Integration tests
1. Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the tests
```
./run_tests.sh
```
