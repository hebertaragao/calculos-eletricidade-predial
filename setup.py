from cx_Freeze import setup, Executable

# Substitua "seu_script.py" pelo nome do seu arquivo Python
executables = [Executable("calculo_predial.py")]

setup(
    name="CalculoPredial",
    version="0.1",
    description="Calculo para eletrotécnicos",
    executables=executables
)
