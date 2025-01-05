from tkinter import *

root = Tk()
root.title("ATM")
root.geometry("500x500+400+100")
root.overrideredirect(1)
root.config(bg="yellow")

balance = 1000  # Initial balance
pin = "2112"  # Example PIN for verification

def verify_pin(action):
    pin_window =  Toplevel(root)
    pin_window.title("Enter PIN")
    pin_window.geometry("500x500+400+100")
    pin_window.configure(bg="lightblue")
    pin_window.overrideredirect(1)

    labpin =  Label(pin_window, text="Enter your PIN:",font=("Impact", 18), bg="lightblue")
    labpin.pack(pady=100)
    pin_entry =  Entry(pin_window, font=("Impact", 18),show="*")
    pin_entry.pack(pady=5)
    error_label =  Label(pin_window, text="",font=("Impact", 18), fg="red", bg="lightblue")
    error_label.pack(pady=10)
    

    def check_pin():
        if pin_entry.get() == pin:
            pin_window.destroy()
            if action == "balance":
                open_balance_window()
            elif action == "deposit":
                open_deposit_window()
            elif action == "withdraw":
                open_withdraw_window()
        else:
            error_label.config(text="INCORRECT PIN.")
            

    submit_button =  Button(pin_window, text="SUBMIT",width=10,font=("Impact", 20),bg='black',fg='white',command=check_pin)
    submit_button.pack(pady=5)
    close_button =  Button(pin_window, text="BACK",width=10, font=("Impact", 20),bg='black',fg='white',command=pin_window.destroy)
    close_button.pack(pady=5)

def open_balance_window():
    balance_window =  Toplevel(root)
    balance_window.title("Check Balance")
    balance_window.geometry("500x500+400+100")
    balance_window.configure(bg="lightgreen")
    balance_window.overrideredirect(1)

    label =  Label(balance_window, text="", font=("Impact", 18), bg="lightgreen")
    label.pack(pady=50)
    label =  Label(balance_window, text="Your current balance is: Rs. ", font=("Impact", 18), bg="lightgreen")
    label.pack(pady=10)
    bal=str(balance)
    lblbal= Label(balance_window, text=bal , font=("Impact", 20), bg="lightgreen")
    lblbal.pack(pady=5)
    close_button =  Button(balance_window, text="CLOSE", font=("Impact", 20),bg='black',fg='white',command=balance_window.destroy)
    close_button.pack(pady=5)

def open_deposit_window():
    deposit_window =  Toplevel(root)
    deposit_window.title("Deposit Money")
    deposit_window.geometry("500x500+400+100")
    deposit_window.configure(bg="lightyellow")
    deposit_window.overrideredirect(1)

    label =  Label(deposit_window, text="", bg="lightyellow",font=("Impact", 18))
    label.pack(pady=40)
    label =  Label(deposit_window, text="Enter amount to deposit:", bg="lightyellow",font=("Impact", 18))
    label.pack(pady=20)
    deposit_entry =  Entry(deposit_window,font=("Impact", 18))
    deposit_entry.pack(pady=5)

    def deposit():
        global balance
        try:
            amount = float(deposit_entry.get())
            if amount <= 0:
                error_label =  Label(deposit_window, text="Enter a valid amount.", fg="red", bg="lightyellow",font=("Impact", 18))
                error_label.pack(pady=5)
            else:
                balance += amount
                success_label =  Label(deposit_window, text="Deposited Rs. " + str(amount) + "\nNew Balance: Rs. " + str(balance), fg="green", bg="lightyellow",font=("Impact", 18))
                success_label.pack(pady=5)
                deposit_entry.delete(0,  END)
        except ValueError:
            error_label =  Label(deposit_window, text="Invalid input. Enter a number.", fg="red", bg="lightyellow",font=("Impact", 18))
            error_label.pack(pady=5)

    deposit_button =  Button(deposit_window, text="DEPOSIT",width=10,font=("Impact", 20),bg='black',fg='white', command=deposit)
    deposit_button.pack(pady=10)
    close_button =  Button(deposit_window, text="CLOSE",width=10,font=("Impact", 20),bg='black',fg='white', command=deposit_window.destroy)
    close_button.pack(pady=10)

def open_withdraw_window():
    withdraw_window =  Toplevel(root)
    withdraw_window.title("Withdraw Money")
    withdraw_window.geometry("500x500+400+100")
    withdraw_window.configure(bg="pink")
    withdraw_window.overrideredirect(1)
    label =  Label(withdraw_window, text="", bg="pink",font=("Impact", 18))
    label.pack(pady=40)
    label =  Label(withdraw_window, text="Enter amount to withdraw:", bg="pink",font=("Impact", 18))
    label.pack(pady=10)
    withdraw_entry =  Entry(withdraw_window,font=("Impact", 18))
    withdraw_entry.pack(pady=5)
    
    def withdraw():
        global balance
        try:
            amount = float(withdraw_entry.get())
            if amount <= 0:
                error_label =  Label(withdraw_window, text="Enter a valid amount.", fg="red", bg="pink",font=("Impact", 18))
                error_label.pack(pady=5)
            elif amount > balance:
                error_label =  Label(withdraw_window, text="Insufficient funds.", fg="red", bg="pink",font=("Impact", 18))
                error_label.pack(pady=5)
            else:

                balance -= amount
                success_label =  Label(withdraw_window, text="Withdrew Rs. " + str(amount) + "\n New Balance: Rs. " + str(balance), fg="green", bg="pink",font=("Impact", 18))
                success_label.pack(pady=5)
                withdraw_entry.delete(0,  END)
        except ValueError:
            error_label =  Label(withdraw_window, text="Invalid input. Enter a number.", fg="red", bg="pink",font=("Impact", 18))
            error_label.pack(pady=5)

    withdraw_button =  Button(withdraw_window, text="WITHDRAW",width=10,font=("Impact", 20),bg='black',fg='white', command=withdraw)
    withdraw_button.pack(pady=10)
    close_button =  Button(withdraw_window, text="CLOSE",width=10,font=("Impact", 20),bg='black',fg='white', command=withdraw_window.destroy)
    close_button.pack(pady=10)

# Main Window UI
welcome_label =  Label(root, text="Welcome to TONI ATM",bg='yellow', font=("Impact", 30))
welcome_label.pack(pady=20)

balance_button =  Button(root, text="CHECK BALANCE", font=("Impact", 18),command=lambda: verify_pin("balance"),bg='black',fg='white', width=20)
balance_button.pack(pady=10)

deposit_button =  Button(root, text="DEPOSIT",font=("Impact", 18), command=lambda: verify_pin("deposit"),bg='black',fg='white', width=20)
deposit_button.pack(pady=10)

withdraw_button =  Button(root, text="WITHDRAW", font=("Impact", 18),command=lambda: verify_pin("withdraw"),bg='black',fg='white', width=20)
withdraw_button.pack(pady=10)

exit_button =  Button(root, text="EXIT",font=("Impact", 18), command=root.quit,bg='black',fg='white', width=20)
exit_button.pack(pady=20)

root.mainloop()
