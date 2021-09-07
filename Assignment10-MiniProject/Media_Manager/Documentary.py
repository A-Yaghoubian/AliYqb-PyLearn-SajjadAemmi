import Media

class Documentary(Media.Media):
    
    def __init__(self, class_name, class_director, class_score, class_url, class_duration, class_casts, class_year):
        super().__init__(class_name, class_director, class_score, class_url, class_duration, class_casts)
        self.year = class_year
    
    def showInfo(self):
        super().showInfo()
        print('Year: ', self.year)
        
    def edit(self):
        super().edit()
        new_year = input('Year = ')
        self.year = new_year