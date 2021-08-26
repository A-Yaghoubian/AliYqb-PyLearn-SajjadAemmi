class Kasr():
    
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m
        
    def sum(self, mehman):
        result = Kasr(None, None)
        result.soorat = (self.soorat * mehman.makhraj) + (self.makhraj * mehman.soorat)
        result.makhraj = self.makhraj * mehman.makhraj
        return result
    
    def sub(self, mehman):
        result = Kasr(None, None)
        result.soorat = (self.soorat * mehman.makhraj) - (self.makhraj * mehman.soorat)
        result.makhraj = self.makhraj * mehman.makhraj
        return result
    
    def mul(self, mehman):
        result = Kasr(None, None)
        result.soorat = self.soorat * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result
    
    def div(self, mehman):
        result = Kasr(None, None)
        result.soorat = self.soorat * mehman.makhraj
        result.makhraj = self.makhraj * mehman.soorat
        return result
    
    def show(self):
        print(self.soorat, '/', self.makhraj)

s_1 = int(input('soorat kasr aval = '))
m_1 = int(input('makhraj kasr aval = '))

s_2 = int(input('soorat kasr dovom = '))
m_2 = int(input('makhraj kasr dovom = '))

    
a = Kasr(s_1, m_1)
b = Kasr(s_2, m_2)

c = a.sub(b)
c.show()