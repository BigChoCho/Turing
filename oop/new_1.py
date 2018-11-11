#幣值轉換程序
#Ask the user to input $ and assign it io the $ variable

dollar = input ('Enter dollars')#輸入美元，與前章不同，在這邊除了要你輸入，同時系統向你問問題

#Convert form string to integer

dollar = int(dollar) #這邊幫你把字元轉換成數字

#Peroform calculation by mutiplying 30.48 times $
TD = dollar * 30.48  #這邊是把你的 dollar 轉換為TD

#Print results using format()

print('{}$ dollars equals {}TW Yuan ' .format(dollar,TD))   #{}=你後面的dollar跟你的TW幣

