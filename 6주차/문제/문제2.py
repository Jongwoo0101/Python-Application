# 10x10 극장 좌석을 초기화
seats = []
for _ in range(10):
    seats.append([0]*10)

# 좌석 배치를 출력하는 함수
def displayBookings():
    print("======================================")
    print("   0 1 2 3 4 5 6 7 8 9")  # 열 번호 출력
    print("======================================")
    for idx, row in enumerate(seats):
        print(f"{idx} {row}")  # 행 번호와 좌석 배열 출력
    print("")

# 좌석 예약을 처리하는 함수
def reserve():
    while True:
        try:
            # 좌석 배치표 출력
            displayBookings()

            # 사용자에게 행 번호와 열 번호 입력받기
            row = int(input("원하시는 좌석의 행 번호를 입력하세요 (0~9): "))
            col = int(input("원하시는 좌석의 열 번호를 입력하세요 (0~9): "))

            # 범위 체크
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue

            # 이미 예약된 좌석이면 메시지를 출력하고 다시 입력 받음
            if seats[row][col] == 1:
                print("이미 예약된 자리입니다. 다시 선택해주세요.")
            else:
                # 예약 가능한 좌석이면 예약 처리
                seats[row][col] = 1
                print("예약되었습니다!")
                displayBookings()

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

# 예약 함수 실행
reserve()
