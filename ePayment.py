x=0
while x==0:
    print("Welcome to the ePayment")
    print("Hit '1' to create an account")
    print("Hit '2' to login to existing account")
    print("Hit '3' to read T&C")
    main_head=input()
    if main_head=="1":
        print("Fill the Entire Details")
        print("Full Name: ")
        name=input()
        print("Email Address: ")
        email=input()
        print("Password: ")
        password=input()

        print("Congratulations!, you've successfully created an account of ePayment")
        print("Your Registration Details")
        print("Full Name: "+name)
        print("Email Address: "+email)
        print("Password: "+password)
        print("Go To Home")
        print("'y' or 'n'")
        home=input()
        if home=="y":
            x=0
        elif home=="n":
            x=1
    
    if main_head=='2':
        print("Enter Email Address And Password to Login")
        print("Email Address: ")
        email2=input()
        print("Password: ")
        password2=input()

        print("Welcome!"+email2)
        print("Hit '1' for Add Fund")
        print("Hit '2' for Withdraw")
        print("Hit '3' for Money Transfer")
        print("Hit '4' Sign Out")

        sub_head=input()

        if sub_head=="1":
            print("Add Fund to Your Account"+email2)
            print("Select Amount to Add:")
            print("'$10','$100','$1000'")
            print("Enter 10, 100, 1000 only")
            add_fund=input()

            if add_fund=="10":
                print("$10 successfully added to your account "+email2)
            elif add_fund=="100":
                print("$100 successfully added to your account "+email2)
            elif add_fund=="1000":
                print("$1000 successfully added to your account "+email2)
                
        if sub_head=="2":
            print("Withdraw Money from your account")
            print("Select Amount for Withdrawl:")
            print("'$100','$1000','$10000'")
            print("Enter 100, 1000, 10000 only")
            withdrawl=input()

            if withdrawl=="100":
                print("$100 Withdrawl...!!!")
            elif withdrawl=="1000":
                print("$1000 Withdrawl...!!!")
            elif withdrawl=="10000":
                print("$10000 Withdrawl...!!!")

        if sub_head=="3":
            print("Welcome to ePayment Secure Money Transfer Portal")
            print("Enter email to transfer money")
            email3=input()
            print("Select Amount to be Transferred")
            print("'$1000','$10000','$100000'")
            transfer=input()

            if transfer=="1000":
                print("$1000 has been successfully transfered to "+email3)
            elif transfer=="10000":
                print("$10000 has been successfully transferred to "+email3)
            elif transfer=="100000":
                print("$100000 has been successfully transferred to "+email3)

        if sub_head=="4":
            print("You've successfully Signed Out")
            print("Thankyou for using ePayment")

    if main_head=="3":
        print("Terms & Conditions")
        print("This is a test string,This is a test string,This is a test string,This is a test string,This is a test string,This is a test string,This is a test string,")
 
