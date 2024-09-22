'''
a-z
0-9
. _ time 1
@time 1
. is on 4nd or 3rd in end postion
lower condition 
mini 6 char

saurabhhh365@gmail.com
'''
email = input("Enter a email : ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") ==1):
            if(email[-4] ==".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i=="." or i=="@":
                        continue
                    else:
                        d =1
                          
                if k == 1 or j ==1 or d==1:
                    print("Wrong email 5 :")
                else:
                    print("Right email")
            else:
                print("Wrong email 4 :")
        else:
            print("Wrong email 3 :")
    else:
        print("Wrong email 2 :")
else:
    print("Wrong email :")
    