import Film, Series, Clip, Documentary
from pyfiglet import Figlet
import qrcode

media = []
address = 'database.txt'
qrcode_address = 'qrcode.png'

def show_menu():
    print('0- Show List')
    print('1- Add Media')
    print('2- Edit Media')
    print('3- Delete Media')
    print('4- Search')
    print('5- Advanced Search')
    print('6- Download Media')
    print('7- Qr Code')
    print('8- Exit & Save')

def welcome():
    f = Figlet(font='standard')
    print(f.renderText('MEDIA (A.Y)'))

def print_line():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def database(address):
    database_file = open(address, 'r')
    data = database_file.read()
    database_file.close()
    data = data.strip()
    return data

def load():
    print('Loading ...')
    data = database(address)
    media_list = data.split('\n')
    
    for i in range(len(media_list)):
        media_info = media_list[i].split(',')
        if media_info[0] == 'Film':
            film = Film.Film(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7], media_info[8])
            media.append(film)
        elif media_info[0] == 'Clip':
            clip = Clip.Clip(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7])
            media.append(clip)
        elif media_info[0] == 'Series':
            series = Series.Series(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7], media_info[8], media_info[9])
            media.append(series)
        elif media_info[0] == 'Documentary':
            documentary = Documentary.Documentary(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7])
            media.append(documentary)
            
    welcome()

def show_list():
    for i in range(len(media)):
        print_line()
        print('(', i, ')')
        print('<<', type(media[i]).__name__, '>>')
        media[i].showInfo()
        
def add_media():
    mode = int(input('1.Film - 2.Series - 3.Clip - 4.Documentary'))
    if mode == 4:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        year = input('Year = ')
        documentary = Documentary.Documentary(name, director, score, url, duration, casts, year)
        media.append(documentary)
    elif mode == 3:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        subject = input('Subject = ')
        clip = Clip.Clip(name, director, score, url, duration, casts, subject)
        media.append(clip)
    elif mode == 2:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        genre = input('Genre = ')
        season = input('Season = ')
        episode = input('Episode = ')
        serie = Series.Series(name, director, score, url, duration, casts, genre, season, episode)
        media.append(serie)
    else:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        genre = input('Genre = ')
        year = input('Year = ')
        film = Film.Film(name, director, score, url, duration, casts, genre, year)
        media.append(film)

def edit_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media[choice].edit()
    
def delete_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media.pop(choice)

def search(): # search by name
    flag = 0
    search_name = input('your media name? ')
    for i in media:
        if i.name == search_name:
            print_line()
            i.showInfo()
            flag = 1
    if flag == 0:
        print('Not Found :(')

def adv_search(): # search by minutes
    flag = 0
    time_a = int(input('Enter your first time: '))
    time_b = int(input('Enter your second time: '))
    for i in media:
        time = int(i.getDuration())
        if time >= time_a and time <= time_b:
            print_line()
            i.showInfo()
            flag = 1
    if flag == 0:
        print('Not Found :(')

def download_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media[choice].download()

def QrCode():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    
    qr_code = media[choice].getQrcode()
    img = qrcode.make(qr_code)
    img.save(qrcode_address)
    print('Media\'s QR Code is Ready :)')

def save():
    database_file = open(address, 'w')
    for i in range(len(media)):
        var = media[i]
        name_cast = ''
        for j in var.casts:
            name_cast += j.showInfo()
            name_cast += ' - '
            name_cast = name_cast[:-2]
        if type(var).__name__ == 'Film':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%('Film',var.name,var.director,var.IMDB_scores,var.url,var.duration,name_cast,var.genre,var.year))
        elif type(var).__name__ == 'Clip':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s\n'%('Clip',var.name,var.director,var.IMDB_scores,var.url,var.duration,name_cast,var.subject))
        elif type(var).__name__ == 'Series':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%('Series',var.name,var.director,var.IMDB_scores,var.url,var.duration,name_cast,var.genre,var.season,var.episode))
        elif type(var).__name__ == 'Documentary':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s\n'%('Documentary',var.name,var.director,var.IMDB_scores,var.url,var.duration,name_cast,var.year))

    database_file.close()
    print('Your changes saved well :)')

def main_media():   
    while True:
        print_line()
        show_menu()
        choice = int(input('Please choose a number:  '))
        print_line()

        if choice == 0: # show list
            show_list()
            
        if choice == 1: # add media
            add_media()

        elif choice == 2: # edit media
            edit_media()

        elif choice == 3: # delete media
            delete_media()

        elif choice == 4: # search
            search()

        elif choice == 5: # advanced search
            adv_search()

        elif choice == 6: # download media
            download_media()

        elif choice == 7: # Qr Code
            QrCode()

        elif choice == 8: # exit and save
            save()
            print('Good Bye ...')
            break
        
        else:
            print('Please choose a correct number!')
            continue
        
load()
main_media()