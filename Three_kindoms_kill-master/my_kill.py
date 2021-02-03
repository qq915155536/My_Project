#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/27 13:34
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_kill.py
#  ===========================
'''使用类与对象实现简易三国杀游戏'''
import time
import numpy as np
from random import shuffle


# 玩家类
class player():
    def __init__(self, player_name):
        self.life = 3
        self.name = player_name
        self.handcard = []

    # 摸牌
    def get_card(self, deck):
        self.handcard.append(deck.card_list[0])
        deck.remove_card()

    # 出牌
    def play_card(self, card_index):
        self.handcard.pop(card_index)

    # 展示手牌
    def display_handcard(self):
        for card in self.handcard:
            print(card.display_card())


# 牌类
class card():
    def __init__(self, index, color, name):
        self.index = index
        self.color = color
        self.name = name

    def display_card(self):
        return '[%s - %s - %s]' % (self.color, self.index, self.name)


# 基础牌堆
class deck():
    def __init__(self):
        self.card_list = []

    def append_card(self, card):
        return self.card_list.append(card)

    def remove_card(self):
        return self.card_list.pop(0)

    def display_all_cards(self):
        for card in self.card_list:
            print(card.display_card())


# 花色
color_list = ['红桃♥', '方块♦', '梅花♣', '黑桃♠']  # [红桃♥，方块♦，梅花♣，黑桃♠]
# 牌号
num_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# 牌名
card_name_list = ['杀', '闪', '药']  # [杀，闪，药]

# 生成牌堆
game_deck = deck()

for col in color_list:
    for num in num_list:
        new_card = card(num, col, '')
        game_deck.append_card(new_card)

shuffle(game_deck.card_list)
for i in range(35):
    game_deck.card_list[i].name = '杀'

for i in range(35, 45):
    game_deck.card_list[i].name = '闪'

for i in range(45, 52):
    game_deck.card_list[i].name = '药'

shuffle(game_deck.card_list)
game_deck.display_all_cards()
time.sleep(2)

# 初始化玩家
player_list = []
player_name = ['玩家1', '玩家2', '玩家3']
for pl in player_name:
    new_player = player(pl)
    for i in range(2):
        new_player.get_card(game_deck)
    player_list.append(new_player)

print('>>>>>>>>游戏开始!!!<<<<<<<<')
time.sleep(2)

while (len(player_list) > 1):
    for player in player_list:
        print('-----%s(%s生命)开始出牌！-----' % (player.name, player.life))
        time.sleep(2)

        # 摸牌阶段
        for i in range(2):
            player.get_card(game_deck)
        time.sleep(2)

        # 出牌阶段
        while (True):
            player.display_handcard()
            choice = int(input('请输入您想出的牌:\n'))
            if choice == -1:
                print('%s 结束出牌阶段.\n' % (player.name))  # 结束他的出牌阶段
                time.sleep(2)
                break
            else:
                if player.handcard[choice].name == '杀':
                    choose_player = int(input('请输入您想攻击的玩家:\n'))
                    player.play_card(choice)

                    flag = 0
                    for i in range(len(player_list[choose_player].handcard)):
                        if player_list[choose_player].handcard[i].name == '闪':
                            player_list[choose_player].play_card(i)
                            print('%s 闪!\n' % (player_list[choose_player].name))
                            flag = 1
                            break

                    if flag == 0:
                        print('%s 失去一点生命\n' % (player_list[choose_player].name))
                        player_list[choose_player].life -= 1

                        if player_list[choose_player].life == 0:
                            print('%s死亡!' % (player_list[choose_player].name))
                            player_list.pop(choose_player)
                            if (len(player_list) == 1):
                                break
                            time.sleep(2)

                    time.sleep(2)

                elif player.handcard[choice].name == '药':
                    if player.life >= 3:
                        print('你血量满值!\n')
                    else:
                        player.play_card(choice)
                        player.life += 1
                        print('%s 血量+1!\n' % (player.name))
                    time.sleep(2)

                else:
                    print('您不能主动出闪!\n')
                    time.sleep(2)

        # 弃牌阶段
        exceed_card = len(player.handcard) - player.life
        if exceed_card > 0:
            print('你需要弃掉 %d 张手牌' % (exceed_card))
            player.display_handcard()
            for i in range(exceed_card):
                discard = int(input('请选择你想弃掉的牌'))
                player.play_card(discard)

            time.sleep(2)

        # 结束阶段
        print(' %s还有手牌:\n' % (player.name))
        player.display_handcard()
        time.sleep(2)

        print('----- %s结束出牌-----\n\n' % (player.name))
        time.sleep(3)

# 输出胜利信息
print('%s获胜!' % (player_list[0].name))
