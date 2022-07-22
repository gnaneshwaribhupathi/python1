#!/usr/bin/env python
# coding: utf-8

# In[1]:


#STATEMENT:instructions which a python interpreter can execute


# In[2]:


#RULE1:SINGLE LINE STATEMENTS :write single statement in a single line


# In[3]:


1+1


# In[4]:


2+2


# In[5]:


#RULE2:MULTIPLE STATEMENTS IN A SINGLE LINE USE(;)


# In[6]:


print(1+1);print(2+2)


# In[7]:


#RULE3:SINGLE STATEMENTS IN A MULTIPLE LINES  USE (\)


# In[8]:


2+2


# In[9]:


#RULE4:COMMENTS:dont want to execute a statement : COMMENTS ARE TWO TYPES 
                                                 #SINGLE LINE COMMENTS  USE (#)BEGINNING OF THE STATEMENT
                                                 #MULTIPLE LINE COMMENTS USE ('''  ''')OR USE ("""  """)at the beginning and at the end 
                     


# In[10]:


#apple


# In[11]:


'''apple'''


# In[12]:


"""apple"""


# In[13]:


#RULE5:RESERVED WORDS:particular meaning in the python engine
36 key words 
3 words where first character will be capital (TRUE, FALSE,NONE)
REST KEY WORDS ARE IN LOWER CASE

#RULE6:IDENTIFIERS:it is a name given to an object(entity)i.e;single occurence of something 
VARIABLE:IT IS A CONTAINER WHERE WE CAN STORE DATA 
# In[ ]:


#NAMING CONVENTITION 
1RULE:variable name should start with_or an alphabets(abc)(ABC)
    
2RULE:variable name should not start with a number or special symbols
    
3RULE:it can be a combination of alphabets and numbers
    
4RULE:variable name should not have any special symbols
    
5RULE:sensitive language (python is a case sensitive programming  language)    


# In[ ]:


#positive slicing:in the string value starts from 0 if we go from left to right
#negative slicing:in the string value starts from -1 if we go from right to left(ending index will not be included)
#NOTE:python engine will always go from left to right 


# In[ ]:


x="abcdef@"
x[2:6]


# In[ ]:


x="abcdefgh@"
x[-8:-1]


# In[ ]:


x="bhupathi"
x[-8: ]


# In[ ]:


#STRING METHODS:we use (.)in the string methods


# In[ ]:


#1:UPPER():this method will convert all lowercase alphabets into uppercase alphabets inside the string.


# In[ ]:


var1="abcdefgh"
var1.upper()


# In[ ]:


var2="abcdDEFG"
var2.upper()


# In[ ]:


#2LOWER():will convert uppercase alphabets into lowercase alphabets in the string


# In[ ]:


var3="ABCDEFGH"
var3.lower()


# In[ ]:


var4="BHUPathi"
var4.lower()


# In[ ]:


var5="bhupat@12"
var5.lower()


# In[ ]:


#3CAPITALIZE():will convert the first character in a string into uppercase and rest of the characters
will be in lower case.


# In[10]:


var4="askmethedoubt123"
var4.capitalize()


# In[ ]:


var5="bhupathi"
var5.capitalize()


# In[ ]:


var6="1gnan"
var6.title()


# In[ ]:


#4TITLE():This method will convert the first character of a word inside the string into upper case alphabet.


# In[ ]:


var4="python java visual"
var4.title()


# In[ ]:


var5="1python java visual"
var5.title()


# In[ ]:


var6="1python 2java 3visual"
var6.title()


# In[ ]:


#5SWAPCASE:will convert uppercase characters in a string into lowercase characters and viceversa.


# In[ ]:


var6="bhupATHI"
var6.swapcase()


# In[ ]:


var7="asd@#$sswBHEM"
var7.swapcase()


# In[ ]:


#CONCATENATION:this (+)symbol is used in combining multiple strings into a single string.


# In[ ]:


var8="bhupathi"
var9="gnaneshwari"
var8+var9


# In[ ]:


var1="inno"
var2="mati"
var3="tics"
var1+var2+var3


# In[ ]:


#6COUNT():will count how many times a character is present inside a string


# In[14]:


x="aaaabdcfeha"
x.count("a")


# In[15]:


x="abababcdcdefghiab"
x.count("ab")


# In[16]:


#starting index and ending index 


# In[17]:


x="abcdaaa"
x.count("a",3,7)


# In[18]:


x="bbbcefghibb"
x.count("b",0,11)


