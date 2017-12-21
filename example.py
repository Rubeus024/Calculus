
import re


class Polynomal:

    def __init__(self,str_reg_expr):
        self._reg_expr = str(str_reg_expr)
        self.derivative_str= ''
        self._coeff_list = []
        self._power_list = []
        self._coeff_der_list = []
        self._power_der_list = []
        self.create_coefficient()
        self.derivative_num = 0
        self.derivative()

    def show(self):
        for element in self.__dict__:
            print(element)

    def create_coefficient(self):
        self._reg_expr = ''.join([x for x in self._reg_expr if x != ' '])
        # Wzór reg. expression
        polynomal_parts = re.findall(r'[+\-]*\d*.\d*[a-zA-Z]*\^*\d*', self._reg_expr)
        # Umożliwia wpisanie każdej litery do konsoli (nie tylko x)
        recognized_letter = re.findall(r'[a-zA-Z]', self._reg_expr)[0]
        print("Wynik: ", recognized_letter)
        # Czyścimy string z niepotrzebnych spacji (po funkcji re.findall czasami pojawia się spacja lub dwie)
        polynomal_parts = [x for x in polynomal_parts if x != '']

        for element in polynomal_parts:
            x_position = element.find(recognized_letter)
            power_position = element.find('^')

            # w zależności od pozycji x dodajemy elementy do tablic
            if element.find(recognized_letter) == 0:
                self._coeff_list.append(1.0)
            # -1 oznacza brak znaku
            elif element.find(recognized_letter) == -1:
                self._coeff_list.append(float(element))
                self._power_list.append(0)  # nie ma x, potęga 0
            # print("Nowa polynomal_parts : ", coeffList)
            # print("PowerList", powerList)
            elif element.find(recognized_letter) == 1:
                
                self._coeff_list.append(1.0) if element[0] == '+' else self._coeff_list.append(-1.0)
                
            # reszta współczynników
            else:
                self._coeff_list.append(float(element[0:x_position:1]))
            # print("Nowa polynomal_parts : ", coeffList)

            if element.find('^') == -1 and element.find(recognized_letter) != -1:  # jeśli nie ma znaku a mamy potęge
                self._power_list.append(int(1))
            # print("PowerList111", powerList)
            elif element.find(recognized_letter) != -1:
                self._power_list.append(int(element[power_position + 1::1]))
            # print("PowerList", powerList)

            self._coeff_der_list = tuple(zip(self._coeff_list, self._power_list))

    def derivative(self):

        self.derivative_str = ''

        if self.derivative_num == 0:
            self._coeff_der_list = [coeff * y for coeff, y in zip(self._coeff_list, self._power_list)]
            self._coeff_der_list = [x for x in self._coeff_der_list if x != 0]
            self._power_der_list = [x-1 for x in self._power_list if x > 0]
            for i, element in enumerate(self._coeff_der_list):
                self.derivative_str += str(element) if element < 0 else '+'+str(element)
                self.derivative_str += 'x^'+str(self._power_der_list[i]) if self._power_der_list[i] >= 1 else ''
        else:
            self._coeff_der_list = [coeff * y for coeff, y in zip(self._coeff_der_list, self._power_der_list)]
            self._coeff_der_list = [x for x in self._coeff_der_list if x != 0]
            self._power_der_list = [x-1 for x in self._power_der_list if x > 0]
            for i, element in enumerate(self._coeff_der_list):
                self.derivative_str += str(element) if element < 0 else '+' + str(element)
                self.derivative_str += 'x^' + str(self._power_der_list[i]) if self._power_der_list[i] >= 1 else ''

        self.derivative_num += 1

    def reset_derivative(self):
        self.derivative_num=0;

    def integral_rectangle(self, start, stop, step=0.1):
        count = int((stop-start)/step)
        sum_rect = 0.0
        for i in range(0, count):
            function_list = [start] * len(self._coeff_list)
            x_power_result = [x**power for x, power in zip(function_list, self._power_list)]
            sum_rect += sum([x*y for x, y in zip(x_power_result, self._coeff_list)]) * step
            #print("Po potęgowaniu: ", x_power_result)
            #print("Prostokąto polu : ", sum_rect)
            start += step

        print("Liczba operacji: ", count)

        return sum_rect


obj1 = Polynomal('x^3 - 4x^2 + 6x - 24 ')
print(obj1.__dict__)
#print(obj1.integral_rectangle(0, 45, 0.01))
print(obj1._reg_expr)
print(obj1.derivative_str)
obj1.derivative()
print(obj1.derivative_str)
obj1.derivative()
print(obj1.derivative_str)

obj1.reset_derivative()
obj1.derivative()
print(obj1.derivative_str)



