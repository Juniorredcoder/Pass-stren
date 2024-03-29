import re
import colorama
from colorama import Fore
import os

os.system('clear')
os.system('figlet Pass-Stren | lolcat')
print(Fore.CYAN + "                                         CODED BY G-ONE")
print(Fore.CYAN + "                                         Version:1.0.1")
class PasswordTester():
    def __init__(self):
        # lower case
        self.p1 = re.compile('[a-z]')
        # upper case
        self.p2 = re.compile('[A-Z]')
        # numbers
        self.p3 = re.compile('[0-9]')
        # symbols
        self.p4 = re.compile('[^A-z0-9]')
        # length 5
        self.p5 = re.compile('.{5}')
        # length 6
        self.p6 = re.compile('.{6}')
        # length 7
        self.p7 = re.compile('.{7}')
        # length 8
        self.p8 = re.compile('.{8}')
        # length 9
        self.p9 = re.compile('.{9}')
        # length 10
        self.p10 = re.compile('.{10}')
        # length 11
        self.p11 = re.compile('.{11}')
        # length 12
        self.p12 = re.compile('.{12}')
        # length 13
        self.p13 = re.compile('.{13}')
        # length 14
        self.p14 = re.compile('.{14}')
        # length 15
        self.p15 = re.compile('.{15}')
        # length 16
        self.p16 = re.compile('.{16}')
        # length 17
        self.p17 = re.compile('.{17}')
        # length 18
        self.p18 = re.compile('.{18}')
        # length 22
        self.p19 = re.compile('.{21}')
        # length 26
        self.p20 = re.compile('.{22}')
        # length 26
        self.p21 = re.compile('.{26}')
        
        self.timeToCrackList = [Fore.RED + "Instantly",Fore.RED + "Seconds",Fore.RED + "Minutes", Fore.RED + "Hours" ,Fore.RED + "Days", Fore.YELLOW + "Years",\
                                Fore.GREEN + "Thousands of years",Fore.GREEN +  "Millions of years",Fore.GREEN +  "Billions of years"]
        
        self.ContainsLowerCase = False
        self.ContainsUpperCase = False
        self.ContainsNumbers = False
        self.ContainsSymbols = False
        self.passwordLength = 0
        
        self.BadPassword = False
        
        self.strength = 0
        
        self.commonPasswords = '''123456
123456789
qwerty
12345678
111111
1234567890
1234567
password
123123
987654321
qwertyuiop
mynoob
123321
666666
18atcskd2w
7777777
1q2w3e4r
654321
555555
3rjs1la7qe
google
1q2w3e4r5t
123qwe
zxcvbnm
1q2w3e'''
    
    def testStrength(self, password):
        
        try:
            p = re.compile(password)
            m = p.search(self.commonPasswords)
        
            if(m):
                self.BadPassword = True
            else:
                self.BadPassword = False
        except:
            None
            
        self.strength = 0
        m1 = self.p1.search(password)
        m2 = self.p2.search(password)
        m3 = self.p3.search(password)
        m4 = self.p4.search(password)
        m5 = self.p5.search(password)
        m6 = self.p6.search(password)
        m7 = self.p7.search(password)
        m8 = self.p8.search(password)
        m9 = self.p9.search(password)
        m10 = self.p10.search(password)
        m11 = self.p11.search(password)
        m12 = self.p12.search(password)
        m13 = self.p13.search(password)
        m14 = self.p14.search(password)
        m15 = self.p15.search(password)
        m16 = self.p16.search(password)
        m17 = self.p17.search(password)
        m18 = self.p18.search(password)
        m19 = self.p19.search(password)
        m20 = self.p20.search(password)
        m21 = self.p20.search(password)
        
        if(m1):
            self.ContainsLowerCase = True
        else:
            self.ContainsLowerCase = False
        if(m2):
            self.ContainsUpperCase = True
        else:
            self.ContainsUpperCase = False
        if(m3):
            self.ContainsNumbers = True
        else:
            self.ContainsNumbers = False
        if(m4):
            self.ContainsSymbols = True
        else:
            self.ContainsSymbols = False
            
        self.passwordLength = len(password)
        
    
        if ((m1 and m2 and m3 and m4 and m14) or (m1 and m2 and m3 and m14)\
                or (m1 and m2 and m16) or ((m1 or m2) and m18) or (m3 and m21)):
            self.strength = 8
        elif ((m1 and m2 and m3 and m4 and m12) or (m1 and m2 and m3 and m13)\
                or (m1 and m2 and m15) or ((m1 or m2) and m16) or (m3 and m20)):
            self.strength = 7
        elif ((m1 and m2 and m3 and m4 and m11) or (m1 and m2 and m3 and m11)\
                or (m1 and m2 and m13) or ((m1 or m2) and m14) or (m3 and m19)):
            self.strength = 6
        elif ((m1 and m2 and m3 and m4 and m9) or (m1 and m2 and m3 and m9) \
                or (m1 and m2 and m11) or ((m1 or m2) and m12) or (m3 and m17)):
            self.strength = 5
        elif((m1 and m2 and m3 and m4 and m8) or (m1 and m2 and m3 and m8) \
                or (m1 and m2 and m9) or ((m1 or m2) and m10) or (m3 and m14)):
             self.strength = 4   
        elif((m1 and m2 and m3 and m4 and m7) or (m1 and m2 and m3 and m7) \
                or (m1 and m2 and m8) or ((m1 or m2) and m9) or (m3 and m11)):
             self.strength = 3
        elif((m1 and m2 and m3 and m4 and m6) or (m1 and m2 and m3 and m6) \
                or (m1 and m2 and m7) or ((m1 or m2) and m8) or (m3 and m11)):
             self.strength = 2
        elif((m1 and m2 and m3 and m4 and m5) or (m1 and m2 and m3 and m5) \
                or (m1 and m2 and m6) or (m3 and m10)):
             self.strength = 1
        else:
            self.strength = 0
        
        return self.strength
    
    def timeToCrack(self):
        return self.timeToCrackList[self.strength]
        
    def passwordInfo(self):
        return Fore.GREEN+"Password length: {0}\nLower case: {1}\nUpper case: {2}\nNumbers: {3}\nSymbols: {4}".\
        format(self.passwordLength,self.ContainsLowerCase,self.ContainsUpperCase,self.ContainsNumbers,\
        self.ContainsSymbols)
        
while True:
        tester = PasswordTester()
        password = input(Fore.CYAN + "Enter password to check password strength:")
        tester.testStrength(password)
        print(Fore.GREEN+"Time to crack: {}".format(tester.timeToCrack()))
        print("\n" + tester.passwordInfo())
    
        if(tester.BadPassword):
            print(Fore.RED + "\nWarning!")
            print(Fore.RED + "You have one of the 25 most common passwords in the world.")
     
