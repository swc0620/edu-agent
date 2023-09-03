# Edu-Agent

## Installation

- Clone this repository

```
docker-compose build
docker-compose up
```

## Requirements

- python 3.9.6
- requirements

## TODO

- [ ] Add tests
- [ ] Make api calls async
- [ ] Make api calls in parallel
- [ ] Set up CI/CD
- [ ] Separate api calls from main.py
- [ ] Make dockerfile
- [ ] Add message queue

## Run
### Run Server in Python Code
```bash
python main.py
```

### Using Docker
```bash
docker build --tag edu-agent-api
```
```bash
docker run -d -p 80:8000 -p 443:8000 -e OPENAI_API_KEY={Write Your Key} edu-agent-api
```

## Test
### CORS Test
```bash
curl \
--verbose \
--request GET \
'http://localhost:8000' \
--header 'Origin: https://ai-note-six.vercel.app/' \
--header 'Access-Control-Request-Headers: Origin, Accept, Content-Type' \
--header 'Access-Control-Request-Method: GET'
```
