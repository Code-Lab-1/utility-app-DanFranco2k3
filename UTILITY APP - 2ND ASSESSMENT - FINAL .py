## The Startup ##
print("------------------------------- KABAYAN VENDING MACHINE ---------------------------")
print()
print(" ----------------- MABUHAY! THE VENDING MACHINE OF ALL FILIPINOS -----------------------")
print()
print(" ----------*** YOU MUST FIRST SELECT YOUR FOOD AND GET YOUR CHANGE IMMEDIATELY *** ---------")
print()
print("--------------*** THE MACHINE WILL ASK YOU IF YOU WANT A DRINK OR NOT ***------------------")
print()
print("--- *** IF YOU WANT A DRINK, THEN YOU SHOULD INSERT ANOTHER CREDIT FOR THE MACHINE TO BE USED *** ---")
print()
## The user will now insert money in this section
## If the user doesn't want food, the machine will still ask if the user wants a drink
def main():
        cart = []
        def order():
                credit_inserted = int(input("Please insert credit: "))
                if credit_inserted <=0:
                        print("Not Enough credit. Please try again.")
                        order()
                elif credit_inserted >=0: 
                        
                ## THE MENU OF THE FOOD, CHOOSE ONE AFTER INSERTING YOUR FIRST CREDIT ##
                        print()
                        print(" *** YOU MUST SELECT YOUR FOOD FIRST BEFORE YOU CAN SELECT YOUR DRINKS *** ")
                        print()
                        print("                            PLEASE CHOOSE YOUR MERIENDA                           ")
                        print()
                        print("""   [1] BIBINGKA = 14 AED     [2] MONAY = 3 AED     [3] PANDESAL = 2 AED   [4] SAPIN-SAPIN= 10 AED    [5] BIKO = 25 AED    [6] MURON = 15 AED

                                [7] PICHI-PICHI = 5 AED  [8] KUTSINTA = 3 AED    [9] SUMAN = 4.50 AED    [10] PUTO-BUMBONG =  3 AED     [11] PUTO = 7 AED       """)
                        print()
                        
