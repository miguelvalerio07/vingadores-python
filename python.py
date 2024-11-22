# escrever um programa que armazene as informações de três carros e apresente-as na tela para o usuário


class Carro:
    def __init__(self, modelo, ano, placa, marca, cor): # método construtor
        self.modelo = modelo # declaração de um atributo e atribuição de um valor
        self.ano = ano # variáveis de instância
        self.placa = placa
        self.marca = marca
        self.cor = cor


        def __str__(self):
            return f'{self.modelo} da empresa {self.marca}, ano {self.ano}, cor {self.cor} e placa {self.placa}'


palio = Carro('Palio', 1997, 'ABC1234', 'Fiat', 'Cinza sujo')
civic = Carro('Civic', 1998, 'DEF5678', 'Honda', 'Preto')
hb20 = Carro('HB20', 2016, 'GHJ9012', 'Toyota', 'Branco')
fusca= Carro('Fusca', 1991,'KLM3456', 'Volkswagen', 'Azul' )


print(palio)
print(civic)
print(hb20)
print(fusca)


print(f'Cor do carro 2 {civic.cor}')
print(f'Marca do carro 3 {hb20.marca}')
 