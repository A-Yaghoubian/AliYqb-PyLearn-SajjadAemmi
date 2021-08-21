translator_list = []
address = 'E:\programming\PyLearn-SajjadAemmi\Assignment7\Translate.txt'

def download_texts(address):    
    try:
        text_file = open(address, 'r')
        texts = text_file.read()
    except:
        print('Your file address is wrong.\nPlease check it.')
        exit()
    
    text_file.close()
    
    list_of_texts = texts.strip().split('\n')
    
    for i in range(0, len(list_of_texts), 2):
        my_dict = {'english':list_of_texts[i], 'persian':list_of_texts[i + 1]}
        translator_list.append(my_dict)
    
    print('@ Download is complete @')

def add():
    while True:
        english_word = input('Input Your ENGLISH word = ')
        persian_word = input('Input Your PERSIAN word = ')
        
        add_dict = {'english':english_word, 'persian':persian_word}
        translator_list.append(add_dict)
        
        question = input('Do you add a new world ? (y or n) ')
        if question == 'y':
            continue
        else:
            break

def test():
    for i in range(len(translator_list)):
        print(translator_list[i])

def save():
    database_file = open(address, 'w')
    for i in range(len(translator_list)):
        save_dict = translator_list[i]
        english = save_dict['english']
        persian = save_dict['persian']
        database_file.write('%s\n%s\n'%(english,persian))
    database_file.close()
    print('Your changes saved well :)')

def translate(model, word):
    if model == 1: # english to persian
        for i in translator_list:
            if i['english'] == word:
                return i['persian']
    
    elif model == 2: # persian to english
        for i in translator_list:
            if i['persian'] == word:
                return i['english']
            
    return False

def english2persian():
    statements = input('input: ')
    words = statements.strip().split(' ')
    output = ''
    for word in words:
        if word == '':
            continue
        
        elif word == '.':
            output += ' '
            output += '.'
        
        elif word[0] == '.':
            word = word[1:]
            if translate(1, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += '.'
                output += translate(1, word)
        
        elif word[-1] == '.':
            word = word[:-1]
            if translate(1, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += translate(1, word)
                output += '.'
        
        elif '.' in word:
            for i in range(len(word)):
                if word[i] == '.':
                    if translate(1, word[:i]) == False:
                        print(word[:i], 'is not exist in Translate.txt')
                        output += ' '
                        output += word[:i]
                    else:
                        output += ' '
                        output += translate(1, word[:i])
                    
                    output += '.'
                    
                    if translate(1, word[i+1:]) == False:
                        print(word[i+1:], 'is not exist in Translate.txt')
                        output += word[i+1:]
                    else:
                        output += translate(1, word[i+1:])
                    
                    break
        
        else:
            if translate(1, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += translate(1, word)
    
    print('output:', output.strip())
        
def persian2english():
    statements = input('input: ')
    words = statements.strip().split(' ')
    output = ''
    for word in words:
        if word == '':
            continue
        
        elif word == '.':
            output += ' '
            output += '.'
        
        elif word[0] == '.':
            word = word[1:]
            if translate(2, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += '.'
                output += translate(2, word)
        
        elif word[-1] == '.':
            word = word[:-1]
            if translate(2, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += translate(2, word)
                output += '.'
        
        elif '.' in word:
            for i in range(len(word)):
                if word[i] == '.':
                    if translate(2, word[:i]) == False:
                        print(word[:i], 'is not exist in Translate.txt')
                        output += ' '
                        output += word[:i]
                    else:
                        output += ' '
                        output += translate(2, word[:i])
                    
                    output += '.'
                    
                    if translate(2, word[i+1:]) == False:
                        print(word[i+1:], 'is not exist in Translate.txt')
                        output += word[i+1:]
                    else:
                        output += translate(2, word[i+1:])
                    
                    break
        
        else:
            if translate(2, word) == False:
                print(word, 'is not exist in Translate.txt')
                output += ' '
                output += word
            else:
                output += ' '
                output += translate(2, word)
    
    print('output:', output.strip())

def menu():
    while True:
        print('-----MENU-----\n1. Add new word\n2. translation english2persian\n3. translation persian2english\n4. exit')
        choice = int(input('Your Choice = '))
        
        if choice == 1: # add
            add()
        
        elif choice == 2: # english2persian
            english2persian()
        
        elif choice == 3: # persian2english
            persian2english()
        
        elif choice == 4: # exit
            ans = input('Do you save your changes? (y or n) ')
            if ans == 'y':
                save()
            print('See you soon :)')
            break
        
        elif choice == 5:
            test()
        
        else:
            print('-----WARNING-----\nYou choose wrong number!')

download_texts(address)
menu()