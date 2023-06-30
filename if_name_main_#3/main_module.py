from codexplore import emailProcess, printMsg



def main():
    emails = [" hc@gmail.com","youtube@yahoo.com", "win@youtube.com"]
    for email in emails:
        username, domain = emailProcess(email)
        printMsg(username, domain)


if __name__ == "__main__": # gọi khi chính module này được gọi thực thi
    main()