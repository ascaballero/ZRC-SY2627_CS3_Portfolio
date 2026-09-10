# ZRC-SY2627_CS3_Portfolio


year = int(input("Enter your birth year: "))

if year < 1900:
    print("Invalid year, it should not be earlier than 1900 :) ")
else:
    zodiac = year % 12

    if zodiac == 4:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)!!")
    elif zodiac == 5:
        print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)!!")
    elif zodiac == 6:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)!!")
    elif zodiac == 7:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)!!")
    elif zodiac == 8:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)!!")
    elif zodiac == 9:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)!!")
    elif zodiac == 10:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)!!")
    elif zodiac == 11:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)!!")
    elif zodiac == 0:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)!!")
    elif zodiac == 1:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)!!")
    elif zodiac == 2:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)!!")
    elif zodiac == 3:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")


-----------------------------------------
class Hero:
    def __init__(self, name, hp):
       self.name = name
       self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

maria = Hero("Maria", 100)
cocoraz = Hero("Cocoraz", 100)
maria.take_damage(10)

print(maria.name, maria.hp)     # Expected: 90
print(cocoraz.name, cocoraz.hp)    # Expected: 100

#this is pisay



