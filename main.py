def read_list():
    '''
    Functie pentru citirea listei
    :return: lista citita
    '''
    lst = []
    lst_str = input('Dați numerele separate prin spațiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst
fwegweg