import pytest
from flyup import menu, passageiros, pagamentos_abertos, pagamentos_efetuados, comprar, admin, confirmar_pagamento

def test_comprar_passagem_paris(monkeypatch):
    global passageiros, pagamentos_abertos, pagamentos_efetuados
    # Limpa as listas globais antes de iniciar o teste
    passageiros.clear()
    pagamentos_abertos.clear()
    pagamentos_efetuados.clear()

    # Simula as entradas do usuário: escolha de destino, 2 pacotes, 'João da Silva', 'Maria Souza'
    inputs = iter([1, 2, 'João da Silva', 'Maria Souza'])
    def mock_input(prompt):
        value = next(inputs)
        return str(value) if isinstance(value, int) else value

    monkeypatch.setattr('builtins.input', mock_input)
    # Chama a função de comprar passagem
    comprar()

    # Verifica se os passageiros foram adicionados corretamente
    assert 'JOÃO DA SILVA' in passageiros
    assert 'MARIA SOUZA' in passageiros
    # Verifica se os pagamentos estão em aberto
    assert pagamentos_abertos['JOÃO DA SILVA'] == 'Pagamento em aberto'
    assert pagamentos_abertos['MARIA SOUZA'] == 'Pagamento em aberto'

def test_confirmar_pagamento(monkeypatch):
    global passageiros, pagamentos_abertos, pagamentos_efetuados
    # Limpa as listas globais antes de iniciar o teste
    passageiros.clear()
    pagamentos_abertos.clear()
    pagamentos_efetuados.clear()

    # Adiciona um passageiro e marca o pagamento como em aberto
    passageiros['JOÃO DA SILVA'] = 'PARIS'
    pagamentos_abertos['JOÃO DA SILVA'] = 'Pagamento em aberto'

    # Simula a entrada do usuário: nome do passageiro para confirmar pagamento
    inputs = iter(['JOÃO DA SILVA'])
    def mock_input(prompt):
        value = next(inputs)
        return str(value) if isinstance(value, int) else value

    monkeypatch.setattr('builtins.input', mock_input)
    # Chama a função para confirmar pagamento
    confirmar_pagamento()

    # Verifica se o pagamento foi confirmado e atualizado corretamente
    assert 'JOÃO DA SILVA' not in pagamentos_abertos
    assert 'JOÃO DA SILVA' in pagamentos_efetuados
    assert pagamentos_efetuados['JOÃO DA SILVA'] == 'Pagamento efetuado'

def test_admin(monkeypatch):
    global passageiros, pagamentos_abertos, pagamentos_efetuados
    # Limpa as listas globais antes de iniciar o teste
    passageiros.clear()
    pagamentos_abertos.clear()
    pagamentos_efetuados.clear()

    # Adiciona um passageiro e marca o pagamento como em aberto
    passageiros['JOÃO DA SILVA'] = 'PARIS'
    pagamentos_abertos['JOÃO DA SILVA'] = 'Pagamento em aberto'

    # Simula as entradas do usuário: senha do admin, opção de ver pagamentos, nome do passageiro
    inputs = iter(['2022', 4, 'JOÃO DA SILVA', 0])
    def mock_input(prompt):
        value = next(inputs)
        return str(value) if isinstance(value, int) else value

    monkeypatch.setattr('builtins.input', mock_input)
    # Chama a função de admin
    admin()

    # Verifica se o pagamento foi confirmado e atualizado corretamente
    assert 'JOÃO DA SILVA' not in pagamentos_abertos
    assert 'JOÃO DA SILVA' in pagamentos_efetuados
    assert pagamentos_efetuados['JOÃO DA SILVA'] == 'Pagamento efetuado'
