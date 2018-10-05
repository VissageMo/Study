number = 23
guess = int(input('Enter an integer : ')) # input 函数用来获得输入量

if guess == number:
    print('Congratulations, you gussed it.')
    print('but you do not win any prizes!')

elif guess < number:
    print('No, it is a litter higher than that')

else:
    print('No, it is a litter lower than that')

print("Done")