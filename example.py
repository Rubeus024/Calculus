import re

#print( re.split(r'(s)', 'here are some worrds'))

#example2='Anothesr interesting eXamples'
#print( re.split(r'[e][s]',example2))

#print( re.findall(r'\d{2}', 'bielsko 20 st.slodka 23 and 139476235'))

#print(  re.findall(r'\d+', 'bielsko 203 st.slodka 3 and 139476235') )
myregex='-x^4+3x^3-12x-19'
lista=re.findall(r'[+-][\d]*[x]*', myregex)
newlista=[]
for element in lista:
    element=element.replace('x', '')
    if(len(element)==1):
        element+='1'
    newlista.append(element)
    print(element,len(element))

newlista=map(int,newlista)
print("Współczynniki", list(newlista))
#lista.append(lista[-1])
print('Lista po przeoraniu regexem: ', lista)
#nowalista=lista[0::2]
#print("Nowa lista po obróbce: ", nowalista)
