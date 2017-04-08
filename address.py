def make_address(name, email, phone, address):
    id_list = list(address_example.keys())
    if id_list==[]:
        id = 1
    else:
        biggest_id = max(id_list)
        id = biggest_id + 1
    address_example[id] = {}

    address_example[id]["name"]=name,
    address_example[id]["email"]=email,
    address_example[id]["phone"]=phone,
    address_example[id]["address"]=address,

    return print('주소록에 추가되었습니다.')

def read_address():
    for i in address_example.keys():
        print(i)
        for x, y in address_example.get(i).items():
            print(x, ":", y[0])

def delete_address(id):
    name = address_example.get(id).get('name')
    del address_example[id]
    print("주소록에서 {name}님이 삭제되었습니다.".format(name=name))

first_input = int(input(
"""
원하는 기능 번호를 입력하세요
1. 주소록 읽기
2. 주소록 생성
3. 주소록 삭제
"""
))

if first_input==1:
    read_address()
elif first_input==2:
    name = input(
    """
    이름:
    """
    )
    email = input(
    """
    이메일:
    """
    )
    phone = input(
    """
    전화번호:
    """
    )
    address = input(
    """
    주소:
    """
    )
    make_address(name, email, phone, address)
else:
    read_address()
    delete_input = input(
    """
    삭제하고 싶은 주소록 번호를 입력하세요:
    """
    )
    delete_address(id)
