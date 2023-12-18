
# coding: utf-8

# In[1]:


print("Hello World")
#shift+Enter 치면 결과값 나타냄


# In[2]:


1+1


# In[3]:


7-4


# In[7]:


3*4
#왜 곱하기를 X라 안하고 *라 할까
#혼동을 방지하기 위해서. 누구는 알파벳 x로 생각하고 누구는 곱하기로 생각할 수 있으니까. 
#프로그래밍 언어의 중요한 소양은 언어를 명시적으로 짜야한다는것.
#그래서 곱하기를 *로 한다는것. 곱셈은 알파벳 엑스(x)가 아닌 별표로 대신한다!!!


# In[9]:


3/2
#이렇듯 프로그래밍언어에서 사람언어와 다른 예외 케이스들은 어쩄든 덜 헷갈리게 하려고 만들어진 것이다.
#기본적으로 나머지 대부분 케이스는 사람의 직관과 일치한다.
#예외적인 케이스들은 다 이유가 있다.


# In[11]:


13%5
#13나누기 5의 나머지 연산자는 %로 입력. 나머지=%


# In[14]:


1+2==3
#왜 등호가 두개? 변수를 쓸때는 등호를 하나만 쓴다. 그거랑 헷갈리지 않기 위해. 
#변수의 값을 대입하는 때에는 등호를 하나. 두가지를 비교할때는 등호를 두개.


# In[13]:


1+2==4


# In[15]:


10%2==0
#홀수와 짝수를 비교하는 로직


# In[19]:


11%2==0


# And와 or의 차이

# In[23]:


12%2==0 and 12%3==0


# In[28]:


14%2==0 and 14%3==0


# In[24]:


14%2==0 or 14%3==0


# 마크다운 단축키

# esc 누르면 커서 사라지고 거기서 마크다운의 약자인 m 누르면 마크다운으로바뀐다

# 샵을 눌러서 주석으로 바꿨다가 그걸 풀어서 모든 결과값이 다 나오지 않게, 약간 보기 편하게. 

# ## Markdown 기능
# ## 샵샵 스페이스누르면 커진다.
# ## 변수

# In[25]:


a=3
b=5

a+5


# In[27]:


a=3
b=13
a+b


# In[29]:


a=3
a=a+1
a
a=a+2
a
#이렇듯 마지막에 값만 나온다


# In[ ]:


#난 마지막꺼말고 세번째 꺼도 출력하고 싶은데? 그러면 중간에 print()를 적으면 된다.


# In[30]:


a=3
a=a+1
print(a)
a=a+2
a


# ## 이제부터 텍스트로!

# In[31]:


#문자열==텍스트==string
"Hello World!"


# In[34]:


#왜 프로그래밍언어는 쌍따옴표를 붙일까? 변수라고 혼동할 수 있기 떄문에
a


# In[33]:


"a"


# 이렇듯 문자열을 사용할때는 따옴표를 해줘야 한다.
# 변수 한번 저장하면 위에 하든 밑에 하든 다 나온다.
# 그리고 코드를 지워도 쥬피터노트북을 껐다 키지 않는 이상 (Kernel 탭의Restart&Run All) 변수 입력한 값은 계속 남아있다.

# In[36]:


#파이썬에는 홀따옴표도 쓸 수 있다.
#파이썬의 중요한 철학 중 하나는 하나의 문제를 해결하는 데에는 두개의 기능이 필요하지 않다 라는것.
#스위치케이스라는 다른 프로그래밍의 기능은 파이썬에 없다. if else로 가능하기 때문.
#그렇다면 왜 쌍따옴표와 홀따옴표를 구분할까?
#문장안에 홀따옴표 등장하는 경우가 있기 때문에
"Shayne's weight?"


# 문장에 홀따옴표가 등장하면 쌍따옴표로 감싸고
# 문장에 쌍따옴표가 등장하면 홀따옴표로 감싼다.

# ## 에러!

# 에러가 나는 경우.
# 누군가에게 다르게 해석될 수 있는 경우 버블이 난다.
# 애매모호한데? 싶은 것들은 실행을 안시키고 강제로 꺼버린다.
# 그러고 에러메시지를 던지는 것. "애매한걸 너가 고쳐줬으면 좋겠어" Help MEssage 같은거라고 생각하면된다.