# In[19]:


#7REPLACE():TO replace a single or sequence of characters in a string


# In[20]:


x="abaadef"
x.replace("a","@")


# In[21]:


x="afternoonatonepm"
x.replace("n","#")


# In[22]:


x="b@n@n@"
x.replace("@","a")


# In[23]:


x="adddssvsdaaaa"
x.replace("a","@",4)


# In[24]:


x="abddssvsdaaaa"
x.replace("s","@",1)


# In[25]:


#8INDEX():will return the index value of a character occuring at first instance.


# In[26]:


x="abssdfghavaa"
x.index("a")


# In[27]:


x="abdssfghaaav"
x.index("a",1)


# In[28]:


#9FIND():Index value of a character occuring at first instance 


# In[29]:


var1="abddssvsdaaaa"
var1.find("v")


# In[30]:


var1="abssvdfghj"
var1.find("@")


# In[31]:


#10SPLIT:This method splits the string into substrings


# In[32]:


var3="python  java c  c++ visual"
var3.split()


# In[33]:


var4="python@java@c@c++@visual"
var4.split("@")


# In[34]:


x=var4


# In[35]:


var4.count(x)


# In[36]:


#11PARTITION():Splits into three parts (#before, #value ,#after)


# In[37]:


x="a b c d e f"
x.partition("c")


# In[38]:


x="java  python   c++"
x.partition(" ")


# In[39]:


#12STRIP():It is used to remove any character from starting and ending of a string.
EACH CHARACTER IS CONSIDERED AS INDIVIDUAL


# In[ ]:


var3="  apple  "
var3.strip()


# In[ ]:


var4="@apple@"
var4.strip("@")


# In[ ]:


var5="abcdefab"
var5.strip("ab")


# In[ ]:


x1="abcdef"
x1


# In[ ]:


x1[0].upper()+x1[1]+x1[2].upper()+x1[3]+x1[4].upper()+x1[5]


# In[ ]:


#13STARTSWITH():It is mainly used to find whether your string is starting with specified character(GIVES ANS AS TRUE OR FALSE)


# In[ ]:


var4="abcd@@@@"
var4.startswith("a")


# In[ ]:


var5="abcdedd222"
var5.startswith("b",1)


# In[ ]:


#14ENDSWITH():It is mainly used to find whether your string in ending with specified character.


# In[ ]:


var4="abcd@@@@"
var4.endswith("@")


# In[ ]:


var5="abcdefff@@"
var5.endswith("@",9)


# In[ ]:


#15ISALPHA():Is to check whether your string is having all characters as alphabets .


# In[ ]:


var3="asdfghnhhh"
var3.isalpha()


# In[ ]:


var4="12asdfgjjnb"
var4.isalpha()


# In[ ]:


#16ISDIGIT():Is to check whether your string is having all characters as numeric


# In[ ]:


var5="1234584122"
var5.isdigit()


# In[ ]:


var6="asd1248223"
var6.isdigit()


# In[ ]:


#17ISALNUM():Is to check whether the string has characters as alphabets or numeric


# In[ ]:


var2="12abggv"
var2.isalnum()


# In[ ]:


#18ISUPPER():WHETHER THE CHARACTERS IN STRING HAVING UPPERCASE ALPHABETS 


# In[ ]:


var4="ASKosnhh"
var4.isupper()


# In[ ]:


var5="ADSHGHB"
var5.isupper()


# In[ ]:


#19ISLOWER():WHETHER THE CHARACTERS IN THE STRING HAVING LOWERCASE ALPHABETS 


# In[ ]:


var5="asnhb"
var5.islower()


# In[ ]:


var5="ASBBBG"
var5.islower()


# In[ ]:


#20ISTITLE():


# In[ ]:


var4="Python Java Visual"
var4.istitle()


# In[ ]:


var5="python java visual"
var5.title().istitle()


# In[ ]:


#21ISSPACE():is to check whether the characters have space


# In[ ]:


var2="   "
var2.isspace()


# In[ ]:


var4=""
var4.isspace()


# In[ ]:


#MAKETRANS:This method will make a mapping table which can be used in translate method to translate the characters


# In[ ]:


var1="abcaadiaasssiiii"
table=var1.maketrans("asi","@#!")
var1.translate(table)


# In[ ]:


#LEN():INBUILT FUNCTION NOT METHOD
      IS MAINLY USED TO KNOW HOW MANY CHARACTERS IS PRESENT INSIDE THE STRING 


# In[ ]:


