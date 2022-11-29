'''

Fixtures são funções especiais que o Pytest chama antes dos casos de testes
Uma Fixture sempre retorna um valor
Injeção de dependencia
Cada fixture deve ter um nome unico
Por padrão o scope é por function
Se mudarmos o SCOPE para ''session'' a fixture é executada apenas uma vez para
o conjunto de testes, ou seja, em um conjunto que utilize a mesma
fixture o Pytest executará apenas uma vez, armazenando seu valor para ser usado
nos outros testes. Pode ser bom para a leitura de dados de um arquivo externo.
Outros niveis de escopo são CLASS, MODULE e PACKAGE.

MONKEYPATCH - modifica temporariamente classes, funções , dicionarios,
 ambientes e outros objetos

 REQUEST fornece metadados

'''
import pytest

from pythonBasics.pytest.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError) as error:
        accum.count = 10
