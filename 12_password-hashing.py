import os,hashlib

def hash_password(password):
    salt="secret"
    hashed_pw=hashlib.sha256((salt+password).encode()).hexdigest()
    print(hashed_pw)
    return hashed_pw
def verify_password(password,hashed_pw):
        new_hash=hash_password(password)
        if(new_hash==hashed_pw):
            print("verified")
            return True
        else:
            print("not verified")
            return False

original_password=input("enter the password")
hashed_pw=hash_password(original_password)
b=input("reenter the password")
verify_password(b,hashed_pw)

  
  
import unittest

class PasswordTestCase(unittest.TestCase):
    def test_Match(self):  # test method names begin with 'test'
        original="abhi"
        hashed=hash_password(original)
        self.assertTrue(verify_password(original,hashed))

    def test_NotMatch(self):
        original="abhi12"
        hashed=hash_password(original)
        self.assertFalse(verify_password("wrong_password",hashed))
    
    def test_empty(self):
        hashed=hash_password("")
        self.assertTrue(verify_password("",hashed))  

if __name__ == '__main__':
    unittest.main()
