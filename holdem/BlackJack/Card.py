class Card:
    # 클래스Card
    def __init__(self, number):  # 랜덤 넘버 number = 0..51 값 인자로 전달

        self.value = number % 13 + 1  # 1,2,...13 (13가지 숫자)
        self.x = number // 13  # 0..51 // 13 -> 0,1,2,3 무늬(suit)

    def getValue(self):  # 1,2,3,4,5,6,7,8,9,10 -> 원래 숫자, J,Q,K -> 10
        if self.value > 10:
            # J,Q,K 인 경우
            return 10
        else:
            # 1,2,...10
            return self.value

    def getsuit(self):  # self.x 에 따라서 카드 무늬를 반환하는 함수
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']  # 카드 무늬 리스트
        return suits[self.x]  # 4 문자열 중에서 self.x 문자열 반환

    def filename(self):  # 랜덤넘버 number =0..51 에서 file name 반환
        return self.getsuit() + str(self.value) + '.png'
