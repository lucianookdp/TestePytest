import pytest
from flyup import compra_paris, nome_passageiro_paris, somaparis, passageiros, pagamentos_abertos, paris

def test_compra_paris():
    global paris
    paris.clear() 
    compra_paris(2)
    assert len(paris) == 2

def test_nome_passageiro_paris(monkeypatch):
    global passageiros, pagamentos_abertos
    passageiros.clear()
    pagamentos_abertos.clear()

    # Simula a entrada do usuário para o nome do passageiro
    input_data = 'João da Silva'
    monkeypatch.setattr('builtins.input', lambda _: input_data)

    # Chama a função para registrar o passageiro
    nome_passageiro_paris()

    # Verifica se o passageiro foi adicionado corretamente
    assert 'JOÃO DA SILVA' in passageiros
    assert passageiros['JOÃO DA SILVA'] == 'PARIS'

    # Verifica se o pagamento está marcado como em aberto
    assert pagamentos_abertos['JOÃO DA SILVA'] == 'Pagamento em aberto'

def test_somaparis():
    # Verifica se a soma dos preços dos pacotes para Paris está correta
    assert somaparis(2) == 2 * 3499.90

