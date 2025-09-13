#----------------------------------Decorators------------------------------------------------
def example(func):
    def wrapper(username):
        print('verifying username..')
        process = func(username)
        print(f'{username} have successfully completed {process}!!')
    return wrapper

@example
def register(username):
    print('registration processing...')
    return 'Registration'

@example
def login(username):
    print('login processing...')
    return 'Login'

register('John Doe')
print()
login('Harry')


#-------------------------------------Inheritance-----------------------------------------------
'''Single Inheritance'''

class Bird:
    def intro(self, name):
        print(f'My name is {name},I am a bird!!')

class Parrot(Bird):
    pass

c1 = Parrot()
c1.intro('Parrot')

'''Multi Level Inheritance'''

class Animal:
    def properties(self, type):
        print(f'{type} is also an Animal!!')

class Bird(Animal):
    def intro(self, name):
        print(f'My name is {name},I am a bird!!')

class Parrot(Bird):
    pass

c1 = Parrot()
c1.properties('Bird')
c1.intro('Parrot')

'''Multiple Inheritance'''

class Bird:
    def fly(self, name):
        print(f'My name is {name},I am a bird ---> I can fly ',end='and also ')

class Human:
    def Talk(self):
        print(f'I can Talk')

class Parrot(Bird, Human):
    pass

c1 = Parrot()
c1.fly('Parrot')
c1.Talk()

'''Hierarchical Inheritance'''

class Bird:
    def intro(self, name):
        print(f'My name is {name} and I am a Bird!!')

class Parrot(Bird):
    pass

class Sparrow(Bird):
    pass

class pigeon(Bird):
    pass

c1 = Parrot()
c1.intro('Parrot')

c2 = Sparrow()
c2.intro('Sparrow')

c3 = pigeon()
c3.intro('Pigeon')

'''Hybrid Inheritance'''

class Bird:
    def Intro(self, name):
        print(f'My name is {name} and I am a Bird!!')

class Human:
    def Talk(self):
        print(f'I can Talk')

class Sparrow(Bird):
    pass

class Parrot(Bird, Human):
    pass

c1 = Sparrow()
c1.Intro('Sparrow')
c2 = Parrot()
c2.Intro('Parrot')
c2.Talk()



