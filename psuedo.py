"""
display user message
while user wants to continue
    get monthly investment, int rate, and years
    convert yearly intereset rate to monthly interest rate
    convert years to months
    set the future value to zero
    for each month
        add monthly investment amount to future value
        calculate interest for month
        add interest to future value
    display future value 
    ask if the user wants to continue
display end message
"""
def main():
    print("The to the Future Value Calculator")
    print("===========================")

    choice = "y"
    while choice.lower() == "y":
        #get the input
        monthly_invest = float(input("Enter the Monthly Investment:\t\t "))
        yearly_intrest_rate = float(input("Enter the Yearly Investment Rate:\t "))
        years = int(input("Enter the number of years:\t\t "))

        #convert yearly to monthly
        monthly_intrest_rate = yearly_intrest_rate/12/100 #/100 to get a percent
        months = years*12

        #calc the future value
        future_value = 0
        for i in range(months):
            future_value += monthly_invest 
            monthly_intrest_amount = future_value * monthly_intrest_rate
            future_value += monthly_intrest_amount
        #display
        print("Future value:\t\t\t\t" + str(round(future_value,2 )))
        print()

        choice= input("Enter (y/n): ")
        print()

    print("Bye!")        

if __name__ == "__main__":
    main()
