class Athlete:
    def __init__(self, value=0):
        self.thing = value
    def how_big(self):
        self.len = len(self.thing)
        return (self.len)
    #The code to initialize a "Athlete" object.



a = Athlete("Holy Grail")   #python 会将目标标识符赋至self参数，so，实际上是执行 Athlete.__init__(a, "Holy Grail") self是对象实例！！
print(a.how_big())          #此句实际上是Athlete.how_big(a)
print(a.thing)

class athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

sarah = athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = athlete('James Jones')
print(type(sarah))
print(type(james))
print(sarah)
print(james)
print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)