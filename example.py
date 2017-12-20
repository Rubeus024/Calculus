
import re


#Listy odpowiednio ze współczynnikami i z potęgami
coeffList=[]
powerList=[]

myregex = 'x^3 - 6x^2 + 4x + 12'

# czyścimy string z niepotrzebnych spacji
myregex = ''.join([x for x in myregex if x!=' '])
#Wzór reg. expression
lista=re.findall(r'[+\-]*\d*[a-z]*\^*\d*', myregex)
# czyścimy string z niepotrzebnych spacji
lista= [x for x in lista if x !='']

for element in lista:
    xPosition=element.find('x')
    powerPosition=element.find('^')
    #print("Gdzie jest x: ", xPosition)
    #print(type(element.find('x')))

    # w zależności od pozycji x dodajemy elementy do tablic
    if element.find('x') == 0:
        coeffList.append(1.0)
     #   print("Nowa lista : ", coeffList)
    # -1 oznacza brak znaku
    elif element.find('x') == -1:
        coeffList.append(float(element))
        powerList.append(0.0) # nie ma x, potęga 0
      #  print("Nowa lista : ", coeffList)
       # print("PowerList", powerList)
    elif element.find('x')==1:
        if element[0]=='+':
            coeffList.append(1.0)
        else:
            coeffList.append(-1.0)
    #reszta współczynników
    else:
            coeffList.append(float(element[0:xPosition:1]))
           # print("Nowa lista : ", coeffList)

    if element.find('^') ==-1 and element.find('x') != -1:  #jeśli nie ma znaku a mamy potęge
        powerList.append(float(1))
       # print("PowerList111", powerList)
    elif element.find('x')!=-1:
        powerList.append(float( element[powerPosition+1::1] ) )
       # print("PowerList", powerList)

print("Ostatecznie:")
print("Lista współczynników", coeffList)
print("Potęgi: ", powerList)
finalList=tuple(zip(coeffList,powerList))
print(tuple(finalList))
sum=0.0
x=5.0
for value, power in finalList:
    if power==0:
        sum+=value
    else:
        sum+=float(value)*x**float(power)
        
print("Suma",sum)





