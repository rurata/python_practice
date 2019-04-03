def change():
    while True:
        allchange={"quarters":0,"dimes":0,"nickels":0,"pennies":0}
        changeval={"quarters":0.25,"dimes":0.10,"nickels":0.05,"pennies":0.01}
        #total=float(input("How much change required?  "))
        try:
            price,money=input("Enter price, then cash received:  ").split()
            price=float(price)
            money=float(money)
            total=money-price
            if (total < 0.0):
                print("Not enough cash!!")
                continue
            for key,val in sorted(allchange.items(), key=lambda x: x[1],reverse=True):
                allchange[key]=int((100.*total)//(100.*changeval[key]))
                total=0.01*round((100.*total)%(100.*changeval[key]))
            print(allchange)
        except:
            print("Wrong number of inputs")
            qq=input("Quit program? y/n: ")
            if (qq.lower() in ["y","yes"]):
                exit()
            else:
                continue

    
    
if __name__ == '__main__':
    change()