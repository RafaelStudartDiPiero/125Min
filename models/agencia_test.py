from models.agencia import Agencia
# Duas agencias modelo, uma que vai ser adiciona, atualizada, selecionada e removida e outra que nunca existira.


def test_agencia_insert():
    # Caso Correto
    agencia0 = Agencia(rua="Rua H8A", numero="125",
                       cidade="São José dos Campos", cep="12228-460")
    result0 = agencia0.inserirAgencia()
    assert result0 == "Agência cadastrada com sucesso."

    # Caso Incorreto - Número não é número
    agencia1 = Agencia(rua="Rua H8A", numero="abbba",
                       cidade="São José dos Campos", cep="12228-460")
    result1 = agencia1.inserirAgencia()
    assert result1 == "Ocorreu um erro na inserção de uma agência"

    # Caso Incorreto - CEP Inválido
    agencia2 = Agencia(rua="Rua H8A", numero="125",
                       cidade="São José dos Campos", cep="12228-aba")
    result2 = agencia2.inserirAgencia()
    assert result2 == "Ocorreu um erro na inserção de uma agência"


def test_agencia_update():
    # Caso Correto
    agencia0 = Agencia(rua="Rua H8A", numero="126",
                       cidade="São José dos Campos", cep="12228-460")
    result0 = agencia0.updateAgencia
    assert result0 == "Agência atualizada com sucesso."

    # Caso Incorreto - Número não é número
    agencia1 = Agencia(rua="Rua H8A", numero="aaa",
                       cidade="São José dos Campos", cep="12228-460")
    result1 = agencia1.updateAgencia
    assert result1 == "Ocorreu um erro na alteração de uma agência"

    # Caso Incorreto - CEP inválido
    agencia2 = Agencia(rua="Rua H8A", numero="125",
                       cidade="São José dos Campos", cep="12228-aba")
    result2 = agencia2.updateAgencia
    assert result2 == "Ocorreu um erro na alteração de uma agência"

    # Caso Incorreto - Agência Inexistente
    agencia3 = Agencia(rua="Rua H8A", numero="125",
                       cidade="São José dos Campos", cep="00000-000")
    result3 = agencia3.updateAgencia
    assert result3 == "Ocorreu um erro na alteração de uma agência"


def test_agencia_select():
    # Caso Correto
    agencia0 = Agencia(rua="Rua H8A", numero="126",
                       cidade="São José dos Campos", cep="12228-460")
    result0 = agencia0.selectAgencia(agencia0.cep)
    assert result0 == "Agência encontrada com sucesso."

    # Caso Incorreto - Agência Inexistente
    agencia1 = Agencia(rua="Rua H8A", numero="126",
                       cidade="São José dos Campos", cep="00000-000")
    result1 = agencia1.selectAgencia(agencia1.cep)
    assert result1 == "Ocorreu um erro na busca de uma agência"


def test_agencia_delete():
    # Caso Correto
    agencia0 = Agencia(rua="Rua H8A", numero="126",
                       cidade="São José dos Campos", cep="12228-460")
    result0 = agencia0.deleteAgencia
    assert result0 == "Agência excluída com sucesso."

    # Caso Incorreto - Agência Inexistente
    result1 = agencia0.deleteAgencia
    assert result1 == "Ocorreu um erro na exclusão de uma agência"