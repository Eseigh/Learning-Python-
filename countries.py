while True:
    print('Enter a number')

    print('1. India\t2. USA\n3. Nigeria\t4. France\n5.Japan\t6. China\n7. Exit')

    choice = int(input('Enter your choice:'))


    def switch(choice):
        def india():
            ind = India()
            print('India')
            print(ind)
            print(ind.capital())
            print(ind.language())
            print(ind.type())

        def usa():
            us = USA()
            print('USA')
            print(us)
            print(us.capital())
            print(us.language())
            print(us.type())

        def nigeria():
            nigeria = Nigeria()
            print('Nigeria')
            print(nigeria)
            print(nigeria.capital())
            print(nigeria.language())
            print(nigeria.type())

        def france():
            france = France()
            print('France')
            print(france)
            print(france.capital())
            print(france.language())
            print(france.type())

        def japan():
            japan = Japan()
            print('Japan')
            print(japan)
            print(japan.capital())
            print(japan.language())
            print(japan.type())

        def china():
            china = China()
            print('China')
            print(china)
            print(china.capital())
            print(china.language())
            print(china.type())

        if choice == 1:
            return switch(india())

        if choice == 2:
            return switch(usa())

        if choice == 3:
            return switch(nigeria())

        if choice == 4:
            return switch(france())

        if choice == 5:
            return switch(japan())

        if choice == 6:
            return switch(china())


class Continents(n):
    def __int__(self, n):
        self.name = n

    def continent(self):
        print(self.name)


class India(Continents('Asia')):
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA(Continents('North America')):
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


class Nigeria(Continents('Africa')):
    def capital(self):
        print("Abuja is the capital of Nigeria.")

    def language(self):
        print("English is the primary language of Nigeria.")

    def type(self):
        print("Nigera is a developing country.")


class France(Continents('Europe')):
    def capital(self):
        print("Paris is the capital of France.")

    def language(self):
        print("French is the primary language of France.")

    def type(self):
        print("France is a developed country.")


class Japan(Continents('Asia')):
    def capital(self):
        print("Tokyo is the capital of Japan.")

    def language(self):
        print("Japanese is the primary language of Japan.")

    def type(self):
        print("Japan is a developed country.")


class China(Continents('Asia')):
    def capital(self):
        print("Beijing is the capital of China.")

    def language(self):
        print("Chinese is the primary language of China.")

    def type(self):
        print("Japan is a developed country.")


obj_chi = China()
obj_jap = Japan()
obj_fra = France()
obj_nig = Nigeria()
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa, obj_nig, obj_fra, obj_jap, obj_chi):
    country.capital()
    country.language()
    country.type()
