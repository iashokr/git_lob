class Demo:
    def __init__(self,acc_no,pin):
        self.__acc_no=acc_no
        self.__pin=pin

    def setter(self,acc_no,pin):
        self.__acc_no=acc_no
        self.__pin=pin
        print("hello")

    def getter(self):
        return self.__acc_no,self.__pin


d=Demo(190199,9076)
d.setter(899090,3421)
print(d.getter())