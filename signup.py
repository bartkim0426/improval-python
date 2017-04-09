user_dict = {}

def signup():
    print('환영합니다. 회원가입 페이지입니다.')
    username = input(
    """
    id:
    """
    )
    password = input(
    """
    password:
    """
    )
    email = input(
    """
    email:
    """
    )

    id_list = list(user_dict.keys())
    if id_list==[]:
        user_id = 1
    else:
        biggest_id = max(id_list)
        user_id = biggest_id + 1

    user_dict[user_id] = {}

    user_dict[user_id]["username"] = username
    user_dict[user_id]["password"] = password
    user_dict[user_id]["eail"] = email

    print("{username}님의 회원가입이 완료되었습니다.".format(username=username))

signup()
