def main():
    more = 'y'
    while more == 'y' or more == 'Y':
     print("\n\n\t\tCalculate the real cost of a meal, where ")
     print("\t\t tax is 7% and be nice to add 18% tip ")
     cost = float(input("\n\t\t\tMeal Cost: "))
     
     print("\n\t\t\t Meal : $ ", cost)
     tax = (cost * .07)
     print("\n\t\t\t  tax : $ ", format(cost * .07, '.2f'))
     tip = (cost * .18)
     print("\n\t\t\t  tip : $ ", format(cost * .18, '.2f'))
     print("\n\t\t\tTotal : $ ", format(tip + cost + tax, '.2f'))
                                    
        
   



     more = input ("\n\t\tDo more (Y/N) ? ")





main()
        
