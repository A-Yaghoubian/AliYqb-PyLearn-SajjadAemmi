def sum(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] + a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def mul(a, b):
    result = {}
    result['n'] = a['n'] * b['n'] 
    result['d'] = a['d'] * b['d']
    return result

def minus(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] - a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def div(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] 
    result['d'] = a['d'] * b['n']
    return result

def show(x):
    print(x['n'], '/', x['d'])

a = {'n':1, 'd':1}
b = {'n':1, 'd':1}

s = sum(a, b)
mu = mul(a, b)
mi = minus(a, b)
d = div(a, b)

show(s)