# Mass Email Sender Using Python
# Importing Libraries
import tkinter as tk
import smtplib
from plyer import notification

# Defining Functions

# Command For Send Button
def send_email():
    message = entry_msg.get()
    my_email = entry_email.get()
    my_pass = entry_password.get()
    my_subject = entry_subject.get()
    body = "Subject: {}\n\n{}".format(my_subject, message)
    f = open("recipients.txt", "r")
    recipients = f.readlines()
    for recipient in recipients:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(my_email, my_pass)
        s.sendmail(my_email, recipient.strip(), body)
        notification.notify(
            title="Auto Email Sender",
            message="Your Email To {} Was Sent Successfully".format(recipient.strip()),
            timeout=5
        )

# Command For ADD Button
def add_email():
    recipient_email = entry_to.get()
    f = open("recipients.txt", "a")
    f.write(recipient_email + "\n")
    entry_to.delete(0, tk.END)

# Open File To Write Emails
f = open("recipients.txt", "w")

# Setting Up Tkinter GUI

# Main Window And Grid Numbering
window = tk.Tk()
window.title("Mass Email Sender")
window.columnconfigure(0, uniform=100)
window.rowconfigure([0, 1, 2, 3, 4, 5], uniform=100)

# Creating Labels, Entries, Buttons And Arranging Them
label_subject = tk.Label(text="Enter Your Subject:")
entry_subject = tk.Entry(bg="gray", fg="black")
label_msg = tk.Label(text="Enter your message:")
entry_msg = tk.Entry(bg="gray", fg="black")
label_email = tk.Label(text="Enter your email:")
entry_email = tk.Entry(bg="gray", fg="black")
label_password = tk.Label(text="Enter your password:")
entry_password = tk.Entry(show="*", bg="gray")
label_to = tk.Label(text="Enter recipient email:")
entry_to = tk.Entry(bg="gray", fg="black")

# Create button to send email
send_button = tk.Button(text="Send Email", command=send_email, bg="blue", fg="white")

# Create button for adding the emails in a file
add_button = tk.Button(text="Add!", command=add_email, bg="white", fg="black")

# Add labels, entries and button to the window
label_subject.grid(row=0, column=0)
entry_subject.grid(row=0, column=1)
label_msg.grid(row=1, column=0)
entry_msg.grid(row=1, column=1)
label_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
label_to.grid(row=4, column=0)
entry_to.grid(row=4, column=1)
add_button.grid(row=4, column=2)
send_button.grid(row=5, column=1)

window.mainloop()

# References
# geeksforgeeks.org
# pypi.org
