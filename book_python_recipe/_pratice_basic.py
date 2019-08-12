"""
# 다음 데이터를 리스트와 딕셔너리를 사용하여 작성하시오
# id  name              email           hp_num
# 1   hong kildong      hong@mail.com   010-2343-9870
# 2   lee soonsin       lee@mail.com    010-3333-5555
# 3   jeong youngsil    jang@mail.com   010-7777-1234
# 4   king sejong       king@mail.com   010-4567-0987
#
"""
# print(__doc__)

list_dict = [
    {
        'id': 1,
            'name': 'hong kildong',
            'email': 'hong@mail.com',
            'hp_num': '010-2343-9870',
    }, {
        'id': 2, 'name':
            'lee soonsin',
            'email': 'lee@mail.com',
            'hp_num': '010-3333-5555',
    }, {
        'id': 3,
            'name': 'jeong youngsil',
            'email': 'jang@mail.com',
            'hp_num': '010-7777-1234',
    }, {
        'id': 4,
            'name': 'king sejong',
            'email': 'king@mail.com',
            'hp_num': '010-4567-0987',
    }
]

[print(f'{key} --> {list_dict[0][key]}') for key in list_dict[0]]
