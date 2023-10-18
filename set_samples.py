import json
samples = []
with open('samples.jsonl', 'r') as f:
    samples = f.readlines()

for i in range(len(samples)):
    samples[i] = json.loads(samples[i])
    samples[i]['completion'] = samples[i]['completion']['choices'][0]['message']['content']

with open('samples.jsonl', 'w') as f:
    for sample in samples:
        f.write(json.dumps(sample) + '\n')