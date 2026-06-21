"""정해진 숫자를 맞히는 반복문 예제입니다."""

SECRET_NUMBER = 7


def main():
    print("1부터 10 사이의 숫자를 맞혀 보세요!")
    attempts = 0

    while True:
        try:
            guess = int(input("예상 숫자: "))
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        attempts += 1

        if guess < SECRET_NUMBER:
            print("조금 더 큰 숫자입니다.")
        elif guess > SECRET_NUMBER:
            print("조금 더 작은 숫자입니다.")
        else:
            print(f"정답입니다! {attempts}번 만에 맞혔습니다.")
            break


if __name__ == "__main__":
    main()
