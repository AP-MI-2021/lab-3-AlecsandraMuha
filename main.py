def read_list():
    '''
    functia citeste lista
    :return: lista citita
    '''
    lst = []
    lst_str = input('Dați numerele : ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst
