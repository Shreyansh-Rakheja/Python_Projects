
import sys
import string
class pass_word:
        def __init__(self,password,other=0):
                self.password=password
                self.other=other
                #self.check_password_length()
                #self.check_password_lower_case()
                #self.check_password_uppercase()
                #self.check_password_number()
                #self.check_password_sp_char()
                #self.check_password_reenter()
        def check_password_length(self):
                print(self.password)
                if(len(self.password)>=8):
                        return 1
                else:
                        print('length must be greater or equal than 8')
                        return 0

        def check_password_lower_case(self):
                for i in self.password:
                        if 96<ord(i)<123:
                                return 1
                return 0
        def check_password_uppercase(self):
                for i in self.password:
                        if 64<ord(i)<91:
                                 return 1
                return 0
        def check_password_number(self):
                s=['0','1','2','3','4','5','6','7','8','9']
                for i in self.password:
                        if i in s:
                                return 1
                return 0
        def check_password_sp_char(self):
                d=['@','#','$']
                for i in self.password:
                        if i in d:
                                return 1
                return 0
        def check_password(self):
                for j in range(3):
                        length = self.check_password_length()
                        
                        lower = self.check_password_lower_case()
                        
                        upper = self.check_password_uppercase()
                                #print(upper)
                        number = self.check_password_number()
                               # print(number)
                        sp_char = self.check_password_sp_char()
                               # print(sp_char)
                        

                                    
                        if number==1 and sp_char==1 and upper==1 and lower==1 and length==1:
                                        cp=self.check_password_reenter()
                                        if cp==1:
                                                f=open('C:/Users/User/Desktop/user_data.txt','a+')
                                                f.write(user_name)
                                                f.write(p)
                                                f.close
                                                break
                                        else:
                                                #self.password=None
                                                break
                                        if self.other==1:
                                                break                        
                        else:
                                        print('password denied,use Uppercase,lowercase,numbers and special character')
                                        if self.other==1:
                                                break
                                        else:
                                                if j==1:
                                                        print("This is your last chance.Please enter carefully")
                                                        self.password=input("Enter password again: ")
                                
                                                elif j<1:
                                                        self.password=input("Enter password again: ")
                        
        def check_password_reenter(self):
                self.reenter=input("comfirm password")
                if self.reenter==self.password:
                        print("password matched")
                        return 1
                else:
                        print("password does not match")
                        return 0
if __name__=='__main__':
        user_name=input("enter the user name")
        p=input("enter the password(min length 8)")
        obj=pass_word(p)
        
        obj.check_password()
        
#obj.check_password_reenter()
#password=input("enter the password(min length 8)")
#s=['0','1','2','3','4','5','6','7','8','9']
#d=['@','#','$']
'''r=string.ascii_uppercase
e=string.ascii_lowercase

number=0
sp_char=0
upper=0
lower=0
retry=3
for j in range(3):
                length = check_password_length(password)
                
                lower = check_password_lower_case(password)
               # print(lower)
                upper = check_password_uppercase(password)
                #print(upper)
                number = check_password_number(password)
               # print(number)
                sp_char = check_password_sp_char(password)
               # print(sp_char)
                if(len(password)>=8):
                                pass
                else:
                                print('length must be greater or equal than 8')
                                sys.exit()

                        #for i in password:
                            #if i in s:
                                    
                                   # number=1
                                    
                                  
                            #if i in d:

                                   #sp_char=1
                            
                           # if i in r:
                                    
                                    #upper=1
                           # if i in e:
                                    
                                    #lower=1

                            
                if number==1 and sp_char==1 and upper==1 and lower==1:
                                print('password accepted')
                                break
                else:
                                print('password denied')
                if j==2:
                        print("This is your last chance.Please enter carefully")
                        password=input("enter the password(min length 8)")'''
     
    
            
        
