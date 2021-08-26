class myTime():
    
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        
    def sum(self, mehman):
        result = myTime(None, None, None)
        
        result.second = self.second + mehman.second
        result.minute = self.minute + mehman.minute
        result.hour = self.hour + mehman.hour
        
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
            
        return result
    
    def sub(self, mehman):
        result = myTime(None, None, None)
        
        if self.second >= mehman.second:
            result.second = self.second - mehman.second
        else:
            self.second += 60
            self.minute -= 1
            result.second = self.second - mehman.second
        
        if self.minute >= mehman.minute:
            result.minute = self.minute - mehman.minute
        else:
            self.minute += 60
            self.hour -= 1
            result.minute = self.minute - mehman.minute
        
        result.hour = self.hour - mehman.hour
        if result.hour < 0:
            result.hour += 24
        
        return result
    
    def timetosec(self):
        result = myTime(None, None, None)
        result.hour = 0
        result.minute = 0
        result.second = self.second + self.minute * 60 + self.hour * 3600
        return result
    
    def sectotime(self):
        result = myTime(None, None, None)
        
        result.hour = self.second // 3600
        self.second %= 3600

        result.minute = self.second // 60
        self.second %= 60

        result.second = self.second
        
        return result
    
    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

h_1 = int(input('Hour(1) = '))
m_1 = int(input('Minute(1) = '))
s_1 = int(input('Second(1) = '))

h_2 = int(input('Hour(2) = '))
m_2 = int(input('Minute(2) = '))
s_2 = int(input('Second(2) = '))

    
a = myTime(h_1, m_1, s_1)
b = myTime(h_2, m_2, s_2)

c1 = a.sum(b)
c1.show()

c2 = a.sub(b)
c2.show()

c3 = a.timetosec()
c3.show()

c4 = c3.sectotime()
c4.show()