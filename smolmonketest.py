crediter = input("Enter ID")

screditer = crediter.split('@')
crediter = screditer[0]+"@!"+screditer[1]
print(screditer)
print(crediter)