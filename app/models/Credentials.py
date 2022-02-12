class Credentials:

    """
    Init method that helps defie properties of our objects
    """
    """
    ARGS:
        acc_type: Type of account
        email: Users email 
        password: Users password
        
    """
    
    # Class Variables
    ac_type = []
    ac_email=[]
    ac_password=[]

    def __init__(self,acc_type, acc_email, acc_password):
        self.type = acc_type
        self.email = acc_email
        self.password = acc_password

    #POsting Credentials
    def save_credentials(self):
        Credentials.ac_password.append(self.password)
        Credentials.ac_email.append(self.email)
        Credentials.ac_type.append(self.type)


    
    def generate_password(self):
        #Defining password
        pas = str(12345)
        self.email = pas
