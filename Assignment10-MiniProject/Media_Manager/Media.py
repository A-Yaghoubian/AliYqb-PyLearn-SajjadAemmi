import Actor
import pytube

class Media():
    
    def __init__(self, class_name, class_director, class_score, class_url, class_duration, class_casts):
        self.name = class_name
        self.director = class_director
        self.IMDB_scores = class_score
        self.url = class_url
        self.duration = class_duration
        self.casts = []
        cast = class_casts
        c = cast.split('-')
        for i in range(len(c)):
            actor  = Actor.Actor(c[i].strip())
            self.casts.append(actor)   
        
    def showInfo(self):
        print('Name: ', self.name)
        print('Director: ', self.director)
        print('IMDB Scores: ', self.IMDB_scores)
        print('Duration: ', self.duration)
        actor_print = []
        for i in range(len(self.casts)):
            actor_print.append(self.casts[i].showInfo())
        print('Casts: ', actor_print)

    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='yourMedia.mp4')
        print('Downlaod is Complete :)')
        
    def edit(self):
        new_name = input('Name = ')
        new_director = input('Director = ')
        new_score = input('IMDB Score = ')
        new_url = input('URL = ')
        new_duration = input('Duration = ')
        new_casts = input('Casts = ')
        self.name = new_name
        self.director = new_director
        self.IMDB_scores = new_score
        self.url = new_url
        self.duration = new_duration
        self.casts = []
        cast = new_casts
        c = cast.split('-')
        for i in range(len(c)):
            actor  = Actor.Actor(c[i].strip())
            self.casts.append(actor)
    
    def getDuration(self):
        return self.duration
    
    def getQrcode(self):
        qr = self.name + ':' + self.url
        return qr