import argparse
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-u', '--username', action='store', type=str, required=True, help='Username to use in Instagram Login')
#my_parser.add_argument('-p', action='store', type=int)
my_parser.add_argument('-p', '--password', action='store', type=str, required=True, help='Password to use in Instagram Login')

args = my_parser.parse_args()
username = args.username
password = args.password
#print("Hello to the",var2)
print("Username = {}".format(username))
#print("Password = {}".format(password))
