def sum(a, b):
    result = {}
    result['real'] = a['real'] + b['real']
    result['image'] = a['image'] + b['image']
    return result

def minus(a, b):
    result = {}
    result['real'] = a['real'] - b['real']
    result['image'] = a['image'] - b['image']
    return result

def  mul(a, b):
    result = {}
    result['real'] = (a['real'] * b['real']) - (a['image'] * b['image'])
    result['image'] = (a['real'] * b['image']) + (a['image'] * b['real'])
    return result

def show(x):
    print(x['real'],'i +', x['image'])

a = {'real':7, 'image':3}
b = {'real':1, 'image':0.5}

show(mul(a, b))