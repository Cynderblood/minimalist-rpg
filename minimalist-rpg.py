import Player

count_slots = 3
player_slots = [None, None, None]


def Main_Menu():
    print('########################')
    print('####### Text Rpg #######')
    print('########################')
    print('1) Start')
    print('2) Exit')
    choose = int(input('>> '))
    if choose == 1:
        choose_slot()
        for i in player_slots:
            if i == 'curr':
                i = Player.Player('Test')
                i = i.pick_race()
                break
    elif choose == 2:
        pass

def choose_slot():
    while True:
        print('Choose character slot:')
        for i in range(1, count_slots + 1):
            print('{}) {}'.format(i, player_slots[i - 1]))
        choose = int(input('>> '))
        if choose >= 1 and choose <= count_slots:
            player_slots[choose - 1] = 'curr'
            break
        else:
            print('Write num from 1 to 3')
            continue

Main_Menu()