"""점수에 따라 등급을 알려 주는 조건문 예제입니다."""


def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main():
    try:
        score = int(input("점수(0~100)를 입력하세요: "))
    except ValueError:
        print("숫자를 입력해 주세요.")
        return

    if 0 <= score <= 100:
        print(f"등급은 {get_grade(score)}입니다.")
    else:
        print("점수는 0부터 100 사이여야 합니다.")


if __name__ == "__main__":
    main()
