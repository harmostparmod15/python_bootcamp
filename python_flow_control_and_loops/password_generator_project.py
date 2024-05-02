import random
import  string

letters = string.ascii_letters;
digits = string.digits;
puncs = string.punctuation;

salt = letters + digits + puncs;

password = "";
passLen = int(input("enter length for password :"));
for i in  range(passLen):
   password += random.choice(salt);
print("######################");
print(f"password generation success : {password}");