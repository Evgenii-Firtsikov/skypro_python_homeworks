class User:
    def __init__(self, first_name, last_name):
        print('Привет')
        self.first_name = first_name
        self.last_name = last_name

    def firstName(self):
        print('Меня зовут', self.first_name)

    def lastName(self):
        print('Моя фамилия', self.last_name)

    def lName_fName(self):
        print(f'Меня зовут и величают {self.first_name} {self.last_name}')
