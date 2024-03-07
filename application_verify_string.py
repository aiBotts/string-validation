# This program validates and email address
# by verifying the ending and the @ symbol

def is_valid_email(email):
    # Does it end with .edu?
    if email.endswith(".edu"):
        # iterating the @ over the string
        if "@" in email:
            return True
        else:
            return False

# calling the is valid function
print(is_valid_email("jbotts4@volstate.edu"))