class fizzBuzz:
    def __init__(self):
        super().__init__()
        self.play()
        
    def play(self):
        for i in range(1,100):
            if (i % 3) == 0 and (i % 5) == 0:
                print('{:} -- fizzbuzz'.format(i))
            elif (i % 3) == 0:
                print('{:} -- fizz'.format(i))
            elif (i % 5) == 0:
                print('{:} -- buzz'.format(i))
                
#-----------------------------------

if __name__ == '__main__':
    
    fizzbuzz = fizzBuzz()