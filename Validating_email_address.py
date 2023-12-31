import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

def filter_mail(emails):
    return list(filter(is_valid_email, emails))

if __name__ == '__main__':
    n = int(input())
    email_list = [input() for _ in range(n)]

    valid_emails = filter_mail(email_list)
    valid_emails.sort()
    print(valid_emails)
