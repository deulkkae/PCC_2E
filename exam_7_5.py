def question_age():
    return int(input("나이가 어떻게 되세요?(숫자만 입력하세요, 종료하려면 0)"))

def judge_fee(age):
    if age == 0:
        return -1
    if 3 <= age < 12:
        print("요금 10달러입니다.")
    elif age >= 13:
        print("요금 15달러입니다.")
    return 0

if __name__ == "__main__":
    while True:
        end_point = judge_fee(question_age())
        if end_point == -1:
            break