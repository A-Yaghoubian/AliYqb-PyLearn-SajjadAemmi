import Media

class Film(Media.Media):
    
    def __init__(self, class_name, class_director, class_score, class_url, class_duration, class_casts, class_genre, class_year):
        super().__init__(class_name, class_director, class_score, class_url, class_duration, class_casts)
        self.genre = class_genre
        self.year = class_year
        
    def showInfo(self):
        super().showInfo()
        print('Genre: ', self.genre)
        print('Year: ', self.year)
        
    def edit(self):
        super().edit()
        new_genre = input('Genre = ')
        new_year = input('Year = ')
        self.genre = new_genre
        self.year = new_year