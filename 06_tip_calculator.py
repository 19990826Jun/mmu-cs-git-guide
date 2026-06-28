"""함수를 나누어 작성하는 팁 계산기 예제입니다."""


def calculate_tip(amount, tip_rate):
    return amount * tip_ratae / 100


def main():
    try:
        amount = float(input("결제 금액: "))
        tip_rate = float(input("팁 비율(%): "))
        tip = calculate_tip(amount, tip_rate)
    except ValueError:
        print("오류: 숫자를 입력해 주세요.")
        return

    print(f"팁 금액: {tip:g}원")
    print(f"총 금액: {amount + tip:g}원")


if __name__ == "__main__":
    main()
