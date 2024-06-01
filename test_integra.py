import pytest
from flyup import passagem_paris, passageiros, paris

def test_passagem_paris(monkeypatch):
    global paris, passageiros
    paris.clear()
    passageiros.clear()

    # Simula as entradas do usuário:
    input_data = iter([2, 'João da Silva', 'Maria Souza'])
    monkeypatch.setattr('builtins.input', lambda _: next(input_data))

    # Chama a função que será testada
    passagem_paris()

    # Verifica se dois pacotes foram adicionados à lista 'paris'
    assert len(paris) == 2
    # Verifica se os passageiros 'JOÃO DA SILVA' e 'MARIA SOUZA' foram adicionados corretamente
    assert 'JOÃO DA SILVA' in passageiros
    assert 'MARIA SOUZA' in passageiros
