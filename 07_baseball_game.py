import random

# 정답 숫자 생성: 서로 다른 숫자 3개
answer = random.sample(range(1, 10), 3)

print("숫자 야구 게임 시작!")
print("1~9 사이의 서로 다른 숫자 3개를 입력하세요.")
print("예: 123")

count = 0

while True:
    user_input = input("숫자 입력: ")

    # 입력값 검사
    if len(user_input) != 3:
        print("3자리 숫자를 입력하세요.")
        continue

    if not user_input.isdigit():
        print("숫자만 입력하세요.")
        continue

    user_numbers = list(map(int, user_input))

    if 0 in user_numbers:
        print("0은 사용할 수 없습니다.")
        continue

    if len(set(user_numbers)) != 3:
        print("서로 다른 숫자를 입력하세요.")
        continue

    count += 1

    strike = 0
    ball = 0

    # 스트라이크, 볼 계산
    for i in range(3):
        if user_numbers[i] == answer[i]:
            strike += 1
        elif user_numbers[i] in answer:
            ball += 1

    print(f"{strike} 스트라이크, {ball} 볼")

    # 정답 조건
    if strike == 3:
        print(f"정답입니다! {count}번 만에 맞혔습니다.")
        break