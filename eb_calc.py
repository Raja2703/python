unit=int(input('Enter the amount of units consumed:'))

def eb_calc(unit):

    if unit<=100:
        amt=0
        print('Free of cost')

    elif unit>=101 and unit<=200:
        rate_1=1.5
        subsidy=20
        rem_units=unit-100
        amt=(rem_units*rate_1)+subsidy

    elif unit>=201 and unit<=500:
        rate_1=2
        rate_2=3
        subsidy=30
        rem_units=unit-200
        amt=(100*rate_1)+(rem_units*rate_2)+subsidy
    
    elif unit>=501:
        rate_1=3.5
        rate_2=4.6
        rate_3=6.6
        subsidy=50
        rem_units=unit-500
        amt=(100*rate_1)+(300*rate_2)+(rem_units*rate_3)+subsidy

    print('Amount to be paid = Rs',amt)

eb_calc(unit)