var2="abcdef"
len(var2)


# In[ ]:


var3="  abcdefgh  "
len(var3)


# In[ ]:


x="abcdefgh  "
len(x.strip())


# In[ ]:


#ISIDENTIFIER():


# In[ ]:


var4="var1"
var4.isidentifier()


# In[ ]:


var5=" var1 "
var5.isidentifier()


# In[ ]:


var5="_var1"
var5.isidentifier()


# In[ ]:


var5="_var1  "
var5.isidentifier()


# In[ ]:


#FORMAT:method is used to combine string with another data type like string,int,float,complex


# In[ ]:


name="gnaneshwari"
age=26


# In[ ]:


"my name is {} my age  is {}".format(name,age)


# In[ ]:


name="gnaneshwari"
age=26
height=152.4
weight=55.2
gender="female"


# In[ ]:


"my name is {} my age is {} my height is {}  my weight is {}  my gender  is  {}".format(name,age,height,weight,gender)


# In[ ]:


#IN FORMAT THE DATA WHICH WE ARE PASSING HAVE INDEX VALUE STARTING FROM 0.


# In[ ]:


#STR():will construct string from integer,float,as well as complex
1.string 2.complex 3.float 4.integer


# In[ ]:


x=1
y=1.1
z=1+2j


# In[ ]:


str(x)


# In[ ]:


str(y)


# In[ ]:


str(z)


# In[ ]:


#int()


# In[ ]:


x="1234"
int(x)


# In[ ]:


#ESCAPE CHARACTERS :used to insert the characters which we cannot used in the string 
(\ backward slash)
(/ forward slash)
(\n new line)
(\t tab space)0
(\b backspace)


# In[ ]:


"hi welome \"to\" python"


# In[ ]:


print("hi welcome\nto python\nand java")


# In[ ]:


print("hi welcome\tto python\t java")


# In[ ]:


print("hi welcome  \b  to  python  \b  java")


# In[ ]:


x=10
y=12
print(x,y,sep="\n")


# In[ ]:


x=10
y=12
print(x,y,sep=" ")


# In[ ]:


x=10
y=12
print(x,y,1000,1.10,sep="\n")


# In[ ]:


x=10


# In[ ]:


type(x)


# In[40]:


x="abdsn"
type(x)


# In[41]:


print(x,end=" ")
print(y,end=" ")
print("hi")


# In[ ]:


#create five  dynamic variables name age height weight gender


# In[ ]:


name=input("my name is " )
age=int(input("my age is "))
height=float(input("my height is " ))
weight=float(input("my weight is " ))
gender=input("my gender is ")
bio_data="my name is {},my age is {},my height is  {}, my weight is {},my gender is {}"
bio_data.format(name,age,height,weight,gender)


# In[ ]:


name=input("my name is ")


# In[ ]:


age=int(input("my age is "))


# In[ ]:


height=float(input("my height is "))


# In[ ]:


weight=float(input("my weight is "))


# In[ ]:


gender=input("my gender is ")


# In[ ]:


booktitle=input(" book title is ")
author=input("author name is" )
copies=int(input("no of copies produced" ))
weight=float(input("each book weights "))
sold=int(input("no of copies sold"))
books_store="book title is {},author name is {},no of copies produced {},each book weight{},no of copies sold{}"
books_store.format(booktitle,author,copies,weight,sold)


# In[ ]:


booktitle=input("book title is :\n ")
author=input("author name is :\n ")
copies=int(input("no of copies produced :\n "))
weight=float(input("each book weights :\n "))
sold=int(input("no of copies sold :\n "))
books_store="book title is {},\n author name is {},\n no of copies produced {},\n each book weights {},\n no of copies sold {}"
books_store.format(booktitle,author,copies,weight,sold)


# In[ ]:


print( booktitle,author,copies,weight,sold)


# In[ ]:


var1="bhupathi"
var1


# In[ ]:


var1[0].upper()+var1[1]+var1[2].upper()+var1[3]+var1[4].upper()+var1[5]+var1[6].upper()+var1[7]


# In[ ]:


var2="abcdef"
var2


# In[ ]:


var2=1
var3=1.1
var4=1+2j
var2+var3+var4


# In[ ]:


x=(3.1+2j)
type(x)


# In[ ]:


name=input("my name is ")
job=input("my job is ")
salary=int(input("my monthly salary is "))
experience=int(input("my jod experience is "))
weight=float(input("my weight is "))
bio_data="my name is {},my job is {},my monthly salary is {},my job experience is {},my weight is {}"


