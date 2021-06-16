
def emailProcess(email):
    # youtube@codexplore.dev
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    #print(f"User name is {email_username}")
    return [email_username, email_domain]

def printMsg(email_username, email_domain):
    print(f"User is {email_username}; Email Domain is {email_domain}")

def main():
    email = input("Please input your email: ").strip()
    email_username, email_domain = emailProcess(email)
    printMsg(email_username, email_domain)

main() # gọi khi có module khác gọi module này

#if __name__ == "__main__": # gọi khi chính module này được gọi thực thi
#    main()