## This is the list for the merienda that will inform the code what the user had chosen
                while True:
                        food = input("Please Enter the code below of the chosen merienda: \n")
                        foodv = {"1":"BIBINGKA",
                                "2":"MONAY",
                                "3":"PANDESAL",
                                "4":"SAPIN-SAPIN",
                                "5":"BIKO",
                                "6":"MURON",
                                "7":"PICHI-PICHI",
                                "8":"KUTSINTA",
                                "9":"SUMAN",
                                "10":"PUTO-BUMBONG",
                                "11":"PUTO",
                                } 
                        if food == '1' and credit_inserted >= 12:
                                print (foodv["1"])
                                cart.append(foodv.get('1'))
                                break
                        elif food == '2':
                                print (foodv["2"])
                                cart.append(foodv.get('2'))
                                break
                        elif food == '3':
                                print (foodv["3"])
                                cart.append(foodv.get('3'))
                                break
                        elif food == '4':
                                print (foodv["4"])
                                cart.append(foodv.get('4'))
                                break
                        elif food == '5':
                                print (foodv["5"])
                                cart.append(foodv.get('5'))
                                break
                        elif food == '6':
                                print (foodv["6"])
                                cart.append(foodv.get('6'))
                                break
                        elif food == '7':
                                print (foodv["7"])
                                cart.append(foodv.get('7'))
                                break
                        elif food == '8':
                                print(foodv["8"])
                                cart.append(foodv.get('8'))
                                break
                        elif food == '9':
                                print(foodv["9"])
                                cart.append(foodv.get('9'))
                                break
                        elif food == '10':
                                print(foodv["10"])
                                cart.append(foodv.get('10'))
                                break
                        elif food == '11':
                                print(foodv["11"])
                                cart.append(foodv.get('11'))
                                break
                        else:
                         print("I'm sorry, we don't have that unfortunately.")
                        break
                ## This is the part where the user will pay and the credit that is inserted will be deduce by the program
                print("Now time for payment.")
                prices ={"1" : 14,
                        "2" : 3,
                        "3" : 2,
                        "4" : 10,
                        "5" : 25,
                        "6" : 15,
                        "7" : 5,
                        "8" : 3,
                        "9" : 4.50,
                        "10" : 3,
                        "11" : 7,
                }
                while True:
                        ordered_food = food
                        if ordered_food == '1':
                                print((credit_inserted) - 14.00)
                                break
                        elif ordered_food == '2':
                                print((credit_inserted) - 3.00)
                                break
                        elif ordered_food == '3':
                                print((credit_inserted) - 2.00)
                                break
                        elif ordered_food == '4':
                                print((credit_inserted) - 10.00)
                                break
                        elif ordered_food == '5':
                                print((credit_inserted) - 25.00)
                                break
                        elif ordered_food == '6':
                                print ((credit_inserted) - 15.00)
                                break
                        elif ordered_food == '7':
                                ((credit_inserted) - 5.00)
                                break
                        elif ordered_food == '8':
                                ((credit_inserted) - 3.00)
                                break
                        elif ordered_food == '9':
                                print((credit_inserted) - 4.50)
                                break
                        elif ordered_food == '10':
                                print((credit_inserted) - 3.00)
                                break
                        elif ordered_food == '11':
                                print ((credit_inserted) - 7.00)
                                break
                        else:
                         print("No payment, given code is not in the menu. Please Try again.")
                        break
                ## If the user got his/her food, this will be displayed
                print()
                print("Thank you for using Kabayan vending, your change and order is now dispensing.")
                print()
                print("If you selected a food but didnt insert any credit, the machine will not dispense the selected food.")
                print()
        def drinks():
                ## The user should insert another credit if she/he wants to get a drink.
                while True:
                        drinks_vendo = str(input("Would you like to get a drink? Yes/No : "))
                        if drinks_vendo != 'Yes':
                                print()
                                print("Thank you for using Kabayan Vending Machine.")
                                print()
                                print("Your order and change is now dispensing.")
                                break
                        elif drinks_vendo == 'Yes':
                                bill_inserted = int(input("Please insert credit: "))
                                if bill_inserted <=0:
                                        print("Not Enough credit. Please try again.")
                                        break
                                        drinks()
                                print("""                                           
                                                                   PLEASE CHOOSE YOUR DRINKS                           """)
                                print()
                                print("""                                          
                                                                     *** COLD DRINKS ***
                                [1] WATER = 1 AED    [2] SPRITE = 3 AED   [3] DIET PEPSI = 3 AED   [4] DIET COKE = 5 AED  [5] COCA-COLA = 3 AED    [6] PEPSI = 5 AED  
                                                                   
                                                                      *** HOT DRINKS ***
                                7] LATTÉ = 10 AED   [8] ESPRESSO = 15 AED    [9] CAPUCCINO = 10 AED    [10] AMERICANO = 5 AED     [11] HOT CHOCOLATE = 3 AED        """)
                                print()
                                while True:
                                        drinksv ={"1":"WATER",
                                                "2":"SPRITE",
                                                "3":"DIET PEPSI",
                                                "4":"DIET COKE",
                                                "5":"COCA-COLA",
                                                "6":"PEPSI",
                                                "7":"LATTÉ",
                                                "8":"ESPRESSO",
                                                "9":"CAPUCCINO",
                                                "10":"AMERICANO",
                                                "11":"HOT CHOCOLATE",
                                                }
                                        drinks_question = int(input("What drink would you like? "))
                                        drink = drinks_question
                                        if drink == 1:
                                                print (drinksv["1"])
                                                cart.append(drinksv.get('1'))
                                                print()
                                                break
                                        elif drink == 2:
                                                print (drinksv["2"])
                                                cart.append(drinksv.get('2'))
                                                break
                                        elif drink == 3:
                                                print (drinksv["3"])
                                                cart.append(drinksv.get('3'))
                                                break
                                        elif drink == 4:
                                                print (drinksv["4"])
                                                cart.append(drinksv.get('4'))
                                                break
                                        elif drink == 5:
                                                print (drinksv["5"])
                                                cart.append(drinksv.get('5'))
                                                break
                                        elif drink == 6:
                                                print (drinksv["6"])
                                                cart.append(drinksv.get('6'))
                                                break
                                        elif drink == 7:
                                                print (drinksv["7"])
                                                cart.append(drinksv.get('7'))
                                               
                                                break
                                        elif drink == 8:
                                                print(drinksv["8"])
                                                cart.append(drinksv.get('8'))
                                                break
                                        elif drink == 9:
                                                print(drinksv["9"])
                                                cart.append(drinksv.get('9'))
                                                break
                                        elif drink == 10:
                                                print(drinksv["10"])
                                                cart.append(drinksv.get('10'))
                                                break
                                        elif drink == 11:
                                                print(drinksv["11"])
                                                cart.append(drinksv.get('11'))
                                                break
                                        else:
                                                break
                                                print("I'm sorry, we don't have that unfortunately.")
                                                break
                                while True:
                                        ordered_drinks = str(input("Please enter the code of the drink you want: "))
                                        if ordered_drinks == '1':
                                                print ((bill_inserted) -1.00)
                                                break
                                        elif ordered_drinks == '2':
                                                print ((bill_inserted)- 3.00)
                                                break
                                        elif ordered_drinks == '3':
                                                print ((bill_inserted)-3.00)
                                                break
                                        elif ordered_drinks == '4':
                                                print ((bill_inserted)- 5.00)
                                                break
                                        elif ordered_drinks == '5':
                                                print ((bill_inserted)-3.00)
                                                break
                                        elif ordered_drinks == '6':
                                                print  ((bill_inserted)- 5.00)
                                                break
                                        elif ordered_drinks == '7':
                                                print  ((bill_inserted)-10.00)
                                                break
                                        elif ordered_drinks == '8':
                                                print ((bill_inserted)- 15.00)
                                                break
                                        elif ordered_drinks == '9':
                                                print ((bill_inserted)-10.00)
                                                break
                                        elif ordered_drinks == '10':
                                                print ((bill_inserted)- 5.00) 
                                                break
                                        elif ordered_drinks == '11':
                                                print ((bill_inserted) -3.00)
                                                break
                                        else:
                                                break
                                                print("I'm sorry, we don't have that unfortunately.")
                                                break
                                else:
                                 print()
                                print(f"You ordered: {(cart)}")
                                print()
                                print("Thank you for using Kabayan Vending Machine.")
                                print()
                                print("Your order and change is now dispensing.")
                                print()
                                ## If you selected a drink, the drink will only dispense, the food will be displayed but not dispensed.
                                break
        order()
        drinks()
main()