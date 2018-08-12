def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' +secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            return (f.readline().strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

#使用列表打印sarah的成绩
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))


#使用字典获取成绩
sarah = get_coach_data('sarah2.txt')
sarah_d = {}
sarah_d['Name'] = sarah.pop(0)
sarah_d['DOB'] = sarah.pop(0)
sarah_d['Times'] = sarah
print(sarah_d['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_d['Times']]))[0:3]))


#换个方式（自己写的）
sarah_data = dict()  #也可以用sarah = {}
sarah_data = {'Name': get_coach_data('sarah2.txt')[0], 'Dob': get_coach_data('sarah2.txt')[1], 'Times': get_coach_data('sarah2.txt')[2:]}
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))