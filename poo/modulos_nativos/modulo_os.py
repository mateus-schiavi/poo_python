import os

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
os.system('ver')

# 4 - Configurações das Máquinas
os.system('systeminfo')

# 5 - Limpar a Tela do Terminal
os.system('cls')

# 6 - Desligar o Computador
# os.system('shutdown /s')
# os.system('shutdown /s /t 0')
# # os.system(shutdown /a)


def turn_off_one_hour():
    os.system('shutdown /s /t 3600')


def turn_off_half_hour():
    os.system('shutdown /s /t 1800')


def cancel_shutdown():
    os.system('shutdown /a')


cancel_shutdown()
