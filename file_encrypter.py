from cryptography.fernet import Fernet

#Will generate a key
def generate_key():
  return Fernet.generate_key()

def save_key(key, key_file):
  with open(key_file, "wb") as file:
    file.write(key)


# def load_key(key_file):
    
#     with open(key_file, "rb") as file:
       
#       return file.read()


#Encrypt file
def encrypt_file(input_file,output_file, key):
   
   
   with open(input_file,"rb") as file:

     
    data = file.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
  
   with open(output_file, 'wb') as file:
     
    file.write(encrypted_data)

#Decrypt file
def decrypt_file(input_x, decrypted_file, key):
  with open(input_x, "rb") as file:
    encrypted_data = file.read()

  fernet = Fernet(key)
  decrypted_data = fernet.decrypt(encrypted_data)

  with open(decrypted_file, "wb") as file:
    file.write(decrypted_data)




if __name__ == '__main__':


  print("FILE ENCRYPTOR \n BY: SULAIMAN SHAMS")
  

  key = generate_key()
  key_file = 'encryption_key.key'
  save_key(key, key_file)

  #input
  input_file = input(str("Enter file name:"))

  encrypted_file = 'encrypted_file.txt'
  decrypted_file = 'decrypted_file.txt'

  encrypt_file(input_file, encrypted_file, key)
  print(f"file '{input_file} encrypted to '{encrypted_file}'")

  input_x = input(str("Enter file name that you want to decrypt:"))
  

  decrypt_file(input_x, decrypted_file, key)
  print("File Decrypted!!")
  




