def introduce_myself():
    # 자기소개 정보를 딕셔너리에 저장
    profile = {
        "이름": "홍길동",
        "직업": "개발자",
        "관심사": ["파이썬", "데이터 분석", "독서"],
        "좌우명": "어제보다 나은 오늘",
    }

    print("=== 자기소개서 ===")
    print(f"안녕하세요! 저는 {profile['이름']}입니다.")
    print(f"현재 {profile['직업']}로 활동하고 있습니다.")
    print(f"저의 관심사는 {', '.join(profile['관심사'])}입니다.")
    print(f"저의 좌우명은 '{profile['좌우명']}'입니다.")
    print("==================")


if __name__ == "__main__":
    introduce_myself()
