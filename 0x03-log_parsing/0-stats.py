#!/usr/bin/python3
rep = True
cpt = 0
somme_file_size = 0
while (rep):
    try:
        x = input()
        cpt += 1
        somme_file_size += int(x.split(' ')[-1])
        if cpt == 10:
            print ('File size: ', somme_file_size)
            cpt = 0
            somme_file_size = 0
        else:
            print(x.split(" ")[-2])
    except KeyboardInterrupt:
        print ('File size:')
        rep = False
