
### TDOD 
Document these
  #### User and Privileges ####

```python

    def _encrypt(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    def _get_user(self,user,password):
        password = self._encrypt(password)
 
        userTable=self.tables['meta_users']._select_where("*",f'user=={user}')
    
        if (userTable.user[0] == user and userTable.password[0] == password):
            return userTable
        else:
            sys.exit('User Validation Error ! Exiting...')

    def create_user(self,user,password,db,tables)

    def _create_admin(self,dbname ,user,password):
        if (user==None):
            user = "Admin"

        if (password == None):
            password = self._encrypt("password")
        else:
            password = self._encrypt(password) 

        self.tables['meta_users']._insert([user,"admin",dbname,"*",password])
```