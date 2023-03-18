##자판기##
import random
import time
money = random.randint(1, 50)
money = money * 100
re, end, rell = 0, 0, 0
def sp(n):
    for i in range(0, n):
        print()
def nm(sm, text):
    global money
    global re
    global end
    global choice
    if money < int(sm):
        if money != 0:
            print("\033[38;5;9m" + "남은 돈: 0")
            sp(1)
            money = 0
            time.sleep(3)
            print("남은 돈은 반환되지 않습니다." + "\033[0m")
            ##자판기 가 빡친듯 하다. (왜지?)##
            end = 1
        else:
            print("\033[38;5;9m" + "남은 돈: 0")
            sp(1)
            money = 0
            time.sleep(3)
            print("\033[38;5;9m" + "돈이 없는데 어떻게 음료를 살까요?" + "\033[0m")
            end = 1
    else:
        if choice == "k":
            print("뭐가 나올까요..!")
            input("[결과를 보려면 Enter를 누르세요.]")
            sp(1)
        money = money - sm
        print(text)
        print("남은 돈: %s" %money)
        input("[자판기로 돌아가려면 Enter를 누르세요.]")
        sp(1)
        re = re + 1
sp(1)
while end == 0:
    print("음료를 선택하세요.")
    print("   [음료 목록]")
    print("   a: 제주 삼다수(1500원)")
    print("   b: 비타 500(800원)")
    print("   c: 박카스(800원)")
    print("   d: 칠성 사이다(1000원)")
    print("   e: 코카 콜라(1300원)")
    print("   f: 펩시 콜라(1300원)")
    print("   g: 솔의 눈(1200원)")
    print("   h: 포카리 스웨트(1500원)")
    print("   i: 데자와(1200원)")
    print("   j: 쌕쌕 오렌지(800원)")
    print("   k: 행운의 뽑기칸!(1000원)")
    print(" x: 구매 종료")
    sp(1)
    print("남은 돈: %s" %money)
    choice = input("어떤 음료를 사겠습니까?: ")
    sp(1)
    if choice == "a":
        nm(1500, "제주 삼다수를 마셨다! 역시 음료는 근-본을 마셔야 해!")
    elif choice == "b":
        nm(800, "비타 500을 마셨다! 카페인이 없어서 좀 더 건강한 느낌이다!")
    elif choice == "c":
        nm(800, "박카스를 마셨다! 카페인이 있어 잠이 확 깨는 느낌이다!")
    elif choice == "d":
        nm(1000, "칠성 사이다를 마셨다! 캬~ 청량하다!")
    elif choice == "e":
        nm(1300, "코카 콜라를 마셨다! 탄산이 강한게 일품이다!")
    elif choice == "f":
        nm(1300, "펩시 콜라를 마셨다! 달달구리한게 일품이다!")
    elif choice == "g":
        nm(1200, "솔의 눈을 마셨다! 정말 머리까지 시원해지는 민트향이다!")
    elif choice == "h":
        nm(1500, "포카리 스웨트를 마셨다! 음료는 역시 이온음료!")
    elif choice == "i":
        nm(1200, "데자와를 마셨다! 뭔가.. 일반 밀크티보다 풍미있는 것 같다!")
    elif choice == "j":
        nm(800, "쌕쌕 오렌지를 마셨다! 새콤한 오렌지향을 맡아본지가 얼마나 오렌지!")
    elif choice == "k":
        al_bet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        al_bet = random.choice(al_bet)
        if al_bet == "a":
            nm(1000, "제주 삼다수를 마셨다! 역시 음료는 근-본을 마셔야 해!")
        elif al_bet == "b":
            nm(1000, "비타 500을 마셨다! 카페인이 없어서 좀 더 건강한 느낌이다!")
        elif al_bet == "c":
            nm(1000, "박카스를 마셨다! 카페인이 있어 잠이 확 깨는 느낌이다!")
        elif al_bet == "d":
            nm(1000, "칠성 사이다를 마셨다! 캬~ 청량하다!")
        elif al_bet == "e":
            nm(1000, "코카 콜라를 마셨다! 탄산이 강한게 일품이다!")
        elif al_bet == "f":
            nm(1000, "펩시 콜라를 마셨다! 달달구리한게 일품이다!")
        elif al_bet == "g":
            nm(1000, "솔의 눈을 마셨다! 정말 머리까지 시원해지는 민트향이다!")
        elif al_bet == "h":
            nm(1000, "포카리 스웨트를 마셨다! 음료는 역시 이온음료!")
        elif al_bet == "i":
            nm(1000, "데자와를 마셨다! 뭔가.. 일반 밀크티보다 풍미있는 것 같다!")
        elif al_bet == "j":
            nm(1000, "쌕쌕 오렌지를 마셨다! 새콤한 오렌지향을 맡아본지가 얼마나 오렌지!")
    elif choice == "x":
        if re == 0 and money < 800:
            print("현명하신 선택입니다..")
        print("이용해 주셔서 감사합니다.")
        end = 1
    else:
        rell = rell + 1
        if rell == 5:
            print("장난 치지마세요;;")
            input("[자판기로 돌아가려면 Enter를 누르세요.]")
            sp(3)
        elif rell == 10:
            time.sleep(3)
            print("\033[38;5;9m" + "장난치지 말라고요." + "\033[0m")
            ##이건 솔직히 빡칠만 했어;;##
            input("[자판기로 돌아가려면 Enter를 누르세요.]")
            sp(3)
        elif rell > 10:
            end = 1
        else:
            print("죄송하지만 주문을 잘못하신것 같은데..")
            print("다시 주문해주세요!")
            input("[자판기로 돌아가려면 Enter를 누르세요.]")
            sp(3)