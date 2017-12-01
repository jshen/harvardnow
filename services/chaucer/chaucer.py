import random, json
def eval():
    return ''.join(random.sample(json.load(open('chaucer.json', 'r')), 1)[0])
special = 'Text "chaucer" to get a full Chaucer verse'
