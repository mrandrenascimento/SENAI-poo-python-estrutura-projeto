import os

from models.enums.sexo import Sexo
from models.pessoa import Pessoa
os.system("cls||clear")

#Instanciando a Classe
pessoa_1 = Pessoa("Marta",22,Sexo.FEMININO)
print(pessoa_1)