# In[ ]:


print(name);print(job);print(salary);print(experience);print(weight)


# In[ ]:


x="abcdefghijk"
x[0:2];x[0:3];x[0:4];x[0:5];x[0:11]


# In[ ]:


x[-5:-1];x[-12: ]


# In[ ]:


print("gnaneshwari");print("bhupathi");print("anasuyamma");print("pulasetty")


# In[ ]:


2+4


# In[ ]:


152-52


# In[ ]:


152+156


# In[ ]:


"gnaneshwari"


# In[ ]:


"bhupathi  gnaneshwari sreenivasulu lalitha  sreekanth anasuyamma "


# In[ ]:


#bhupathi


# In[ ]:


x="""gnaneshwari bhupathi"""


# In[ ]:


x='''gnaneshwari bhupathi'''


# In[ ]:


var1="abcdefghijklmnopqrstuvwxyz"
var1.upper()


# In[ ]:


var2="gnaneshwari bhupathi learning data science in innomatics"
var2.upper()


# In[ ]:


var3="GNANESHWARI IS A M.COM POSTGRADUATE STUDENT"
var3.lower()


# In[ ]:


var4="GNNEJAN"
var4[0:5].lower()


# In[ ]:


var4[-8: ].lower()


# In[ ]:


var4="gnaneshwari"
var5="bhupathi"
var4.capitalize()+var5.capitalize()


# In[ ]:


var1="bhupathi1"
var1.capitalize()


# In[ ]:


var1="bhupathi  gnaneshwari  innomatics"
var1.title()


# In[ ]:


var2="0bhupathi  1gnaneshwari  2innomatics"
var2.title()


# In[ ]:


var2="BHUPathi"
var2.swapcase()


# In[ ]:


var2="@@bhuPATHI"
var2.swapcase()


# In[ ]:


var3="1bhupaTHIGNANESHWARI223"
var3.swapcase()


# In[ ]:


var4="gnaneshwari"
var5=  "bhupathi"
var6= "studying"
var7= "datascience"
var4+var5+var6+var7


# In[ ]:


var5="askagainafterattention"
var5.count("a")


# In[ ]:


var5="aaanhbwaa"
var5.count("a",0,9)


# In[ ]:


var5.count("a",2,9)


# In[ ]:


var6="bhupathibhupathibhupathi"
var6.replace("b","@")


# In[ ]:


var6="@#$$&&^%$#@@"
var6.replace("$","a")


# In[ ]:


var5="adbbhhwaanbd"
var5.replace("a","@",9)


# In[ ]:


var3="blackpinkinyourarea"
var3[0:5].replace("black","white")+var3[5:9].replace("pink","black")+var3[9:11].replace("in","is")+var3[11:15].replace("your","mine")+var3[15: ].replace("area","@")


# In[ ]:


var2="aabdsenjnj"
var2.index("a")


# In[ ]:


var2.index("n")


# In[ ]:


var2.index("j")


# In[ ]:


var2.index("a",1)


# In[ ]:


var12="abddssvsdaaaa"
var12.index("a",1)


# In[ ]:


var2="abcdefahanjjaa"
var2.find("a")


# In[ ]:


var2.find("#")


# In[ ]:


var4="gnaneshwari  bhupathi  innomatics  kukatpally"
var4.split()


# In[ ]:


var4="1  2  2  4"
var4.split()


# In[ ]:


var4="100000  200000  30000 400000 500000"
var4.split()


# In[ ]:


var2="python java c++ c visual sql"
var2.split()


# In[ ]:


var="bhupathi  gnaneshwari innomatics"
var.partition("gnaneshwari")


# In[ ]:


var2="1  2  3  4"
var2.partition("3")


# In[ ]:


var5="gnaneshwari  bhupathi  innomatics  studying "
var5.partition("innomatics")


# In[ ]:


var6="bhupathi gnaneshwari     innomatics    studying"
var6.partition("  ")


# In[ ]:


var5="  banana  "
var5.strip()


# In[ ]:


var6="bbhupathib"
var6.strip("b")


# In[ ]:


var5="@apple@"
var5.strip("@")


# In[ ]:


var6="abcefghijkacb"
var6.strip("abc")


# In[ ]:


var5="abcdefgha"
var5.strip("a")


# In[ ]:


var3="abcdefgh@@@"
var3.startswith("a")


# In[ ]:


var4="bsdehhhbhb"
var4.startswith("a")


# In[ ]:


