class time:
    def __init__(self , h , m , s):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self, guest):
        result = time(None , None , None)
        result.hour = self.hour + guest.hour
        result.minute = self.minute + guest.minute
        result.second = self.second + guest.second
        if result.second >= 60 :
            result.second-=60
            result.minute+=1
        if result.minute >= 60 :
            result.minute-=60
            result.hour+=1     
        return result
    
    def sub(self , guest):
        result = time(None , None , None)
        result.hour = self.hour - guest.hour
        result.minute = self.minute - guest.minute
        result.second = self.second - guest.second
        if result.second < 0 :
            result.second+=60
            result.minute-=1
        if result.minute < 0 :
            result.minute+=60
            result.hour-=1     
        return result

    def SecondToTime(self):
        result = time(None , None , None)
        result.hour = self // 3600
        result.minute = (self % 3600) // 60
        result.second = (self % 3600) % 60
        return result


    def TimeToSecond(self):
        result = (self.hour *3600) + (self.minute *60) + (self.second)
        return result
    
    def show(self):
        print(self.hour ,":", self.minute ,":", self.second )
    


print("Time 1:")
a = time(3,5,5)
a.show()
print("Time 2:")
b = time(11,33,57)
b.show()

c = 5000
print("default second:" ,'\n',c)

sum = a.sum(b)
print("sum: " , end='')
sum.show()

sub = a.sub(b)
print("sub:" , end='')
sub.show()


timetosecond1 = a.TimeToSecond()
print("Time to second Time 1:" , '\n' ,timetosecond1 )

timetosecond2 = b.TimeToSecond()
print("Time to second Time 2:" , '\n', timetosecond2) 

secondtotime = time.SecondToTime(c)
print("default Second to Time:")
secondtotime.show()