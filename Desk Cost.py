def getDetails():
    name = str(input("Enter Your name"))
    print("Name:" , name)
    number_of_orders = int(input("Enter The amount of orders"))
    print("Number of orders:", number_of_orders)
    count = 0
    length2 = []
    width2 = []
    nu_drawers = []
    wood = []
    while count < number_of_orders:
        length = int(input("Enter the length of the desk"))
        width = int(input("Enter your width of the desk"))
        length2.append(length)
        width2 .append(width)
        wood_types = ["mahogany" , "pine" , "oak" , "maple" , "cherry"]
        type_of_wood = str(input("Enter your type of wood"))
        if type_of_wood in wood_types:
            print("Valid Type of Wood")
            
        else:
            while type_of_wood not in wood_types:
                type_of_wood = str(input("Please enter a valid type of wood"))
        number_of_drawers = int(input("Enter the number of drawers"))
        nu_drawers.append(number_of_drawers)
        count = count + 1
        wood.append(type_of_wood)
    return length2 , width2 , number_of_orders , wood , nu_drawers

def getCalculations():
    length2 , width2 , no_orders , type_of_wood1 , number_of_drawers1 = getDetails()
    count = 0
    charge = 200
    data2 = []
    while count < no_orders:
        
        square_inches = length2[0]*width2[0]
        del length2[0]
        del width2[0]
        if square_inches >= 750:
            charge = charge + 50
        if type_of_wood1[0] == "mahogony":
                charge = charge + 150
        elif type_of_wood1[0] == "oak":
            charge_total = charge + 125
        else:
        del type_of_wood1[0]
        charge_t =(charge + (number_of_drawers1[0]*30))
        data2.append((charge_t))
        count = count + 1
        total_price = sum(data2)
    print("Total Charge:" , total_price)
        

getCalculations()
                     
        
        
                
            
    
    
        
            
            


    
    









