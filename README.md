# 🏧 ATM Management System (Python)

A simple command-line **ATM Management System** built using Python. This project simulates basic ATM operations such as user authentication, cash withdrawal, cash deposit, and balance inquiry.

## 📌 Features

- 🔐 User authentication using Account Number and PIN
- 💰 Withdraw money
- 💵 Deposit money
- 📊 Check account balance
- 🚪 Exit the application
- ✅ Withdrawal allowed only in multiples of ₹500

## 🛠️ Technologies Used

- Python 3
- Command Line Interface (CLI)

## 📂 Project Structure

```
ATM-Management-System/
│── atm.py        # Main Python program
│── README.md     # Project documentation
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/ATM-Management-System.git
```

2. Navigate to the project folder

```bash
cd ATM-Management-System
```

3. Run the Python file

```bash
python atm.py
```

## 🔑 Default Login Credentials

| Account Number | PIN |
|---------------|-----|
| `112233` | `1234` |

## 📋 Available Options

```
======= OPTIONS ========
1. Withdraw Money
2. Deposit Money
3. Check Balance
4. Exit
```

## 💡 Example

```
Enter Account No: 112233
Enter PIN: 1234

======= OPTIONS ========
1. Withdraw Money
2. Deposit Money
3. Check Balance
4. Exit

Select option: 1
Enter amount to withdraw: 5000

₹5000 withdrawn successfully.
Available Balance: ₹95000
```

## ⚙️ Program Logic

- The user enters an account number and PIN.
- If the credentials are correct, the ATM menu is displayed.
- Users can:
  - Withdraw money (only in multiples of ₹500)
  - Deposit money
  - Check the available balance
  - Exit the program
- If incorrect credentials are entered, access is denied.

## 🚀 Future Improvements

- Multiple user accounts
- PIN change feature
- Transaction history
- Data storage using files or databases
- Receipt generation
- Admin dashboard
- Account creation
- Password masking
- GUI version using Tkinter or PyQt

## 📸 Sample Output

```
Enter Account No: 112233
Enter PIN: 1234

======= OPTIONS ========
1. Withdraw Money
2. Deposit Money
3. Check Balance
4. Exit

Select option: 3
Available Balance: ₹100000
```

## 📖 Learning Objectives

This project helps beginners understand:

- Variables
- Conditional statements (`if-else`)
- Loops (`while`)
- User input (`input()`)
- Functions like `print()`
- Basic banking logic
- Menu-driven programs

---

⭐ If you found this project helpful, consider giving it a **star** on GitHub!
