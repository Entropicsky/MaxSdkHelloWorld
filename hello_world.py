from answer_rocket import AnswerRocketClient
import json

def call_me():
    client = AnswerRocketClient()
    j = client.config.get_artifact('test.json')
    return json.loads(j)

def get_greeting():
    client = AnswerRocketClient()
    greeting = client.config.get_artifact('greeting.html')
    return greeting


if __name__ == '__main__':
    x = get_greeting()
    print(x)
