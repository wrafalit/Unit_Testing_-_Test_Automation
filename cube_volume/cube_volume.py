def cub_volume(l):
    return l*l*l

length = [2, 1.1, -2.5,  2j, 'two']

for i in range(len(length)):
    print('The volume of cube is:',cub_volume(length[i]))