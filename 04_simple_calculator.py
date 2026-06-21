"""함수를 나누어 작성하는 간단한 계산기 예제입니다."""


def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return first / second
    raise ValueError("지원하지 않는 연산자입니다.")


def main():
    try:
        first = float(input("첫 번째 숫자: "))
        operator = input("연산자(+, -, *, /): ").strip()
        second = float(input("두 번째 숫자: "))
        result = calculate(first, operator, second)
    except ValueError as error:
        print(f"오류: {error}")
        return

    print(f"계산 결과: {result:g}")


if __name__ == "__main__":
    main()
    