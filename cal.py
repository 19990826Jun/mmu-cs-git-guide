def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "오류: 0으로 나눌 수 없어요"
    except Exception:
        return "오류: 잘못된 수식이에요"

print("=== 계산기 ===")
print("종료하려면 'q' 입력\n")

while True:
    expr = input("계산식 입력: ")
    if expr.lower() == 'q':
        print("종료!")
        break
    print(f"결과: {calculate(expr)}\n")