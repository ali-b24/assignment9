class kasr:

    def __init__(self , n , d):
        self.numerator = n
        self.denomirator = d


    
    def sum(self , guest):
        result = kasr(None , None)
        result.numerator = self.numerator * guest.denomirator + self.denomirator * guest.numerator
        result.denomirator = self.denomirator * guest.denomirator
        return result 

    def mul(self , guest):
        result = kasr(None , None)
        result.numerator = self.numerator * guest.numerator
        result.denomirator = self.denomirator * guest.denomirator
        return result
    
    def sub(self , guest):
        result = kasr(None,None)
        result.numerator = self.numerator * guest.denomirator - self.denomirator * guest.numerator
        result.denomirator = self.denomirator * guest.denomirator
        return result
    
    def dev(self , guest):
        result = kasr(None , None)
        result.numerator = self.numerator / guest.numerator
        result.denomirator = self.denomirator / guest.denomirator
        return result



    def show(self):
        print(self.numerator, '/' , self.denomirator)




print("fraction 1:")
a = kasr(3,5)
a.show()
print("fraction 2:")
b = kasr(4,3)
b.show()


sum = a.sum(b)
print("sum: " , end='')
sum.show()

mul = a.mul(b)
print("mul: " , end='')
mul.show()

sub = a.sub(b)
print("sub:" , end='')
sub.show()

dev = a.dev(b)
print("dev:" , end='')
dev.show()