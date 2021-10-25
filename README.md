# Python Chat Room

A Python single-chat-room server using Websocket with MongoDB as the database 


### Docker setup

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
./start.sh
```
or
```
uvicorn main:app --port 8000 --reload
```

