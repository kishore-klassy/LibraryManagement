class User :
    def __init__(self,id,username,email,mobileNumber):
        self.UserID = id
        self.UserName = username
        self.Email = email
        self.MobileNumber = mobileNumber
    @staticmethod
    def fromTuple(user_tuple) :
        
        if len(user_tuple) == 3 :
            id=user_tuple[0]
            username=user_tuple[1]
            email = user_tuple[2]
        
            user=User(id,username,email)
            return user
        else :
            raise Exception("Value of the tuple Error")
        
    def to_dict(self) :
        return {
            "id":self.id,
            "username":self.username,
            "email" : self.email
        }
    

    # bookid , userid ,date ,isReturned 