var5="abcdefghijk"
var5.startswith("b",1)


# In[ ]:


var5="abcdefghikjn"
var5.endswith("n")


# In[ ]:


var5="abdcdjhnd"
var5.endswith("d",-1)


# In[ ]:


var2="abcd@@@@"
var2.endswith("d",1,4)


# In[ ]:


var2="abcdefghi@@"
var2.endswith("@")


# In[ ]:


var1="AMNCDUIEIB"
var1.isalpha()


# In[ ]:


var2="asdjcdjjdb"
var2.isalpha()


# In[ ]:


var2="12asjj@#$"
var2.isalpha()


# In[ ]:


var5="12331889"
var5.isdigit()


# In[ ]:


var3="12.2"
var3.isdigit()


# In[ ]:


var1="_123"
var1.isdigit()


# In[ ]:


var1="123"
var1.isdigit()


# In[ ]:


x="acbw125461@##"
x.isalnum()


# In[ ]:


x="welocome129e"
x.isalnum()


# In[ ]:


x="bhupathignaneshwari999"
x.isalnum()


# In[ ]:


x="BHUPATHIGNANESHWARI"
x.isupper()


# In[ ]:


x="AXSSNNIIMwjioo@#"
x.isupper()


# In[ ]:


x="AVSHWBnjjxb"
x[0:7].isupper()


# In[ ]:


x="asubb12338"
x[-5:-1].isalnum()


# In[ ]:


var3="asxsnnANNXSN"
var3[-7:-1].islower()


# In[ ]:


var3[0:6].islower()


# In[ ]:


var3="ASSBJDWBN"
var3.lower().islower()


# In[ ]:


var2="Python  Java  Visual"
var2.istitle()


# In[ ]:


var3="python java  visual"
var3.title().istitle()


# In[ ]:


var2="   "
var2.isspace()


# In[ ]:


var2=""
var2.isspace()


# In[ ]:


var3="abcsdnwj"
var3.isspace()


# In[ ]:


var2="aaasnjnjnssniiii"
var2.maketrans("asi","@#$")


# In[ ]:


table=var2.maketrans("asi","@#$")
var2.translate(table)


# In[ ]:


x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
len(x)


# In[ ]:


x="bhupathignaneshwari"
len(x)


# In[ ]:


x="  abcdefg  "
len(x)


# In[ ]:


x="  abcdefg  "
len(x.strip())


# In[ ]:


"hi welcome \"to\" python"


# In[ ]:


"higher acheivements \"takes\"  \"time "


# In[ ]:


print("higher  \nacheivements \ntakes \ntime")


# In[ ]:


print("Name:gnaneshwaribhupathi  \nFathername: sreenivasulu \nAddress:2-2-735/9  \npochammabasthi  \namberpet  \nhyderabad  \npincode:500013")


# In[ ]:


bool(0)


# In[ ]:


bool(1223)


# In[ ]:


bool(0.0)


# In[ ]:


bool("")


# In[ ]:


bool(" ")


# In[ ]:


x=1
y=2
x+y


# In[ ]:


x="a"
y="b"
x+y


# In[ ]:


x=1
y=2
x-y


# In[ ]:


x="ab"
x*3


# In[ ]:


x="ab"
x*-3


# In[ ]:


10/2


# In[ ]:


10%2


# In[ ]:


2**2


# In[ ]:


4**2


# In[ ]:


4**3


# In[ ]:


cube=3
2**cube


# In[ ]:


square=2
2**square


# In[ ]:


11/2


# In[ ]:


11//2


# In[ ]:


13/2


# In[ ]:


13//2


# In[ ]:


12/2


# In[ ]:


12//2


# In[ ]:


x=1


# In[ ]:


x+=1


# In[ ]:


print(x)


# In[ ]:


var1=10
var2=20
var1>var2


# In[ ]:


10>20


# In[ ]:


10<20


# In[ ]:


10==20


# In[ ]:


10<=20


# In[ ]:


10>=20


# In[ ]:


10!=20


# In[ ]:


10==10


# In[ ]:


x=10
y=10


# In[ ]:


x==y


# In[ ]:


x=[1,2,3]
y=[1,2,3]
x==y


# In[ ]:


x is y


# In[ ]:


id(x)


# In[ ]:


id(y)


# In[ ]:


x  is not y


# In[ ]:


x=10
y=2


# In[ ]:


x>y and x%2==0  and x%5==0


# In[ ]:


y<x and x/2==5 and x%2==0


