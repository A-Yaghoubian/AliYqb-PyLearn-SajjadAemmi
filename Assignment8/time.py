def sum(a, b):
    result = {}
    
    result['s'] = a['s'] + b['s']
    result['m'] = a['m'] + b['m']
    result['h'] = a['h'] + b['h']
    
    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1
    
    if result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1
        
    return result

def minus(a, b): # must a > b
    result = {}
    
    if a['s'] >= b['s']:
        result['s'] = a['s'] - b['s']
    else:
        a['s'] += 60
        a['m'] -= 1
        result['s'] = a['s'] - b['s']
    
    if a['m'] >= b['m']:
        result['m'] = a['m'] - b['m']
    else:
        a['m'] += 60
        a['h'] -= 1
        result['m'] = a['m'] - b['m']
    
    result['h'] = a['h'] - b['h']
    
    return result

def time_to_sec(x):
    seconds = x['s'] + (x['m'] * 60) + (x['h'] * 3600)

    return seconds

def sec_to_time(x):
    result = {}
    
    result['h'] = x // 3600
    x %= 3600

    result['m'] = x // 60
    x %= 60

    result['s'] = x
    
    return result

def show(time):
    print(time['h'], ':', time['m'], ':', time['s'])
    
time_1 = {'h':21, 'm':7, 's':21}
time_2 = {'h':8, 'm':57, 's':2}

output = time_to_sec(time_1)
print(output)
show(sec_to_time(76041))