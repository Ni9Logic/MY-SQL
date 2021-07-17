while True:
    num = input("Please enter a number ")
    try:
        val = int(num)
        print("Input is an integer number.")
        print("Input number is: ", val)
        break;
    except ValueError:
        try:
            float(num)
            print("Input is an float number.")
            print("Input number is: ", val)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")