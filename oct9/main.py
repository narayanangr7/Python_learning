def day_check(day):
    if type(day)==str:
        print("Invalid input")
    else:
        print("ok")

        match day:
            case 1:
                print("monday")
            case 2:
                print("Tuestday")
            case 4:
                print("wednesday")
            case 5:
                print("Thureday")
            case 6:
                print("friday")
            case 7:
                print("saterday")
            case _:
                print("Enter number between 1 and 7 only ")


#=====================================================================

