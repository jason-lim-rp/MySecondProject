data = "admin:$E*G$@R:/users/root"
split_data = data.split(":")

print ("User\t: %s" % split_data[0])
print ("Password: %s" % split_data[1])
print ("Homedir\t: %s" % split_data[2])

