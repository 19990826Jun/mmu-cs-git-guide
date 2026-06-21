"""이름을 입력받아 인사하는 가장 간단한 예제입니다."""


def main():
    name = input("이름을 입력하세요: ").strip()

    if name:
        print(f"안녕하세요, {name}님!")
        print("Git 실습에 오신 것을 환영합니다.")
    else:
        print("이름을 입력하지 않았습니다.")


if __name__ == "__main__":
    main()
    