from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random
from Configuration import *


class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0

        self.playerMoney = 1000
        self.Table = []
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.LcardsTable = []
        self.deckN = 0
        self.setMoney()
        self.round = 0
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))

        self.window.mainloop()

    def setMoney(self):
        self.betMoney +=10
        self.playerMoney -=10
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))




    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Betx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedBetx1)
        self.Betx1.place(x=150, y=500)
        self.Betx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedBetx2)
        self.Betx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)

        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'


    def setupLabel(self):
        self.LbetMoney = Label(text="$0", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=500, y=550)

        self.LplayerPts = Label(text="", width=10, height=1, font=self.fontstyle2, bg="green", fg="orange")
        self.LplayerPts.place(x=400, y=350)
        self.LdealerPts = Label(text="", width=10, height=1, font=self.fontstyle2, bg="green", fg="orange")
        self.LdealerPts.place(x=400, y=100)
        self.LTablePts = Label(text="", width=6, height=2, font=self.fontstyle2, bg="green", fg="blue")
        self.LTablePts.place(x=600, y=200)

        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=600, y=200)

    def setupDeck(self):
        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0
        self.player.N=0
        self.dealer.N=0
        self.hitPlayer(0)
        self.hitDealerDown(0)
        self.hitPlayer(1)
        self.hitDealerDown(1)
        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Betx1['state'] = 'active'
        self.Betx1['bg'] = 'white'
        self.Betx2['state'] = 'active'
        self.Betx2['bg'] = 'white'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'


    def pressedCheck(self):
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Betx1['state'] = 'disabled'
        self.Betx1['bg'] = 'gray'
        self.Betx2['state'] = 'disabled'
        self.Betx2['bg'] = 'gray'
        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"
        PlaySound('sounds/chip.wav', SND_FILENAME)

    def pressedBetx1(self):

        dealMoney = self.betMoney
        self.betMoney += self.betMoney

        if dealMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= dealMoney
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Betx1['state'] = 'disabled'
            self.Betx1['bg'] = 'gray'
            self.Betx2['state'] = 'disabled'
            self.Betx2['bg'] = 'gray'
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= dealMoney

    def pressedBetx2(self):
        dealMoney = self.betMoney
        self.betMoney += dealMoney * 2

        if 2 * dealMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= dealMoney * 2
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Betx1['state'] = 'disabled'
            self.Betx1['bg'] = 'gray'
            self.Betx2['state'] = 'disabled'
            self.Betx2['bg'] = 'gray'
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= dealMoney * 2

    def pressedDeal(self):
        if self.betMoney > 0:
            if self.round == 0:
                self.setupDeck()
            self.deal()


    def pressedAgain(self):
        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Betx1['state'] = 'active'
        self.Betx1['bg'] = 'white'
        self.Betx2['state'] = 'active'
        self.Betx2['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        self.LplayerMoney.configure(text="$" + str(self.playerMoney))
        self.betMoney = 0
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.Lstatus.configure(text="")
        self.round =0

        for i in range(self.player.inHand()):
            self.LcardsPlayer[i].destroy()
        self.LcardsPlayer.clear()
        self.player.cards.clear()
        self.LplayerPts.configure(text="")

        for i in range(self.dealer.inHand()):
            self.LcardsDealer[i].destroy()
        self.LcardsDealer.clear()
        self.dealer.cards.clear()
        self.LdealerPts.configure(text="")

        for i in range(5):
            self.LcardsTable[i].destroy()
        self.LcardsTable.clear()
        self.Table.clear()
        self.LTablePts.configure(text="")

        self.setMoney()



    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))

        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 80, y=50)

    def deal(self):
        if self.round != 0:
            if len(self.Table) == 0:
                for i in range(3):
                    newCard = Card(self.cardDeck[self.deckN])
                    self.deckN += 1
                    self.Table.append(newCard)
                    p = PhotoImage(file="cards/" + newCard.filename())
                    self.LcardsTable.append(Label(self.window, image=p))

                    # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
                    self.LcardsTable[i].image = p
                    self.LcardsTable[i].place(x=200 + i * 80, y=200)
                    self.LTablePts.configure()
            else:
                newCard = Card(self.cardDeck[self.deckN])
                self.deckN += 1
                self.Table.append(newCard)
                p = PhotoImage(file="cards/" + newCard.filename())
                self.LcardsTable.append(Label(self.window, image=p))

                # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
                self.LcardsTable[len(self.Table) - 1].image = p
                self.LcardsTable[len(self.Table) - 1].place(x=200 + (len(self.Table) - 1) * 80, y=200)
                self.LTablePts.configure()

            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

        print(self.round)
        if self.round == 3:
            self.checkWinner()
        else:
            self.Check['state'] = 'active'
            self.Check['bg'] = 'white'
            self.Betx1['state'] = 'active'
            self.Betx1['bg'] = 'white'
            self.Betx2['state'] = 'active'
            self.Betx2['bg'] = 'white'

            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'

        self.round += 1

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + n * 80, y=350)
        self.LplayerPts.configure()
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        p = PhotoImage(file="cards/" + self.dealer.cards[1].filename())
        self.LcardsDealer[1].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[1].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        Win_Lose = Configuration()
        player_score = Win_Lose.score(self.player.cards, self.Table)
        dealer_score = Win_Lose.score(self.dealer.cards, self.Table)

        self.LplayerPts.configure(text=str(Win_Lose.hand_ranking[player_score]), font=("Arial", 20, "bold"))
        self.LdealerPts.configure(text=str(Win_Lose.hand_ranking[dealer_score]), font=("Arial", 20, "bold"))

        # 승리 기준

        if player_score == 0 and dealer_score == 0:
            player_card1 = self.player.cards[0].value
            dealer_card1 = self.dealer.cards[0].value
            player_card2 = self.player.cards[1].value
            dealer_card2 = self.dealer.cards[1].value

            # 최댓값 구하기
            max_value = max(player_card1, dealer_card1, player_card2, dealer_card2)

            # 최댓값이 플레이어의 카드인지 확인
            if max_value in [player_card1, player_card2]:
                player_score+=100
        if player_score > dealer_score:
            self.LTablePts.configure(text="WIN", font=("Arial", 40, "bold"))
            self.playerMoney += self.betMoney*2
        elif player_score < dealer_score:
            self.LTablePts.configure(text="LOSE", font=("Arial", 40, "bold"))
        else:
            self.LTablePts.configure(text="DRAW", font=("Arial", 40, "bold"))
            self.playerMoney += self.betMoney


        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


BlackJack()
