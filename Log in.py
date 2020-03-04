class user:
        name = ' '
        email = ' '
        password = ' '
        login = False

        def login(self):
               email= input('Enter your email : ')
               password = input('Enter your password : ')

               if email == self.email and password == self.password :
                   login = True  
                   print('Login successful.')
                   
                   if login == True :
                      print("Welcome",self.name,"\n","Your code has successfully runned")
                   
               else :
                   login = False
                   print('Login failed')
                   
        def isLoggedIn(self):
                 if self.login :
                     return True
                 else :
                     return False
                     
        

user1 = user()
user1.name = ' Rahi '
user1.email = 'rahiraihanulhaque@gmail.com'
user1.password = '7244'
user1.login()