import time

print ("文字を入れないでください")
tenthousand = int(input('1万円札の持っている数: '))
fivethousand = int(input('五千円札の持っている数: '))
twothousand = int(input('二千円札の持っている数: '))
onethousand = int(input('千円札の持っている数: '))
fivethundred = int(input('五百円玉を持っている数: '))
onehundred = int(input('百円玉を持っている数: '))
fifty = int(input('五十円玉の持っている数: '))
ten = int(input('十円玉の持っている数: '))
one = int(input('一円玉の持っている数: '))



tenthousand = (tenthousand*10000)
fivethousand = (fivethousand*5000)
twothousand = (twothousand*2000)
onethousand = (onethousand*1000)
fivethundred = (fivethundred*500)
onehundred = (onehundred*100)
fifty = (fifty*50)
ten = (ten*10)
one = one

#print (tenthousand+fivethousand+onethousand+fivethundred+onehundred+fifty+ten+one)#ok
print (tenthousand+fivethousand+onethousand+fivethundred+onehundred+fifty+ten+one+twothousand)


time.sleep(10)
