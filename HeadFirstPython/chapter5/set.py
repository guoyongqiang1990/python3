def sanitize(time_string):   #创建函数，转换数据格式
    if '-' in time_string:
        splitter = '-'
        #(mins, secs) = time_string.split(splitter)
    elif ":" in time_string:
        splitter = ':'
        #(mins, secs) = time_string.split(splitter)
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):      #创建函数读取数据
    try:
        with open(filename) as f:
            return (f.readline().strip().split(","))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(sorted(set(sanitize(t) for t in james))[0:3])
print(sorted(set(sanitize(t) for t in julie))[0:3])
print(sorted(set(sanitize(t) for t in mikey))[0:3])
print(sorted(set(sanitize(t) for t in sarah))[0:3])