# In[37]:


1+"2"


# In[39]:


#에러가 난다면? 당황하지말라.
#맨 아래줄에 에러메시지가 있다.
#화살표로 표시한 부분이 문제가 생긴 부분
# int==integer==정수형
# str==string==문자열


# 에러 쉽게 처리하기. 맨 마지막 에러메시지 복붙해서 구글링. stackoverflow라는 페이지 유명.
# 이걸로 해결된다. 구글 기준 1페이지 내에 해결된다고 보면 돼.
# 
# 요즘은 검색하는 것도 스킬!! 검색하는 것을 생활화하라!!
# 
# 처음 프로그래밍 하는사람은 좋은 프레임워크를 고르는 방법은 사람들이 많이 쓰는 걸 쓰면돼.
# 웬만하면 마이너한건 피하라.

# In[40]:


"1"+"2"
#문자를 이런 식으로 붙여쓸 수 있다.


# ## 포메팅
# 특정 코드- 위에서 어떤 코드를 실행시키냐에 따라 아래 코드가 달라진다.
# 그럴 때 쓰이는 코드: 포메팅

# In[42]:


bananas=3
days=5
"Shayne ate 3 bananas for 5 days"


# In[43]:


bananas=3
days=5

"Shayne ate {0} bananas for {1} days." .format(bananas, days)

#프로그래밍 언어상 모든 숫자의 시작은 0
# . 표시는 method라 해서 특수기능을 불러올 수 있는것.
#0은 첫번째, 1은 두번째. .format은 여기에 넣은 순서대로 입력된다고 보면된다.
# bananas가 첫번째고 days가 두번째인것


# In[45]:


#신버전은 다른 방식으로도 같은 기능 가능. 중괄호에 바나나랑 데이스 넣은 다음에 맨 앞에 f를 표시.
f"Shayne ate {bananas} bananas for {days} days."


# #shift+enter는 다음칸 넘어가는 기능이기도 해. 빈칸일떄는. 이런식으로 밑에다 여러칸 띄워놓고 하니까 보기 편하네

# In[50]:


model_a=0.123456789
model_b=0.987654321

f"[Accuracy] Model A= {model_a:.5f}, Model B={model_b:.3f}"

#소숫점이 많으면 정밀하다
#이 기능은 소숫점 원하는 자릿수로 자르기. 
#[Accuracy]는 그냥 string. 문자열.그냥 알아보기 쉽게 문자열 넣어준것.

# :. 기능이 소숫점 자르기 :.5f는 다섯자리수로 자르고 싶다는 것.


# In[52]:


#위처럼 신버전 f 대신 원래대로 format을 쓴다면
"[Accuracy] Model A={:.5f}, Model B={:.3f}".format(model_a, model_b)


# ## 문자열
# 문자를 좀 더 깊게 알아보자

# In[54]:


message = "Hello World!"
messagemessage


# In[55]:


#알파벳 부분중에 일부만 가져오고 싶다. 그러면 대괄호 []
print(message[0])
print(message[1])
print("----")
print(message[-1])
print(message[-2])
#알파벳을 뒤에서부터 가져오고 싶다. 그러면 마이너스 (-)기호를 붙인다.


# In[57]:


#중괄호는 포메팅 할 때 빼고는 안 쓴다. {} 
#대괄호는 무언가를 검색하거나 색인할 때 빼고는 안 쓴다. 예외적으로 list 할때는 쓴다. 추후에 볼것. []
#나머지는 전부 소괄호 ()


# In[60]:


message[0:4]
#콜론 (:)을 넣으면 0번째글자부터 4번째 글자 직전까지 일부를 표출 가능.
#4까지가 아니라 4 직전까지 실행하는 것임에 주의


# In[62]:


#특정문자열을 포함하고있냐 포함하고있지 않냐를 알아보고 싶을 때
# in 을 사용한다.
print("H" in message)
print("h" in message)
print("A" in message)
print("Hell" in message) 


# In[63]:


#어떤 method가 있는지 알아보고 싶으면 message 뒤에 .치고 tab 누르면 돼.
message.lower()
#lower는 다 소문자로 바꿔주는것


# In[65]:


