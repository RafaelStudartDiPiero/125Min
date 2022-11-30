from models.agencia import Agencia
# Duas agencias modelo, uma que vai ser adiciona, atualizada, selecionada e removida e outra que nunca existira.


def test_agencia_insert():
    # Caso Correto
    agencia0 = Agencia(rua="Rua H8A",numero="125",cidade="São José dos Campos",cep="12228-460")
    result0 = agencia0.inserirAgencia()
    assert result0 == "Agência cadastrada com sucesso."

    # Caso Incorreto - Número não é número
    agencia1 = Agencia(rua="Rua H8A",numero="abbba",cidade="São José dos Campos",cep="12228-460")
    result1 = agencia1.inserirAgencia()
    assert result1 == "Ocorreu um erro na inserção de uma agência"

    # Caso Incorreto - CEP Inválido
    agencia2 = Agencia(rua="Rua H8A",numero="125",cidade="São José dos Campos",cep="12228-aba")
    result2 = agencia2.inserirAgencia()
    assert result2 == "Ocorreu um erro na inserção de uma agência"

def test_agencia_update():
    # Caso Correto
    pass

    # Caso Incorreto - Número não é número

    # Caso Incorreto - CEP inválido

    # Caso Incorreto - Agência Inexistente

def test_agencia_delete():
    # Caso Correto 
    pass

    # Caso Incorreto - Agência Inexistente


def test_agencia_select():
    # Caso Correto
    pass

    # Caso Incorreto - Agência Inexistente