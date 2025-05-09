class Singelton:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


########## Run Code ##############
obj1 = Singelton()
obj2 = Singelton()

print(obj1 is obj2) 
print(obj1 == obj2)  