message.upper()
#upper는 다 대문자로 바꿔주는것. 대표적인 두가지 메쏘드.


# ## 리스트
# 프로그래밍에서는 반복적으로 일어나는 상황을
# 짧게 줄여서 실행하게 해주는 기능이 있다. 그게 리스트
# 여러개의 값들을 하나로 묶어서 처리.
# 
# 예를 들면 변수를 너무 많이 입력해야 된다거나. 그런식.

# In[66]:


odd=[1,3,5,7,9] #이게 아까말한 예외 케이스인 대괄호. 대괄호 여기서도 쓰인다는것.
odd


# In[70]:


#문자열에 썼던것과 리스트는 비슷한 기능이 많다.
print(odd[0])
print(odd[1])
print("----")
print(odd[-1])
print(odd[-2])

#이처럼 몇번째 글자 실행시키는 것과 같이 리스트는 문자열과 똑같은 기능 수행한다.


# In[69]:


odd[0:4]


# In[71]:


print(1 in odd)
print(2 in odd)
print(3 in odd)


# In[78]:


#하지만 근본적으로 리스트랑 문자열은 다른 용도.
#문자열은 텍스트를 담기위한 거고 리스트는 값을 담기 위한 것.
#append를 넣으면 그다음에는 계속 그 값만 실행.
odd.append(11)
odd
#실행하면 실행할수록 그 값이 계속 실행된다. shift enter 여러번 누르면서 확인해보면 알수있다.


# In[80]:


odd[3]=-1
odd[5]=-1
odd
#값 바꾸기. odd[]=  이거로 0,1,2,3번째에 있는 숫자 값을 바꿀 수 있고 5번째 숫자값을 바꿀수 있다.
#헷갈리지만 시작은 0임을 항상 기억.


# In[83]:


#리스트인데 문자열의 기능을 쓰고 싶을때
#문자열로 변환해준다음에 문자열의 기능을 쓰고 다시 리스트로 바꿔준다
#문자열일 때 리스트기능을 쓰고 싶을때도 마찬가지

#문자를 리스트로 바꾼 케이스. 문자열 기능을 리스트에 적용! split: 쪼개쓰기의 기준을 정해달라. split(" "): 띄어쓰기 기준으로 쪼개달라.
message="Hello World!"
print(message.split(" "))
print(message.split("o"))


# In[84]:


#이번엔 리스트를 문자로 바꿔보기
words=["Hello", "World!"]
#이번에는 뭘 기준으로 두가지 문자열을 붙일거냐! (리스트의 기능을 문자열에 사용!)
print(" ".join(words)) #띄어쓰기를 기준으로 합친다.
print(",".join(words))
print(", ".join(words))


# # 제어문

# In[86]:


age=3

if age<5:
    print("아이")
else: 
    print("어른")
    
#이렇게 분계를 나눌 수가 있다.


# In[87]:


age=10

if age<5:
    print("아이")
elif age<18:
    print("학생")
else: 
    print("어른")
    
#if랑 else에 이어 elif라는 것도 알아두자.
#왜 else if 대신 elif를 쓰나? 다른언어에서는 else if라 한다. if와 else만 구현할 수 있으면 else if는 자동으로 구분할 수 있다.
#하지만 파이썬은 약간 문법이 달라서 :(콜론)과 띄어쓰기를 굉장히 중요시 여긴다. 
#실제로 위에서 했던거 띄어쓰기 잘못되면 다르게 나옴. 
#그래서 if와 else만으로 구현이 안되니까 고육지책으로 else if를 elif로 만든것.


# # 반복문

# In[90]:


basket= ['apple', 'banana', 'chicken', 'pineapple', 'cherry']

print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])


# In[89]:


#하지만 변수가 많아지면 이렇게 일일이 넣기도 어렵다. 이 문법을 줄여준게 for 문법
for stuff in basket:
    print(stuff)
    
#stuff라는 데에 하나씩 세주면서 출력하는 것.


# In[92]:


#단순 반복하고 싶다면? for+ in range 사용
for i in range(5):
    print(i)
    
    
#중요한건 콜론을 꼭 써야한다. 띄어쓰기를 두번째줄 앞에 꼭 해야 한다.


# In[94]:


for i in range(1, 5):
    print(i)
    
