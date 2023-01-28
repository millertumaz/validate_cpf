# Validate CPF

The purpose of the CPF validator is to assist students, developers and analysts in testing software under development.

## Example of use
##### Using with user input

```python
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
        cpf = ValidateCPF(cpfInput).validates() # Boolean return : True or False

        if cpf:
            print(f'✓ CPF: {cpfInput} is valid.\n')
        else:
            print(f'☓ CPF: {cpfInput} is invalid.\n')

```


## Project layout
    validate_cpf/
        docs/
            index.md
        src/
            controller/
                index.py
            views/
                index.py
        tests/
            __init__.py
            test_valid_cpf.py
        LICENSE
        mkdocs.yml
        pyproject.toml
        README.md
