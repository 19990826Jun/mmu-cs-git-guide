"""할 일을 텍스트 파일에 저장하고 읽는 예제입니다."""

from pathlib import Path

TODO_FILE = Path(__file__).with_name("todos.txt")


def show_todos():
    if not TODO_FILE.exists():
        print("등록된 할 일이 없습니다.")
        return

    todos = TODO_FILE.read_text(encoding="utf-8").splitlines()
    if not todos:
        print("등록된 할 일이 없습니다.")
        return

    print("\n[할 일 목록]")
    for number, todo in enumerate(todos, start=1):
        print(f"{number}. {todo}")


def add_todo():
    todo = input("새로운 할 일: ").strip()
    if not todo:
        print("내용을 입력해 주세요.")
        return

    with TODO_FILE.open("a", encoding="utf-8") as file:
        file.write(todo + "\n")
    print("할 일을 저장했습니다.")


def main():
    print("1. 목록 보기")
    print("2. 할 일 추가")
    choice = input("메뉴 선택: ").strip()

    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    else:
        print("올바른 메뉴 번호를 선택해 주세요.")


if __name__ == "__main__":
    main()