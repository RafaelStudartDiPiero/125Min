from models.config import Config


def test_config_select():
    # Caso Correto
    config = Config()
    result0 = config.selectConfig()
    assert result0 == "Configuração encontrada com sucesso."


def test_config_update():
    config0 = Config()
    config0.selectConfig()

    # Caso Correto
    config1 = Config(2, 2, 2, 2, 2, 2)
    result1 = config1.updateConfig
    assert result1 == "Configuração atualizada com sucesso."

    # Caso Incorreto - Alguma Entrada Negativa
    config2 = Config(-2, 2, 2, 2, 2, 2)
    result2 = config2.updateConfig
    assert result2 == "Ocorreu um erro na alteração da configuração"

    # Caso Incorreto - Número de Motoristas Menor que 1
    config3 = Config(2, 2, 2, 2, 2, 0)
    result3 = config3.updateConfig
    assert result3 == "Ocorreu um erro na alteração da configuração"

    # Voltando ao Estado Inicial
    config0.updateConfig

def test_config_requirements():
    config = Config()
    config.selectConfig()

    config1 = Config(2, 2, 2, 2, 2, 2)
    config1.updateConfig
    config1.selectConfig()
    assert config1.consumo_combustivel == 2

    config1.consumo_combustivel = -2
    config1.updateConfig
    config1.selectConfig()
    assert config1.consumo_combustivel == 2

    config1.consumo_combustivel = 5
    config1.updateConfig
    config1.selectConfig()
    assert config1.consumo_combustivel == 5

    # Voltando ao Estado Inicial
    config.updateConfig