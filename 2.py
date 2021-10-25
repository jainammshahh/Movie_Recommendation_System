from prettytable import PrettyTable
table1=PrettyTable()

file = open("demo.c","r")

def Icons(x):
    k=['#','<','>','{','}',',',';','-','+','*','/',' ','\n','\t','(',')']
    return x in k
def Keywords(x):
    k = ['int','float','void','include','stdio.h','conio.h','break','printf','for']
    return (x in k)
def Operators(x):
    k=['-','+','*','/','%']
    return (x in k)
def Punctuations(x):
    k=[',',';']
    return (x in k)
def AssignmentOperators(x):
    return (x == '=')
def SpaceOperators(x):
    return x == "\n" or x == "\t" or x == ""
def Preprocessors(x):
    return (x == "#")
def Relational(x):
    k = ['<','>','=>']
    return x in k
def Brackets(x):
    return (x == '(' or x == ')' or x == '{' or x == '}')
def Comments(x):
    k=['//','/*','*/']
    return (x in k)

listofcharacters=[]
while 1:
    char = file.read(1)
    if not char:
        break
    listofcharacters.append(char)
print(listofcharacters)

icons = []
for i in range(len(listofcharacters)):
    if Icons(listofcharacters[i]):
        icons.append(i)
print(icons)

words=[]
for i in range(len(icons)-1):
    words.append(listofcharacters[icons[i]])
    temp = ""
    for j in range(icons[i],icons[i+1]):
        temp = temp + listofcharacters[j]
    words.append(temp[1:])
print(words)

allwords = list(filter(lambda a: a != ' ', words))
allwords = list(filter(lambda a: a != '\n', allwords))
allwords = list(filter(lambda a: a != '\t', allwords))

table1.field_names = ["Icons","Token Names"]
for i in allwords:
    if Keywords(i):
        table1.add_row([i,"Keyword"])
    elif Operators(i):
        table1.add_row([i,"Operator"])
    elif AssignmentOperators(i):
        table1.add_row([i,"Assignment Operator"])
    elif Preprocessors(i):
        table1.add_row([i,"Pre-processor"])
    elif Relational(i):
        table1.add_row([i,"Relational Operator"])
    elif SpaceOperators(i):
        table1.add_row([i,"Space Operator"])
    elif Brackets(i):
        table1.add_row([i,"Bracket"])
    elif Punctuations(i):
        table1.add_row([i,"Punctuations"])
    elif Comments(i):
         table1.add_row([i,"Comments"])
    else:
        table1.add_row([i,"Identifier"])
print(table1)
        
