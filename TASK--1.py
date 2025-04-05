
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Pre-defined accounts
accounts = {
    112233: [1234, "Mallika", "9381903208", 10000],
    445566: [5678, "Sravya", "9234567880", 20000],
    778899: [2408, "Padma", "9123456787", 50000]
}

def send_otp_email(receiver_email):
    otp = random.randint(1111, 9999)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    mailusername = "mallikagalla2002@gmail.com"         
    mailpassword = "wldg iakd pzeg ddpp"      

    subject = "OTP For Validation"
    body = f"Your OTP for validation is {otp}"

    msg = MIMEMultipart()
    msg['From'] = mailusername
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(mailusername, mailpassword)
        server.send_message(msg)
        server.quit()

        verify_otp = int(input("Enter OTP to verify: "))
        if verify_otp == otp:
            print("Login Successful")
            return True
        else:
            print("Login Failed")
            return False
    except Exception as e:
        print("Failed to send OTP:", e)
        return False

while True:
    print("\nATM Menu")
    print("Choose the Required option(s):")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Pin Change")
    print("5. Pin Generation")
    print("6. Exit")

    option = int(input("Choose Your Option: "))

    if option == 1:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exist!")
        else:
            pin = int(input("Enter PIN: "))
            if pin != accounts[accno][0]:
                print("Invalid PIN")
            else:
                print(f"Balance: ₹{accounts[accno][3]}")

    elif option == 2:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exist!")
        else:
            money = int(input("Enter amount to Deposit: "))
            accounts[accno][3] += money
            print("Money Deposited Successfully!")

    elif option == 3:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exist!")
        else:
            pin = int(input("Enter PIN: "))
            if pin != accounts[accno][0]:
                print("Invalid PIN")
            else:
                money = int(input("Enter Amount to Withdraw: "))
                if money > accounts[accno][3]:
                    print("Insufficient Funds!..")
                else:
                    accounts[accno][3] -= money
                    print("Collect your cash...")

    elif option == 4:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Account does not exist!")
        else:
            pin = int(input("Enter Current PIN: "))
            if pin != accounts[accno][0]:
                print("Invalid PIN")
            else:
                npin = int(input("Enter New PIN: "))
                cpin = int(input("Confirm New PIN: "))
                if npin != cpin:
                    print("PIN Change Failed: PINs do not match")
                else:
                    accounts[accno][0] = npin
                    print("PIN Changed Successfully.")

    elif option == 5:
        accno = random.randint(111111, 999999)
        print(f"Your new Account Number is: {accno}")
        pin = int(input("Create a New PIN: "))
        cpin = int(input("Confirm your New PIN: "))
        if pin != cpin:
            print("Account Generation Failed: PINs do not match")
        else:
            name = input("Enter your Name: ")
            mobile = input("Enter your Mobile Number: ")
            email = input("Enter your Email Address: ")
            otp_verified = send_otp_email(email)
            if otp_verified:
                accounts[accno] = [pin, name, mobile, 0]
                print("Account and PIN Generated Successfully.")
            else:
                print("Account Creation Failed due to OTP verification.")

    elif option == 6:
        print("Thanks for using ATM.")
        break

    else:
        print("Invalid Option. Try Again.")
