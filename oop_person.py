class Person:
    pass

    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        interests_str = 'My interests are '
        for pos in range(len(self.interests)):
            if pos == len(self.interests) - 1:
                interests_str += 'and ' + self.interests[pos] + '.'
            else:
                interests_str += self.interests[pos] + ', ' 
        return 'Hello, my name is {} and I am {} years old. {}'.format(self.name, self.age, interests_str)

person = Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'])
greeting = person.hello()
print(greeting)