class Credentials:
    def __init__(self,acc_type, acc_email, acc_password):
        self.type = acc_type
        self.email = acc_email
        self.password = acc_password
    
    def generate_password(self):
        #Dfeining password
        pas = str(12345)
        self.email = pas