# In[ ]:


x>y or x%3==0  or x%7==0


# In[ ]:


not(x>y or x%3==0 or x%7==0)


# In[ ]:


x=100
y=100
x  is y


# In[ ]:


id(x)


# In[ ]:


id(y)


# In[ ]:


x="abcd"
y="abcd"
x is y


# In[ ]:


x="abcdefghijklmnop"
x[0].upper()


# In[ ]:


x[1].replace( "b","@")


# In[ ]:


x[2].upper()


# In[ ]:


x[4].replace("d","@")


# In[ ]:


x[5].upper()


# In[ ]:


x[6].replace("g","@")


# In[ ]:


x[7].upper()


# In[ ]:


x[8].replace("i","@")


# In[ ]:


x[9].upper()


# In[ ]:


x[10].replace("k","@")


# In[ ]:


x[11].upper()


# In[ ]:


x[12].replace("m","@")


# In[ ]:


x[13].upper()


# In[ ]:


x[14].replace("o","@")


# In[ ]:


x=int(input("salary of person A "))
y=int(input("salary of person B "))


# In[ ]:


x>y


# In[ ]:


x="abcd1234"
x[5: ].isdigit()


# In[ ]:


x="12 34@ w 5"
x.count(" ")


# In[ ]:


x.find(" ")


# In[ ]:


x.find(" ",3)


# In[ ]:


x.find(" ",7)


# In[ ]:


x=10
y=11
x<=y


# In[ ]:


x=111
y=121
x!=y


# In[ ]:


x=10
y=10
x is y


# In[ ]:


x=20
y=30
x is not y


# In[ ]:


#BITWISE OPERATORS:


# In[ ]:


a=3
b=2


# In[ ]:


a & b


# In[ ]:


bin(3)


# In[ ]:


bin(2)


# In[ ]:


bin(5)


# In[42]:


3 | 4


# In[43]:


bin(3)


# In[44]:


bin(4)


# In[45]:


bin(7)


# In[46]:


a=10


# In[47]:


~a


# In[48]:


a=100


# In[49]:


~a


# In[50]:


a=-100


# In[51]:


~a


# In[52]:


a=3
b=2


# In[53]:


a^b


# In[54]:


bin(a)


# In[55]:


bin(b)


# In[56]:


10>>1


# In[57]:


bin(10)


# In[58]:


bin(5)


# In[59]:


20>>2


# In[60]:


bin(20)


# In[61]:


bin(5)


# In[62]:


10<<1


# In[63]:


#COLLECTION***:


# In[64]:


#LIST:


# In[65]:


x=[1,2,3,4,5,6,7,8]


# In[66]:


type(x)


# In[67]:


y=list((1,2,3,4,5,6,7))


# In[68]:


type(y)


# In[69]:


z=[1,2,3,1.1,2.3,2+3j,"abcdef"]


# In[70]:


type(z)


# In[71]:


len(z)


# In[72]:


z[3:6]


# In[73]:


z


# In[74]:


type(q)


# In[ ]:


q


# In[ ]:


q[3:8]


# In[ ]:


q[-1]


# In[ ]:


q=[1,2,3,"a","b"]


# In[ ]:


q[0]=100


# In[ ]:


q


# In[ ]:


q[2:3]=200,300


# In[ ]:


q


# In[ ]:


q[-1]=2+1j


# In[ ]:


q


# In[ ]:


q[1:2]=10000,1.2


# In[ ]:


q


# In[3]:


x=[1,2,3,4]


# In[4]:


x.insert(0,"abcedf")


# In[5]:


x


# In[6]:


x.insert(3,"cdfg")


# In[7]:


x


# In[1]:


x=[1,2,3,4]
x.append(1)


# In[2]:


x


# In[8]:


x.append("ab")


# In[9]:


x


# In[ ]:


x=[1,2,3,4]


# In[ ]:


x.extend("56789")


# In[ ]:


x


# In[ ]:


x.extend([5,6,7,8,9,10])


# In[ ]:


