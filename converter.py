def convert_usd_to_krw(usd, exchange_rate=1350):
    """달러(USD)를 원화(KRW)로 변환하는 간단한 함수"""
    return usd * exchange_rate

def main():
    print("=== 간단한 환율 변환기 ===")
    try:
        usd_amount = float(input("변환할 달러(USD) 금액을 입력하세요: "))
        krw_amount = convert_usd_to_krw(usd_amount)
        
        print(f"\n💵 {usd_amount:,} USD")
        print(f"➡️ ₩ {krw_amount:,} KRW (적용 환율: 1,350원 기준)")
    except ValueError:
        print("올바른 숫자를 입력해주세요!")

if __name__ == "__main__":
    main()