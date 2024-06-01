import sys
#wlecome page
welcome = '''
*************************
*        Welcome        *
*        python         *
*************************
'''
print(welcome)
#input element 
nameinput= input("Enter you'r name\t")
idinput= input("Enter you'r id\t")
Ageinput= input("Enter you'r age\t")
if nameinput == "" :
 sys.exit("enter your name and try agen")
elif idinput == "":
   sys.exit("enter your id and try agen")
elif Ageinput =="":
   sys.exit("enter your age and try agen")
#dara input contners
username = str(nameinput)
iduser = str(idinput)
Ageuser = str(Ageinput)
#simple data
data = [{
    "name": "kidus",
    "id": 1010,
    "Age": 17,
    "sex": "M"
}, {
    "name": "Jc",
    "id": 1011,
    "Age": 18,
    "sex": "M"
}, {
    "name": "max",
    "id": 1012,
    "Age": 19,
    "sex": "F"
}]
#user data add to simple data
data.append("username:"+username+ "\n"+"id:"+iduser+"\n"+"Age:"+Ageuser)
#user data output 
print(data[-1])