#5로 꼭 끝났으면 좋겠어. 그러면 (1,6)으로 써주면돼


# In[97]:


for i in range(1,6):
    if i==5:
        print("bang!")
        
    print(i)
    
    #반복문과 제어문을 같이 쓰기


# In[99]:


#반복문에서만 쓸수 있는 기능 break
#반복문이 break를 만나는 순간 반복문 전체가 강제종료된다.
for i in range(1,6):
    if i==5:
        print("bang!")
        break
        
    print(i)
    
    #이경우 5직전에서 "bang!"이 나온 다음에 break를 통해 반복문을 강제종료시켰으므로 5는 나오지 않는다.


# In[102]:


for i in range(1, 6):
    if i==2:
        print("beep!")
        
    if i==5:
        print("bang!")
        break
        
    print(i)
    
#for문과 if문의 관계를 잘 이해하는게 중요. if가 for 뒤에 어케 오느냐에 따라 결과가 달라진다.


# In[119]:


#continue
#continue는 루프를 한번만 스킵하고 재시작.
#break가 아예 강제종료인 것과 비교.

for i in range(1,6):
    if i==2:
        print("beep!")
        continue #이 기능으로 인해 2라는 숫자가 표시되지 않고 beep만 나오고 바로 다음인 3으로 넘어가는것.
    if i==5:
        print("bang!")
        break
        
    print(i)
    


# In[104]:


for i in range(10):
    print(i)


# In[106]:


#우리는 1부터 10까지하고 싶으니까
for i in range(1,11):
    print(i)


# In[107]:


double_list = [] #double_list로 2의배수 변수 설정

for i in range(1, 11):
    if i==5:
        continue #continue니까 5번째만 한번 스킵, 그 뒤는 그대로
    if i==8:
        break #break는 강제종료니까 8번째에서 아예 강제종료. 16 나오기직전까지 반복.
    
    double =i*2
    double_list.append(double) #여기서 띄어쓰기 한번 더 들어가면 요 두줄도 if의 범위로 들어간다.
    
double_list #결과적으로 5번째 빠지고 8번째 나오기전에 스탑


# In[108]:


#반복문의 범위를 결정하는게 콜론과 띄어쓰기

double_list = [] #double_list로 2의배수 변수 설정

for i in range(1, 11):
    if i==5:
        continue #continue니까 5번째만 한번 스킵, 그 뒤는 그대로
    if i==8:
        break #break는 강제종료니까 8번째에서 아예 강제종료. 16 나오기직전까지 반복.
    
        double =i*2
        double_list.append(double) 
    
double_list #다 if에 들어갔으므로 애초에 print될게 없어짐


# In[ ]:


double_list = [] #double_list로 2의배수 변수 설정

for i in range(1, 11):
    if i==5:
        continue #continue니까 5번째만 한번 스킵, 그 뒤는 그대로
    if i==8:
        break #break는 강제종료니까 8번째에서 아예 강제종료. 16 나오기직전까지 반복.
    
double =i*2
double_list.append(double) 
    
double_list #최종적으로 8인 상태에서 i가 종료되었고 그게 8*2로 출력된것. 결국 콜론과 띄어쓰기의 관계가 중요하다는것


# In[ ]:


#tab은 스페이스 4번과 같다. 요즘은 스페이스가 추세


# # 함수

# In[109]:


#def==define의 약자

def multiply(a,b):
    c=a*b
    return c

multiply(2,3)


# In[110]:


def multiply(a,b):
    c=a*b
    return c

print(multiply(2,3))
print(multiply(3,4))


# In[112]:


def sign(n):
    if n>0:
        return "양수"
    elif n<0:
        return "음수"
    else:
        return "0"
    
print(sign(-1))
print(sign(0))
print(sign(1))
print(sign(+1)) #+1 안해도 동작은 하지만 하는 것을 추천. 
#가독성 때문. 협업을 할때 동료프로그래머들이 읽기 쉽게. 가능한 띄어쓰기 많이 하고 +1로 쓰는게 더 좋다

#함수의 장점은 코드를 여러줄 묶어서 한줄로 나타낼 수 있다는것. 코드가 반복된다면 함수로 처리하면 된다.


# In[117]:


import pandas as pd
pd.read_csv("D:/user/python/train.csv").head()

