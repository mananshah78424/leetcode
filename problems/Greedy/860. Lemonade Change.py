

def lemonadeChange(bills):
    fives=0
    tens=0
    for i in bills:
        if i == 5:
            fives+=1
        elif i==10:
            if fives==0:
                return false
            fives-=1
            tens+=1
        else:
            if(tens and fives):
                tens-=1
                fives-=1
            elif(fives>3):
                fives-=1
            else:
                return false

    return true

bills = [5,5,10,10,20]
print(lemonadeChange(bills))