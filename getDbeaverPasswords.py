import os
import sys
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
 
class getDbeaverPasswords:
    LOCAL_KEY_CACHE = bytes([186, 187, 74, 159, 119, 74, 184, 83, 201, 108, 45, 101, 61, 254, 84, 74])
    DEFAULT_FILE_PATH = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "DBeaverData", "workspace6", "General", ".dbeaver", "credentials-config.json")
 
    @staticmethod
    def decrypt(contents):
        file_iv = contents[:16]
        cipher = AES.new(getDbeaverPasswords.LOCAL_KEY_CACHE, AES.MODE_CBC, iv=file_iv)
        decrypted = cipher.decrypt(contents[16:])
        return unpad(decrypted, AES.block_size).decode('utf-8')
 
    @staticmethod
    def main():
        file_path = sys.argv[1] if len(sys.argv) > 1 else getDbeaverPasswords.DEFAULT_FILE_PATH
 
        try:
            with open(file_path, 'rb') as file:
                contents = file.read()
 
            decrypted_content = getDbeaverPasswords.decrypt(contents)
            print(type(decrypted_content))
            print(decrypted_content)
 
            with open("passwords.json", "w") as output_file:
                json_obj = json.loads(decrypted_content)
                json.dump(json_obj, output_file, indent=4)
                
            print("Decrypted content saved to passwords.json")
 
        except FileNotFoundError:
            print(f"Error: File not found - {file_path} \n Provide credentials-config.json path as argument")
        except IOError as e:
            print(f"Error reading file: {str(e)}")
        except Exception as e:
            print(f"Error decrypting file: {str(e)}")
 
if __name__ == "__main__":
    getDbeaverPasswords.main()
 
