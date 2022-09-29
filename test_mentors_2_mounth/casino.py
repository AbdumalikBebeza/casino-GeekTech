import random


class Casino:
    balanse = 1000
    print(" ----------> добро пожаловать в казино GeekTech! <----------")
    print(f"ваш баланс = {balanse}$")

    def func_casino(self):
        while True:
            stavka = int(input("для выхода нажмите 'q'\n"
                               "выберите сумму ставки\n"))
            if stavka == "q":
                print("досвидания!")
                break
            elif stavka > self.balanse:
                print("у вас не достаточно денег")
                continue
            a = random.randint(1, 11)
            b = random.randint(10, 21)
            c = random.randint(20, 31)
            d = random.randint(30, 41)
            data = [a, b, c, d]
            print(data)
            ran = random.choice(data)
            user_num = int(input("выберите одно число из этого списка"))
            if user_num == ran:
                self.balanse += stavka
                print(f"вы выиграли - {stavka * 2}$ \n"
                      f"цифра казино - {ran}\n"
                      f"ваш баланс = {self.balanse}$")
            elif user_num != ran:
                self.balanse -= stavka
                print(f"вы проиграли - {stavka}$\n"
                      f"цифра казино - {ran}\n"
                      f"ваш баланс = {self.balanse}$")
            else:
                print("вы что то не правильно ввели")


casino = Casino()
casino.func_casino()
