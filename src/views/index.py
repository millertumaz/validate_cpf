import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.index import ValidateCPF

print('\n*To exit type "exit"*\n')
while True:  

    cpfInput = input('Insert the cpf (only number): ')

    if cpfInput == 'exit':
        sys.exit()
    else:
        cpf = ValidateCPF(cpfInput)

        if cpf.validates():
            print(f'✓ CPF: {cpfInput} is valid.\n')
        else:
            print(f'☓ CPF: {cpfInput} is invalid.\n')