x=int(input("number 1 is :"))
y=int(input("number 2 is :"))
z="x {} ,y {} , sum is {} ,min is {} , division is {} ,mul of {} ,percentage of {} ,// of {}".format(x,y,x+y,x-y,x/y,x*y,x%y,x//y)
print(z)


# In[ ]:


var10=[]
var10


# In[ ]:


var10.extend("abcdef")


# In[ ]:


var10


# In[ ]:


x=[1,2,3,4,5]


# In[ ]:


type(x)


# In[ ]:


x=[1,2,3,5,6,7,8,9]


# In[ ]:


x.insert(3,4)


# In[ ]:


x


# In[ ]:


x=[1,2,3,5,6,7,8,9]


# In[ ]:


x.append(10)


# In[ ]:


x


# In[ ]:


x=["hello"]


# In[ ]:


x.append("world")


# In[ ]:


x


# # REMOVE METHOD

# In[ ]:


x=["a","b","c","d",1,2,3,"a"]


# In[ ]:


x.remove("c")


# In[ ]:


x


# # POP METHOD

# In[ ]:


x=["a","b","c","d",1,2,3,"a"]


# In[ ]:


x.pop(2)


# In[ ]:


x


# In[ ]:


x=[1,2,3,4,5,6,7]


# In[ ]:


x.pop(3)


# In[ ]:


x


# # DEL(KEYWORD)

# In[ ]:


x=['a','b','c','d']


# In[ ]:


del x[2]


# In[ ]:


x


# In[ ]:


del x[:]


# In[ ]:


x


# # sort method

# In[1]:


x=[2,3,5,7,1,9]


# In[2]:


x.sort()


# In[3]:


x


# # x.sort(reverse=True)

# In[4]:


x=[2,3,5,7,1,9]


# In[5]:


x.sort(reverse=True)


# In[6]:


x


# In[ ]:


x=["b","a","c","e","d"]


# In[ ]:


x.sort()


# In[ ]:


x


# In[ ]:


x.sort(reverse=True)


# In[ ]:


x


# In[ ]:


x=["B","a","d","e","c","b"]


# In[ ]:


x.sort()


# In[ ]:


x


# In[ ]:


x=["B","a","d","e","c","b","A"]


# In[ ]:


x.sort()


# In[ ]:


x


# In[ ]:


x.sort(reverse=True)


# In[ ]:


x


# # COPY METHOD

# In[1]:


x=[1,2,3,4,"a","b"]


# In[2]:


x


# In[3]:


y=x.copy()


# In[4]:


y


# In[5]:


z=y


# In[6]:


del z[0]


# In[7]:


z


# In[8]:


x


# # COUNT()

# In[ ]:


x=[1,2,3,4,5,6,1,1,1,1,1,1]


# In[ ]:


x.count(1)


# # index()

# In[97]:


x=[1,2,3,4,5,6,7,8,9,1,1,1]


# In[98]:


x.index(1)


# In[99]:


x.clear()


# In[100]:


x


# In[101]:


x=["a","b","c","d"]


# In[102]:


x


# In[103]:


x[0]=x[0].upper()


# In[104]:


x


# In[105]:


x[2]=x[2].upper()


# In[106]:


x


# In[ ]:


x.sort()


# In[ ]:


x


# In[ ]:


x=[]


# In[ ]:


x


# In[ ]:


x=int(input("value of A "))
y=int(input("value of  B "))
z=int(input("value of c "))


# In[ ]:


a=[x,y,z]


# In[ ]:


a


# In[ ]:


x=input()


# In[ ]:


x.split()


# In[ ]:


x=((1,2,3,4))


# In[ ]:


type(x)


# # sets

# In[83]:


x={1,2,3,4,5,"a","b"}


# In[84]:


type(x)


# In[86]:


x


# In[87]:


{1,1,1,1,1,1,1}


# In[90]:


l={1,2,1,2,1,3,4,5,6,1,8,9}


# In[91]:


set(l)


# In[92]:


list(set(l))


# In[93]:


x="abcadcdeffde"


# In[94]:


q=x[0:3]+x[6:9]


# In[95]:


q


# In[96]:


set(q)


# # JOIN (STRING METHOD)

# In[76]:


x=["a","b","c"]


# In[77]:


"@".join(x)


# In[78]:


x=["java","python","c++"]


# In[79]:


" ".join(x)


# In[80]:


"@".join(x)


# In[ ]:


x="""Mahendra Singh Dhoni (/məˈheɪndrə ˈsɪŋ dhæˈnɪ/ (listen); born 7 July 1981) is an Indian professional cricketer who was captain of the Indian national cricket team in limited-overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014. He is a right-handed wicket-keeper batsman.[3] He led the team to three ICC trophies including the 2007 ICC World Twenty20, 2011 ICC Cricket World Cup and 2013 ICC Champions Trophy. Under his captaincy, India won the Asia Cup two times, in 2010 and 2016. India also won ICC Test Championship Mace two times in 2010 and 2011 under his leadership. He is considered as one of the greatest Captains and Wicket Keeper-Batsmen of all time.[4][5][6][7][8][9] Throughout his 15 year long international career, Dhoni has won several awards and accolades.[10][11][12][13]

In Indian domestic cricket he played for Bihar and Jharkhand Cricket team. He is the captain of Chennai Super Kings (CSK) in the Indian Premier League. He captained the side to championships in the 2010, 2011, 2018 and 2021 editions of IPL league. Also under his captaincy Chennai Super Kings (CSK) Won Champions League T20 two times, in 2010 and 2014"""


# In[ ]:


x


# In[ ]:


#create a tuple and try to insert an element


# In[75]:


x=input("value of a ")
y=input("value of b ")
z=input("value of c ")
q=print(x,y,z)


# In[81]:


x=["a","b","c","d"]


# In[82]:


"is".join(x)


# # ADD METHOD():THIS METHOD IS USED TO ADD NEW ELEMENTS IN A SET.

# In[8]:


x={1,2,3,4}


# In[9]:


x.add("abcd")


# In[10]:


x


# # UPDATE METHOD:IT IS USED TO INSERT ELEMENTS INSIDE A SET.WE CAN INSERT MULTIPLE ELEMENTS AT A TIME.string and all collection data type

# In[11]:


x={1,2}


# In[12]:


x.update([3,4,5,6])


# In[13]:


x


# In[14]:


x.update([13,14,15,16])


# In[15]:


x


# In[16]:


x.update("abcdef")


# In[17]:


x


# # REMOVE METHOD():REMOVE THE ELEMENTS INSIDE A SET

# In[18]:


x.remove("b")


# In[19]:


x


# # discard method:

# In[20]:


x.discard("d")


# In[21]:


x


# In[24]:


x.discard(5)


# In[25]:


x


# # pop():

# In[25]:


x.pop()


# In[26]:


x


# # clear():

# In[27]:


x.clear()


# In[28]:


x


# In[29]:


x=[]


# In[30]:


x


# In[31]:


type(x)


# In[32]:


y=()
type(y)


# In[33]:


z={}
type(z)


# In[34]:


a=set()
type(a)


# # union

# In[35]:


x={1,2,3,4}
y={5,6,7,8}


# In[40]:


z=x.union(y)


# In[37]:


z


# In[38]:


z.update()


# In[39]:


z


# In[41]:


y.update(x)


# In[42]:


x


# In[43]:


y


# # intersection

# In[44]:


x.intersection(y)


# In[45]:


s=x.intersection(y)


# In[46]:


s


# In[47]:


x


# In[48]:


y


# In[49]:


y.intersection_update(x)


# In[50]:


y


# In[61]:


x1={1,2,3,4,5,6}
x2={6,7,8,9,1,2}


# In[62]:


z=x2.union(x1)


# In[63]:


z


# # DICTIONARY

# In[4]:


x={"name":"gnaneshwari","age":25,"phonenumber":1264,"height":152.2}


# In[5]:


type(x)


# In[6]:


x


# In[7]:


x.keys()


# In[8]:


x.values()


# In[9]:


x.items()


# In[10]:


x["age"]


# In[11]:


x["height"]


# In[12]:


x["name"]


# In[13]:


x["age"]=29


# In[14]:


x


# In[15]:


x["height"]=56.3


# In[16]:


x


# In[17]:


x["weight"]=55.2


# In[18]:


x


# In[19]:


x["weight"]=56.2


# In[20]:


x


# In[21]:


del x['phonenumber']


# In[22]:


x


# # update():dictionaries

# In[23]:


x


# In[24]:


x.update({'name': 'gnaneshwari', 'age': 27, 'height': 152.5, 'weight': 156.2})


# In[25]:


x


# In[26]:


x.update({"aa":12,"ab":20,"abc":30})


# In[27]:


x


# # get method

# In[28]:


x.get("name")


# In[29]:


x.get("age")


# In[30]:


x.get("ab")


# In[31]:


x.clear()


# In[32]:


x


# In[33]:


x={1,2,3}
y=x.copy()


# In[34]:


y


# In[45]:


z={"a","b","c","d"}


# In[46]:


z


# In[43]:


r=z.copy()


# In[44]:


r


# In[55]:


x={"gnaneshwari","sreekanth","lalitha","sreenivasulu","anasuyamma"}


# In[56]:


x


# In[57]:


y=x.copy()


# In[58]:


y


# In[ ]:




