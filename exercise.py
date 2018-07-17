def who():
    names = input("Enter names of people you know seperated by comma: ")
    return list(names.split(','))
   
def ask():
    name = who()
    inq = input("Enter the person you know: ")
    if inq in name: 
        print("You know {}!".format(inq))
    else:
        print("You don't know {}".format(inq))

ask()