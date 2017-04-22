import time

print ("文字を入れないでください")
money = int(input('あなたの持っているお金: '))

if money >= 10000:
    tenthousand = money//10000
    remains = money%10000
    tenthousandyen = tenthousand*10000
    money = remains
    onethousand = 0
    print ('一万円札',tenthousand,'枚')

if money >= 1000:
    onethousand = money//1000
    remains = money%1000
    money = remains
    print ('千円札',onethousand,'枚')

if money >= 500:
    fivethundred = money//500
    remains = money%500
    money = remains
    print ('五百円玉',fivethundred,'個')

if money >= 100:
    onehundred = money//100
    remains = money%100
    money = remains
    print ('百円玉',onehundred,'個')

if money >= 50:
    fifty = money//50
    remains = money%50
    money = remains
    print ('五十円玉',fifty,'個')

if money >= 10:
    ten = money//1
    remains = money%10
    money = remains
    print ('十円玉',ten,'個')

if money >= 1:
    one = money//1
    remains = money%1
    money = remains
    print ('一円玉',one,'個')



time.sleep(5)
