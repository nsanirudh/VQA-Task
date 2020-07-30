import json
data = open('Quest_Answers.json').read()
data = json.loads(data)
print(data)