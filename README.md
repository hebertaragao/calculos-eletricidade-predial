# calculos-eletricidade-predial
Cálculos para toda a infraestrutura predial.


pip install cx_Freeze

Crie um setup script com o código abaixo
from cx_Freeze import setup, Executable

# Substitua "seu_script.py" pelo nome do seu arquivo Python
executables = [Executable("seu_script.py")]

setup(
    name="NomeDoSeuPrograma",
    version="0.1",
    description="Descrição do seu programa",
    executables=executables
)
Fim do código para o setup.py

por ultimo rode esse comando
python setup.py build
