LIMITE = 9  # TROQUE pelo seu LIMITE


def pode_emprestar(quantidade):
    if quantidade < 1:
        return False
    return quantidade <= LIMITE
