class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):  # 손에 들고 있는 카드의 개수
        return self.N

    def addCard(self, c):  # 카드 추가
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        total_value = 0  # 카드의 총 값
        num_aces = 0  # 에이스의 수

        # 카드의 총 값 계산
        for card in self.cards:
            total_value += card.getValue()  # 카드의 값 더하기

            # 에이스의 수 세기
            if card.value == 1:
                total_value += 10
                num_aces += 1

        # 총 값이 21을 초과하고 에이스가 있는 경우 에이스 값을 조정
        while total_value > 21 and num_aces > 0:
            total_value -= 10  # 에이스 값을 11에서 1로 조정
            num_aces -= 1  # 조정된 에이스 수 감소

        return total_value
