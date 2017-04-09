user_dict = {
}

user_dict[1]={
    "username": "bartkim0426",
    "password": "1111",
    "email": "bartkim0426@gmail.com",
    "user_id": 1,
}

def login():

    username = input("id를 입력하세요:")
    password = input("password를 입력하세요:")

    for user in user_dict.values():
        if user.get('username')!=username:
            print('id가 없습니다')
            login()
        else:
            if user.get('password')==password:
                print('환영합니다, {username}님!'.format(username=username))
            else:
                print('비밀번호가 틀렸습니다.')
                login()

login()
