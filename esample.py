class Building:
    klass_var = 45
    @staticmethod
    def structure(cls):
        print('this is a structure', cls.klass_var)



class Home(Building):
    @staticmethod
    def structure(a):
        print("This is the home", a, "and this is the building", Home.klass_var)


obj = Home()
obj.structure(1)