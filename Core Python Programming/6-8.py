# 6-8
# I use dictionary instead of list in this exercise

def num2english(n):
    num_dict = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        
        20:'twen',
        30:'thir',
        40:'for',
        
        '15_50':'fif',
        '18_80':'eigh',
        
        '<20':'teen',
        '>20':'ty',
        
        '100':' hundred',
        '1000':' thousand'
        }
    
    th = n / 1000
    hun = (n / 100) % 10
    ten = (n / 10) % 10
    ones = n % 10
    
    ten_ones = n % 100

    # print th, hun, ten, ones, ten_ones

    num_str = ''

    and_flag = False # flag for 'and' between thousand/hundred and tens or ones
    if th>0:
        num_str +=  num_dict[th] + num_dict['1000']
        and_flag = True
        
    if hun > 0:
        if th>0:
            num_str += ' '
        num_str += num_dict[hun] + num_dict['100']
        and_flag = True

    if ten > 1: # 20~99
        if and_flag:
            num_str += ' and '
        
        if ten==8:
            num_str += num_dict['18_80']
        elif ten==5:
            num_str += num_dict['15_50']
        elif ten==4:
            num_str += num_dict[40]
        elif ten==3:
            num_str += num_dict[30]
        elif ten==2:
            num_str += num_dict[20]
        else:
            num_str += num_dict[ten]
            
        num_str += num_dict['>20']  # 'ty'
        
        if ones!=0:
            num_str += '-' + num_dict[ones]
            
    elif ten_ones>13:   # 14 ~ 19
        if and_flag:
            num_str += ' and '
            
        if ten_ones == 15:
            num_str += num_dict['15_50']
        elif ten_ones == 18:
            num_str += num_dict['18_80']
        else:
            num_str += num_dict[ones]
            
        num_str += num_dict['<20']  # 'teen'
        
    elif ten_ones<=13 and ten_ones!=0:     # 1 ~ 13
        if and_flag:
            num_str += ' and '
            
        num_str += num_dict[ten_ones]
    else: # 0
        if th==0 and hun==0:
            num_str += num_dict[ten_ones]    # should be num_dict[0]
                
    print n,'==>',num_str


if __name__ == '__main__':
    for i in range(22):
        num2english(i)

    for i in [30, 31, 40, 41, 50, 51, 80, 81, 100, 101, 110, 120, 121, 199,
              200, 201, 210, 212, 219, 220, 345, 555, 1000, 1200,
              2345, 9999, 2015, 2016, 2001, 2030, 3000, 4320, 5005, 6606, 7074,
              8218, 9517]:
        num2english(i)
