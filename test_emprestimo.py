from emprestimo import pode_emprestar, LIMITE


def test_quantidade_igual_ao_limite_e_aceita():
    # preparar
    quantidade = LIMITE
    # agir
    resultado = pode_emprestar(quantidade)
    # verificar
    assert resultado is True


def test_quantidade_acima_do_limite_e_rejeitada():
    # preparar
    quantidade = LIMITE + 1
    # agir
    resultado = pode_emprestar(quantidade)
    # verificar
    assert resultado is False


def test_quantidade_zero_e_rejeitada():
    # preparar
    quantidade = 0
    # agir
    resultado = pode_emprestar(quantidade)
    # verificar
    assert resultado is False
