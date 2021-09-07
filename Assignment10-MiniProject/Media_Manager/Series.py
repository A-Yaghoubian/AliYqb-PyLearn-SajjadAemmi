import Media

class Series(Media.Media):
    
    def __init__(self, class_name, class_director, class_score, class_url, class_duration, class_casts, class_genre, class_season, class_episode):
        super().__init__(class_name, class_director, class_score, class_url, class_duration, class_casts)
        self.genre = class_genre
        self.season = class_season
        self.episode = class_episode
    
    def showInfo(self):
        super().showInfo()
        print('Genre: ', self.genre)
        print('Season: ', self.season)
        print('Episode: ', self.episode)
        
    def edit(self):
        super().edit()
        new_genre = input('Genre = ')
        new_season = input('Season = ')
        new_episode = input('Episode = ')
        self.genre = new_genre
        self.season = new_season
        self.episode = new_episode