# gabriel = Desenvolvedor('GAbriel', 'fulano@gmail.com', 'FBVCD$45', 3650, 'Python')
# eva = Desenvolvedor('Erva', "Evinha#gmail.com", 'EFGR666', 1000, 'Java')
# ana = GerenteProjeto('Ana Maria', 'aninha@gmail.com', 'RTFD432', 4000)

class Empregado:
    numero_empregados = 0                                                                                                 # Atributo de classe para contagem dos funcionários.

    def __init__(self, nome_completo:str, email: str, matricula: str, salario:float):                                     # Método construtor da class pai "Empregado".
        self.nome_completo = nome_completo
        self.email = email
        self.matricula = matricula
        self.salario = salario
        self.trabalhando = False
        Empregado.numero_empregados += 1

    def iniciar_trabalho(self):                                                                                           # Método iniciar trabalho que será herdado pelos objetos das classes filha.
        if not self.trabalhando:
            self.trabalhando = True
            print(f'O funcionário {self.nome_completo} começou a trabalhar!')
        else:
            print(f'Funcionário {self.nome_completo} já está em trabalho!')

    def finalizar_trabalho(self):                                                                                         # Método finalizar trabalho que será herdado pelos objetos das classes filha.
        if self.trabalhando:
            self.trabalhando = False
            print(f'O funcionário {self.nome_completo} parou de trabalhar.')
        else:
            print(f'O funcionário {self.nome_completo} não está trabalhando no momento.')

    def receber_aumento(self):                                                                                           # Método para receber aumento que será empregado diferentemente em cada uma das classes, dependendo
        raise NotImplemented                                                                                             # do parametro de classe das classes filhas, irá retornar valores de aumentos diferentes.


class Desenvolvedor(Empregado):                                                                                          # Class 'filha' da class "Empregado", possui seus próprios parâmetros, bem como métodos tbm.
    pct_aumento = 1.16
    desenvolvedores = {}

    def __init__(self, nome_completo: str, email: str, matricula: str, salario: float, linguagem, burnout=False):        # Método inicializador recebendo os parâmetros da classe pai e também seus próprios parâmetros
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula, salario)
        self.linguagem = []
        self.litros_cafe = 0.0
        self.burnout = burnout
        self.linguagem.append(linguagem)
        Desenvolvedor.desenvolvedores.update({self.matricula: self.nome_completo})
        print(f'Funcionário {self.nome_completo} matrícula {self.matricula} cadastrado com sucesso!')

    def add_linguagem(self, nome_linguagem):                                                                             # Adicionando uma linguagem de programação á lista do objeto
        self.linguagem.append(nome_linguagem)
        print(f'{self.nome_completo} aprendeu uma nova linguagem de programação --> {nome_linguagem}')

    def toma_cafe(self, qtd_cafe: float):                                                                                # Método tomar cafá, que dependendo da quantidade de litros tomado ativa o burnout, passado como booleano
        print(f'{self.nome_completo} está tomando café')
        self.litros_cafe += qtd_cafe
        if self.litros_cafe >= 3:
            self.burnout = True

    def receber_aumento(self):                                                                                           # Receber aumento utilizando o atributo de classe de aumento para Desenvolvedores.
        novo_salario = Desenvolvedor.pct_aumento * self.salario
        self.salario = novo_salario
        print(f'O Desenvolvedor {self.nome_completo} foi bonificado com um aumento de {Desenvolvedor.pct_aumento}%')


class GerenteProjeto(Empregado):                                                                                         # Class 'filha' da class "Empregado", possui seus próprios parâmetros, bem como métodos tbm.
    pct_aumento = 1.3

    def __init__(self, nome_completo: str, email: str, matricula: str, salario: float):                                  # Método inicializador recebendo os parâmetros da classe pai e também seus próprios parâmetros
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula, salario)
        self.time = {}
        self.projetos = []

    def receber_aumento(self):                                                                                           # Receber aumento utilizando o atributo de classe de aumento para Gerente de Projeto.
        novo_salario = GerenteProjeto.pct_aumento * self.salario
        self.salario = novo_salario
        print(f'O Gerente de Projeto {self.nome_completo} foi bonificado com um aumento de {GerenteProjeto.pct_aumento}%')

    def add_dev(self, cadastro):                                                                                         # Método que adiciona um desenvolvedor da lista de Desenvolvedores criada na class anterior
        if cadastro in Desenvolvedor.desenvolvedores:                                                                    # ao  time do gerente em questão
            self.time.update({cadastro: Desenvolvedor.desenvolvedores[cadastro]})
        else:
            print('Não existe esse registro em nosso sitema')

    def remove_dev(self, cadastro):                                                                                      # Método que remove desenvolvedor do time.
        if cadastro in self.time:
            self.time.pop(cadastro)
            print(f'O Dev. registro {cadastro} foi removido do time.')
        else:
            print(f'Não há nenhum Dev com esse registro...')

    def participar_projeto(self, projeto):                                                                               # Método que inicia novos projetos e da entrada com esse projeto na lista de projetos passada como parametro
        if projeto not in self.projetos:
            self.projetos.append(projeto)
        else:
            print(f'Você já está participando de um projeto com esse nome. Verifique novamente.')

    def sair_projeto(self, projeto):                                                                                     # Mapeia todos os projetos procurando o que foi passado por parametro e utiliza os indices
        if projeto in self.projetos:                                                                                     # da lista para remoção, caso exista o projeto.
            for k, v in enumerate(self.projetos):
                if v == projeto:
                    del self.projetos[k]
                else:
                    pass
        else:
            print(f'você não esta em nenhum projeto com esse nome')

