class Configuration:
    RoyalStraightFlush = {1, 10, 11, 12, 13}
    BackStraightFlush = {1, 2, 3, 4, 5}

    hand_ranking = {
        12: 'Royal Straight Flush',
        11: 'Back Straight Flush',
        10: 'StraightFlush',
        9: 'Four Card',
        8: 'Full House',
        7: 'Flush',
        6: 'Mountain',
        5: 'Back Straight',
        4: 'Straight',
        3: 'Triple',
        2: 'Two Pair',
        1: 'One Pair',
        0: 'no Pair'
    }

    def score(self,cList, cCards):  # cList : 플레이어 카드 리스트, cCards : 커뮤니티 카드 리스트
        c = cList + cCards

        xd = {i: [] for i in range(4)}
        for i in range(7):
            xd[c[i].x].append(c[i].value)

        vd = {i: [] for i in range(1, 14)}
        for i in range(7):
            vd[c[i].value].append(c[i].x)

        if Configuration.scoreRoyalStraightFlush(xd): return 12
        elif Configuration.scoreBackStraightFlush(xd): return 11
        elif Configuration.scoreStraightFlush(xd): return 10
        elif Configuration.scoreFourCard(vd): return 9
        elif Configuration.scoreFullHouse(vd): return 8
        elif Configuration.scoreFlush(xd): return 7
        elif Configuration.scoreMountain(xd): return 6
        elif Configuration.scoreBackStraight(xd): return 5
        elif Configuration.scoreStraight(xd): return 4
        elif Configuration.scoreTriple(vd): return 3
        elif Configuration.scoreTwoPair(vd): return 2
        elif Configuration.scoreOnePair(vd): return 1
        else: return 0

    def scoreRoyalStraightFlush(xd):
        for k, v in xd.items():
            if len(v) >= 5:
                if len(set(v).intersection(Configuration.RoyalStraightFlush)) == 5:
                    return True
        return False

    def scoreBackStraightFlush(xd):
        for k, v in xd.items():
            if len(v) >= 5:
                if len(set(v).intersection(Configuration.BackStraightFlush)) == 5:
                    return True
        return False

    def scoreStraightFlush(xd):
        for k, v in xd.items():
            if len(v) >= 5:
                v.sort()
                for i in range(len(v) - 4):
                    if sum(v[i:i + 5]) == v[i] * 5 + 10:
                        return True
        return False


    def scoreFourCard(vd):
        for k, v in vd.items():
            if len(v) >= 4:
                return True
        return False

    def scoreFullHouse(vd):
        cnt = [len(v) for v in vd.values()]
        if 2 in cnt and 3 in cnt:
            return True
        return False

    def scoreFlush(xd):
        for k, v in xd.items():
            if len(v) >= 5:
                return True
        return False

    def scoreMountain(xd):
        l = []
        for k, v in xd.items():
            l += v
        if len(set(l).intersection(Configuration.RoyalStraightFlush)) == 5:
            return True
        return False

    def scoreBackStraight(xd):
        l = []
        for k, v in xd.items():
            l += v
        if len(set(l).intersection(Configuration.BackStraightFlush)) == 5:
            return True
        return False

    def scoreStraight(xd):
        l = []
        for k, v in xd.items():
            l += v
        l.sort()
        l = list(set(l))
        for i in range(len(l) - 4):
            if sum(l[i:i + 5]) == l[i] * 5 + 10:
                return True
        return False

    def scoreTriple(vd):
        for k, v in vd.items():
            if len(v) == 3:
                return True
        return False

    def scoreTwoPair(vd):
        cnt = 0
        for k, v in vd.items():
            if len(v) == 2:
                cnt += 1
            if cnt == 2:
                return True
        return False

    def scoreOnePair(vd):
        for k, v in vd.items():
            if len(v) == 2:
                return True
        return False
