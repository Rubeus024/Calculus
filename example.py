
import re


class Polynomal:

    def __init__(self,str_reg_expr):
        self._reg_expr = str(str_reg_expr)
        self._coeff_list = []
        self._power_list = []
        self.__coeff_power_tuple = ()
        self.create_coefficient()

    def create_coefficient(self):
        self._reg_expr = ''.join([x for x in self._reg_expr if x != ' '])
        # Wzór reg. expression
        lista = re.findall(r'[+\-]*\d*[a-z]*\^*\d*', self._reg_expr)
        # czyścimy string z niepotrzebnych spacji (po funkcji re.findall czasami pojawia się spacja lub dwie, niewiadomo czemu)
        lista = [x for x in lista if x != '']

        for element in lista:
            xPosition = element.find('x')
            powerPosition = element.find('^')
            # print("Gdzie jest x: ", xPosition)
            # print(type(element.find('x')))

            # w zależności od pozycji x dodajemy elementy do tablic
            if element.find('x') == 0:
                self._coeff_list.append(1.0)
            #   print("Nowa lista : ", coeffList)
            # -1 oznacza brak znaku
            elif element.find('x') == -1:
                self._coeff_list.append(float(element))
                self._power_list.append(0.0)  # nie ma x, potęga 0
            #  print("Nowa lista : ", coeffList)
            # print("PowerList", powerList)
            elif element.find('x') == 1:
                if element[0] == '+':
                    self._coeff_list.append(1.0)
                else:
                    self._coeff_list.append(-1.0)
            # reszta współczynników
            else:
                self._coeff_list.append(float(element[0:xPosition:1]))
            # print("Nowa lista : ", coeffList)

            if element.find('^') == -1 and element.find('x') != -1:  # jeśli nie ma znaku a mamy potęge
                self._power_list.append(float(1))
            # print("PowerList111", powerList)
            elif element.find('x') != -1:
                self._power_list.append(float(element[powerPosition + 1::1]))
            # print("PowerList", powerList)

            self.__coeff_power_tuple=tuple(zip(self._coeff_list,self._power_list))

    def integral_rectangle(self,start,stop,step=1):
        count=int((stop-start)/step)
        array=[]
        suma=[]
        sumaIteracji=0.0;
        function = [start] * len(self.__coeff_power_tuple)
        #mapa = map(lambda x : x*2, function)
        #print(list(mapa))
        for i in range(0,count):
            for j in range(0, len(self.__coeff_power_tuple)):
                array.append(function[j] ** self._power_list[j])
                #print("Po potęgowaniu: ", array)
                suma.append(array[j]*self._coeff_list[j])
                #print("Suma: ",suma)
            print('Suma iteracji', sum( suma))
            sumaIteracji+= sum(suma)
            print("CALKA:",sumaIteracji)
            array=[]
            suma=[]
            start+=step
            function=[start]*len(self.__coeff_power_tuple)



        #print(function)
            #sum+=step*
        #sum=
        print(count)
        print(list(range(0,60)))

        return 0



#Listy odpowiednio ze współczynnikami i z potęgami


obj1=Polynomal('x+2')
print(obj1._reg_expr)
print(obj1.__dict__)
print(obj1.integral_rectangle(-2, 1,0.01))



'''
print(tuple(finalList))
sum=0.0
x=5.0
for value, power in finalList:
    if power==0:
        sum+=value
    else:
        sum+=float(value)*x**float(power)

print("Suma",sum)
'''




