text = "Hello << UserName>>,how are you"
username = input("Enter the user name : ")
if len(username )>=3:
 newtext = text.replace("UserName", username)
else:print("enter the min 3 character")
print(newtext)

