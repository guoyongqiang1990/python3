def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' +secs)

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self, time):
        self.times.append(time)         #append 加列表，是把整个列表作为最后一项添加到列表末尾
    def add_times(self, times):
        self.times.extend(times)        #extend 加列表，是把两个列表有序连接

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
        return (Athlete(data.pop(0), data.pop(0), data))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

if __name__ == '__main__':
    james = get_coach_data('james2.txt')
    julie = get_coach_data("julie2.txt")
    mikey = get_coach_data('mikey2.txt')
    sarah = get_coach_data('sarah2.txt')
    print(james.name + "'s fastest time s are: " + str(james.top3()))
    print(julie.name + "'s fastest time s are: " + str(julie.top3()))
    print(mikey.name + "'s fastest time s are: " + str(mikey.top3()))
    print(sarah.name + "'s fastest time s are: " + str(sarah.top3()))

    A = Athlete('a')
    A.add_time('1.31')
    print(A.top3())
    A.add_times(['3.22', '3:31'])
    print(A.top3())