'''

- random unicode comment added to str // maYBE NOT seems a bit annoying to implement and dont have time
- split ascii values into numbers for math
- compile each line at a time

'''

import string 
import random
import math

ALLSTR=string.ascii_letters+"1234567890"


inputFile = "hi.py"
utf8identify = "]"


def rstring(): 
    random_config={
        "c": ''.join([random.choice(ALLSTR) for _ in range(1,random.randint(20,40))]),
        "r": ''.join([random.choice(ALLSTR) for _ in range(1,random.randint(20,40))]),
    }
    return f"""
import string 
import random
import math

ALLSTR=string.ascii_letters+"1234567890"
def {random_config['r']}(): return 1*random.randint(1,1000) if (x:=int(math.factorial(round((math.pi / random.randint(1,100)) * random.randint(1,5))) * random.randint(1,1000))) != 1 else x*random.randint(1,1000)
def {random_config['c']}(): return (chr({random_config['r']}()))
''.join([{random_config['c']}() for _ in range(1,random.randint(1000,10000))])
"""

try:
    efull = ""
    open("out.py","w").write("")
    if inputFile[len(inputFile)-3:] != ".py":
        exit("Not a python file")
    og = open(inputFile,"r").read()
    for line in og.split("/n"):
        end=""
        line = rstring()+line
        for char in line:
            end += f"str({ord(char)/2}+{ord(char)/2}){utf8identify}"
        end = end[:len(end)-1]
        print(end)
        open("out.py","a").write('''def uIO9(sM2nxdo, dNm23I: str, In4weX: int): sM2nxdo = sM2nxdo.replace('str(',f'exec("a{In4weX} = chr(int(');sM2nxdo += f')", None, {dNm23I});';return {"Jie": sM2nxdo}
Oe33={}'''+f''';[exec(uIO9(meow, "Oe33", v)['Jie']) for v,meow in enumerate("{end}".split(']'))]; exec(''.join([Oe33[eee222] for eee222 in Oe33]))\n''')

except Exception as e:
    exit(f"Error --{e}")