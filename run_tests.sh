docker-compose -f docker-compose-test.yml up --build -d
pytest
docker-compose -f docker-compose-test.yml down
