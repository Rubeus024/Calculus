
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
        polynomal_parts = re.findall(r'[+\-]*\d*[a-z]*\^*\d*', self._reg_expr)
        # Czyścimy string z niepotrzebnych spacji (po funkcji re.findall czasami pojawia się spacja lub dwie)
        polynomal_parts = [x for x in polynomal_parts if x != '']

        for element in polynomal_parts:
            x_position = element.find('x')
            power_position = element.find('^')

            # w zależności od pozycji x dodajemy elementy do tablic
            if element.find('x') == 0:
                self._coeff_list.append(1.0)
            # -1 oznacza brak znaku
            elif element.find('x') == -1:
                self._coeff_list.append(float(element))
                self._power_list.append(0.0)  # nie ma x, potęga 0
            # print("Nowa polynomal_parts : ", coeffList)
            # print("PowerList", powerList)
            elif element.find('x') == 1:
                
                self._coeff_list.append(1.0) if element[0] == '+' else self._coeff_list.append(-1.0)
                
            # reszta współczynników
            else:
                self._coeff_list.append(float(element[0:x_position:1]))
            # print("Nowa polynomal_parts : ", coeffList)

            if element.find('^') == -1 and element.find('x') != -1:  # jeśli nie ma znaku a mamy potęge
                self._power_list.append(float(1))
            # print("PowerList111", powerList)
            elif element.find('x') != -1:
                self._power_list.append(float(element[power_position + 1::1]))
            # print("PowerList", powerList)

            self.__coeff_power_tuple = tuple(zip(self._coeff_list,self._power_list))

    def integral_rectangle(self, start, stop, step=0.1):
        count=int((stop-start)/step)
        sum_rect = 0.0

        for i in range(0, count):
            function_list = [start] * len(self.__coeff_power_tuple)
            x_power_result = [x**power for x, power in zip(function_list, self._power_list)]
            sum_rect += sum([x*y for x, y in zip(x_power_result, self._coeff_list)]) * step
            #print("Po potęgowaniu: ", x_power_result)
            #print("Prostokąto polu : ", sum_rect)
            start += step
        return sum_rect

obj1 = Polynomal(' x^2 - 4x +2x+ 1')
print(obj1.__dict__)
print(obj1.integral_rectangle(-2, 1, 0.1))

