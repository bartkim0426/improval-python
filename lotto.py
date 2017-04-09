import random

win_dict = {
    0: "꽝입니다",
    1: "꽝입니다",
    2: "꽝입니다",
    3: "꽝입니다",
    4: "축하드립니다, 4등입니다",
    5: "축하드립니다, 3등입니다",
    6: "축하드립니다, 1등입니다",
    7: "축하드립니다, 2등입니다",
}

def lotto():

    win_list = random.sample(range(1, 47), 7)
    random.shuffle(win_list)
    bonus_num = win_list.pop()

    user_num = input(
    """
    로또 번호 6개를 순차적으로 입력하세요 (1~46):
    """
    )
    user_bonus_num = int(input(
    """
    보너스 번호를 입력하세요 (1~46):
    """
    ))

    user_list = list(map(int, user_num.split()))
    print("""
    당첨번호는 {win_list}, 보너스 번호는 {bonus_num}
    선택번호는 {user_list}, 보너스 번호는 {user_bonus_num} 입니다!
    """.format(
        win_list=win_list,
        user_list=user_list,
        bonus_num=bonus_num,
        user_bonus_num=user_bonus_num,
    ))
    win_count = 0
    for x in user_list:
        user_num = x
        if user_num in win_list:
            win_count += 1
            print("{num} matching!".format(num=user_num))

    if win_count == 5:
        if user_bonus_num == bonus_num:
            print("bonus number matching")
            win_count += 2

    print(win_dict.get(win_count))

lotto()
