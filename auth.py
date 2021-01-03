from functools import wraps

def hasAccess(minPriv, currentPriv):

    if minPriv == "system" and currentPriv == "system" :
        print("here")
        return True

    if minPriv == "admin" and (currentPriv =="system" or currentPriv=="system"):
        print("her2e")
        return True

    if minPriv == "user":
        return True

    return False    

def privileges(minPriv):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            self = args[0]
            
            if self._isnew:
                ret = function(*args, **kwargs) 
                return ret
            
            currentUser = self._currentUser

            tables = currentUser.tables[0]
            
            if not hasAccess(minPriv,currentUser.group[0].strip()):
                raise Exception('User Priviledges Error ')

            if currentUser.group[0] == "system":
                ret = function(*args, **kwargs) 
                return ret

            if tables != "*":
                for table in tables.split(","):
                    if table == args[1]:
                        ret = function(*args, **kwargs) 
                        return ret
            else:
                if not args[1][:4]=="meta":
                    ret = function(*args, **kwargs) 
                    return ret
                else:
                    raise Exception('You have no access for this! Exiting...')

        return wrapper
    return real_decorator

