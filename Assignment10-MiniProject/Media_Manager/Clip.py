import Media

class Clip(Media.Media):
    
    def __init__(self, class_name, class_director, class_score, class_url, class_duration, class_casts, class_subject):
        super().__init__(class_name, class_director, class_score, class_url, class_duration, class_casts)
        self.subject = class_subject
    
    def showInfo(self):
        super().showInfo()
        print('Subject: ', self.subject)
    
    def edit(self):
        super().edit()
        new_subject = input('Subject = ')
        self.subject = new_subject