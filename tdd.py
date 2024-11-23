######## CODIGO DE TESTES ###################
#Funcao de Soma
def soma(num1, num2):
    result = num1 + num2
    return result

### TESTES
import unittest
class TestMathOperations(unittest.TestCase):
    def teste(self):
        #Recebendo funcao soma na variavel
        adicao = soma(num1 = 10, num2 = 30)
        #Resultado experado
        self.assertEqual(adicao, 40)

###
if __name__ == '__main__':
    unittest.main()