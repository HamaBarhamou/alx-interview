#!/usr/bin/python3


def read() -> [bool, bool, str]:
    try:
        x = input()
        return [True, False, x]
    except KeyboardInterrupt:
        return [True, True, "error"]


rep = True
cpt = 0
somme_file_size = 0
dic = {}
rep = True
while (rep):
    rep, state_err, x = read()
    if state_err is False:
        x = input()
        cpt += 1
        somme_file_size += int(x.split(' ')[-1])
        if cpt == 10:
            print('File size:', somme_file_size)
            cpt = 0
            somme_file_size = 0
            for key, value in sorted(dic.items()):
                print(key, ":", value)
            dic = {}
        else:
            key = x.split(" ")[-2]
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
    else:
        print("hello on continue...")
