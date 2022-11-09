
import Train
import random
player=Train.Train()
quit=0
day=1
while (quit==0):
    print(str.format("Day {}",day))
    day=day+1
    print(str.format("You have {}$ in funds",player.funds))
    print(str.format("You have {} passengers going to Town A",player.townAPassengers))
    print(str.format("You have {} passengers going to Town B",player.townBPassengers))
    print(str.format("You have {} lbs of iron",player.iron))
    print(str.format("You have {} lbs of produce",player.produce))
    print(str.format("You are at location {}",player.locations[player.position]))
    if player.position==0:
        print("A - The Mines (you are here)        ")               
        print("B - Town A                          A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B                              F---G")
        print("G - The Farms                       ")
        print("")
        ironPrice=10+random.randrange(0,11)
        ironAmount=random.randrange(1,6)
        purchasePrice=ironAmount*ironPrice
        testInput=0
        while testInput==0:
            answer=input(str.format("Would you like to buy {} lbs of iron for {}$ Yes or No: ",ironAmount,purchasePrice))
            if (answer=="Yes") or (answer=="No"): 
                testInput=1
        if (answer=="Yes"):
            if player.funds >= purchasePrice:
                print(str.format("You purchased {} lbs of iron",ironAmount))
                player.funds=player.funds-purchasePrice
                player.iron=player.iron+ironAmount
            else:
                print("You cannot afford the iron")
        else:
            print("You did not buy any iron")
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go B or C: ")
            if (answer=="B") or (answer=="C"): 
                testInput=1
        if answer=="B":
            player.position=1
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="C":
            player.position=2
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))

    elif player.position==1:
        print("A - The Mines                       ")
        print("B - Town A (You are here)           A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B                              F---G")
        print("G - The Farms                       ")
        print("")
        passengerPrice=player.townAPassengers*2
        print(str.format("{} passengers from Town B get off the train. You make {}$ from ticket sales",player.townAPassengers,passengerPrice))
        player.funds=player.funds+passengerPrice
        passengerBoarding=random.randrange(0,11)+random.randrange(0,11)+random.randrange(0,11)
        print(str.format("{} passengers board your train they want to go to Town B",passengerBoarding))
        player.townBPassengers=player.townBPassengers+passengerBoarding
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go A or D: ")
            if (answer=="A") or (answer=="D"): 
                testInput=1
        if answer=="A":
            player.position=0
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="D":
            player.position=3
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))

    elif player.position==2:
        print("A - The Mines                       ")
        print("B - Town A                          A---B")
        print("C - The Market (You are here)       |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B                              F---G")
        print("G - The Farms                       ")
        print("")
        producePrice=5+random.randrange(0,4)
        sellPrice=producePrice*player.produce
        print(str.format("You sold {} lbs of produce to The Market for {}$",player.produce,sellPrice))
        player.produce=0
        player.funds=player.funds+sellPrice
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go A or D: ")
            if (answer=="A") or (answer=="D"): 
                testInput=1
        if answer=="A":
            player.position=0
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="D":
            player.position=3
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        
    elif player.position==3:
        print("A - The Mines                       ")
        print("B - Town A                          A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard (You are here)   C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B                              F---G")
        print("G - The Farms                       ")
        print("")
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go B,C,E,or F: ")
            if (answer=="B") or (answer=="C") or (answer=="E") or (answer=="F"): 
                testInput=1
        if answer=="B":
            player.position=1
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="C":
            player.position=2
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="E":
            player.position=4
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="F":
            player.position=5
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
    elif player.position==4:
        print("A - The Mines                       ")
        print("B - Town A                          A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory (You are here)          |   |")
        print("F - Town B                              F---G")
        print("G - The Farms                       ")
        print("")
        ironPrice=15+random.randrange(0,16)
        sellPrice=ironPrice*player.iron
        print(str.format("You sold {} lbs of iron to The Factory for {}$",player.iron,sellPrice))
        player.iron=0
        player.funds=player.funds+sellPrice
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go D or G: ")
            if (answer=="G") or (answer=="D"): 
                testInput=1
        if answer=="G":
            player.position=6
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="D":
            player.position=3
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        
    elif player.position==5:
        print("A - The Mines                       ")
        print("B - Town A                          A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B (You are here)               F---G")
        print("G - The Farms                       ")
        print("")
        passengerPrice=player.townBPassengers*2
        print(str.format("{} passengers from Town A get off the train. You make {}$ from ticket sales",player.townBPassengers,passengerPrice))
        player.funds=player.funds+passengerPrice
        passengerBoarding=random.randrange(0,11)+random.randrange(0,11)+random.randrange(0,11)
        print(str.format("{} passengers board your train they want to go to Town A",passengerBoarding))
        player.townAPassengers=player.townAPassengers+passengerBoarding
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go D or G: ")
            if (answer=="A") or (answer=="D"): 
                testInput=1
        if answer=="G":
            player.position=6
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="D":
            player.position=3
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
    elif player.position==6:
        print("A - The Mines                       ")
        print("B - Town A                          A---B")
        print("C - The Market                      |   |")
        print("D - The Train Yard                  C---D---E")
        print("E - The Factory                         |   |")
        print("F - Town B                              F---G")
        print("G - The Farms (You are here)   ")
        print("")
        producePrice=3+random.randrange(0,3)
        produceAmount=random.randrange(1,11)
        purchasePrice=produceAmount*producePrice
        testInput=0
        while testInput==0:
            answer=input(str.format("Would you like to buy {} lbs of produce for {}$ Yes or No: ",produceAmount,purchasePrice))
            if (answer=="Yes") or (answer=="No"): 
                testInput=1
        if (answer=="Yes"):
            if player.funds >= purchasePrice:
                print(str.format("You purchased {} lbs of produce",produceAmount))
                player.funds=player.funds-purchasePrice
                player.produce=player.produce+produceAmount
            else:
                print("You cannot afford the produce")
        else:
            print("You did not buy any produce")
        testInput=0
        while testInput==0:
            answer=input("Where would you like to go E or F: ")
            if (answer=="F") or (answer=="E"): 
                testInput=1
        if answer=="F":
            player.position=5
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))
        elif answer=="E":
            player.position=4
            print(str.format("You have spent 10$ of funds to travel to {}",player.locations[player.position]))

    player.funds=player.funds-10
    if player.funds<0:
        quit=1
        print("You have ran out of money")
print("Thanks for playing")
    


        
        