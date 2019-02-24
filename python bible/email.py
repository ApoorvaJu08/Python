#get user email address

email = input('''what is your email address?: ''').split()

#slice out user name

user = email[:email.index('''@''')]

#slice domain name

domain = email[email.index('''@''')+1:]

#format message

output = '''Your username is {} and your domainname is {}.'''.format(user,domain)

#display output message

print(output)
