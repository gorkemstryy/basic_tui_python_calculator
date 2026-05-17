def calc():
        u = int(input("first number..:"))
        r = int(input("second number..:"))
        procsess = input("which one; +,-,*,/,//,**")
        if procsess =="+":
                print(u+r)
        elif procsess =="-":
                print(u-r)
        elif procsess=="*":
                print(u*r)
        elif procsess=="/":
                print(u/r)
        elif procsess=="//":
                print(u//r)
        elif procsess=="**":
                print(u**r)
        else:
                print("Please select one of the procsesses...")

calc()