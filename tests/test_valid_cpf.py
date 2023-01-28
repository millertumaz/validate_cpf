import sys
from pathlib import Path

from src.controller.index import ValidateCPF

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


def test_validate_cpf_with_punctuation():
    assert ValidateCPF('066.752.150-00').validates()


def test_validate_cpf_no_punctuation():
    assert ValidateCPF('06675215000').validates()


def test_validate_cpf_invalid_character():
    assert ValidateCPF('0667521500a').validates() is False
