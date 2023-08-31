# Edu-Agent

## Installation

- Clone the repository
- Install requirements

```
pip install -r requirements.txt
```

- Set API key in .env file with name `OPENAI_API_KEY`
- Run `python main.py`

```
uvicorn main:app --reload
```

## Requirements

- python 3.9.6
- requirements.

## TODO

- [ ] Add tests
- [ ] Make api calls async
- [ ] Make api calls in parallel
- [ ] Set up CI/CD
- [ ] Separate api calls from main.py
- [ ] Make dockerfile
- [ ] Add message queue
