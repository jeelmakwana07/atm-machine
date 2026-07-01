default_acc_no = "112233"
default_pin = "1234"

avl_bal = 100000
is_verified = False
flag = True

avl_opt = """
======= OPTIONS ========
1. Withdraw Money
2. Deposit Money
3. Check Balance
4. Exit
"""

# Enter account details
acc_no = input("Enter Account No: ")
pin = input("Enter PIN: ")

if acc_no == default_acc_no and pin == default_pin:
    is_verified = True
else:
    print("Invalid credentials")

if is_verified:

    while flag:
        print(avl_opt)

        opt = int(input("Select option: "))

        if opt == 1:
            amt = int(input("Enter amount to withdraw: "))

            if amt <= avl_bal:
                if amt % 500 == 0:
                    avl_bal -= amt
                    print(f"₹{amt} withdrawn successfully.")
                    print(f"Available Balance: ₹{avl_bal}")
                else:
                    print("Only ₹500 notes are available.")
            else:
                print("Insufficient balance.")

        elif opt == 2:
            amt = int(input("Enter amount to deposit: "))
            avl_bal += amt
            print(f"₹{amt} deposited successfully.")
            print(f"Available Balance: ₹{avl_bal}")

        elif opt == 3:
            print(f"Available Balance: ₹{avl_bal}")

        elif opt == 4:
            print("Good Bye!")
            flag = False

        else:
            print("Invalid option")