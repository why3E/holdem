from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random


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
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.deckN = 0
        self.window.mainloop()

    def setupButton(self):
        self.B50 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedB50)
        self.B50.place(x=50, y=500)
        self.B10 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedB10)
        self.B10.place(x=150, y=500)
        self.B1 = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedB1)
        self.B1.place(x=250, y=500)
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
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)

    def pressedB50(self):
        self.betMoney += 50

        if 50 <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 50
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 50

    def pressedB10(self):
        self.betMoney += 10

        if 10 <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 10
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 10

    def pressedB1(self):
        self.betMoney += 1

        if 1 <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 1
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1

    def pressedDeal(self):
        if self.betMoney > 0:
            self.deal()

    def pressedAgain(self):
        self.B50['state'] = 'active'
        self.B50['bg'] = 'white'
        self.B10['state'] = 'active'
        self.B10['bg'] = 'white'
        self.B1['state'] = 'active'
        self.B1['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        self.LplayerMoney.configure(text="$" + str(self.playerMoney))
        self.betMoney = 0
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.Lstatus.configure(text="")

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

    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))

        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 80, y=50)


    def deal(self):
        self.player.reset()
        self.dealer.reset()
        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer(0)
        self.hitDealerDown(0)
        self.hitPlayer(1)
        self.hitDealerDown(1)

        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

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

    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value() > 21:
            self.checkWinner()

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        self.LdealerPts.configure(text=str(self.dealer.value()))

       #승리 기준

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


BlackJack()
