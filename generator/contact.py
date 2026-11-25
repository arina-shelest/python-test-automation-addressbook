from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"
for o, arg in opts:
    if o == "-n":
        n = int(arg)
    elif o == "-f":
        f = arg


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])


testdata = [
               Contact(firstname="", lastname="", email=""),
           ] + [
               Contact(firstname=random_string("John_", 10), lastname=random_string("Smith_", 10), title="Engineer",
                       company="Meta", email=random_string("email_", 10), bday="11",
                       bmonth="October", byear="1986")
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
