import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Pessoa:
    def __init__(self, ent_pessoa, ent_visit):
        self.ent_pessoa = ent_pessoa
        self.ent_visit = ent_visit

class pessoa_morador:
    def __init__(self, nome_mor, apt_mor, tel_mor, car_mor, doc_mor):

        self._nome_mor = nome_mor
        self.apt_mor = apt_mor
        self.tel_mor = tel_mor
        self.car_mor = car_mor
        self._doc_mor = doc_mor
        self.indice_morador = 0

    @classmethod
    def novo_morador(cls, nome_mor):
        return cls(nome_mor)
    
    @property
    def novo_morador_apt(self):
        return self.apt_mor
    
    @property
    def novo_tel_morador(self):
        return self.tel_mor
    
    @property
    def novo_car_mor(self):
        return self.car_mor
    
    @property
    def novo_doc_mor(self):
        return self._doc_mor
    



class pessoa_visit:
    def __init__(self, nome_visit, apt_visit, tel_visit, sai_visit, car_visit, doc_visit):

        self._nome_visit = nome_visit
        self.apt_visit = apt_visit
        self.tel_visit = tel_visit
        self.car_visit = car_visit
        self.sai_visit = sai_visit
        self._doc_visit = doc_visit

    @classmethod
    def novo_visitante(cls, nome_visit):
        return cls(nome_visit)
    
    @property
    def novo_apt_visit(self):
        return self.apt_visit
    
    @property
    def novo_tel_visit(self):
        return self.tel_visit
    
    @property
    def novo_car_visit(self):
        return self.car_visit
    
    @property
    def novo_saida_visit(self):
        return self.sai_visit



def menu():
    menu = """\n
    ===== CONTROLE DE PESSOAS =====
    
    [m] MORADORES
    [v] VISITANTES

    ===============================
    
    ==> """
    return input(textwrap.dedent(menu))

def criar_morador(moradores):
    nome_morador = input("Nome completo: ")
    doc_morador = input("Documento (somente numeros): ")
    apt_morador = input("Apartamento/Casa: ")
    car_morador = input("Carro (Placa): ")
    tel_morador = input("Telefone: ")

    morador = pessoa_morador(nome_mor=nome_morador, doc_mor=doc_morador, apt_mor=apt_morador, car_mor=car_morador, tel_mor=tel_morador)
    moradores.append(morador)

    print("\n===== Morador cadastrado com sucesso!=====")

def criar_visitante(visitantes):
    nome_visitante = input("Nome completo: ")
    doc_visitante = input("Documento (somente numeros): ")
    apt_visitante = input("Apartamento: ")
    car_visitante = input("Carro (Placa): ")
    tel_visitante = input("Telefone: ")
    saida_visitante = input("Data de saída: ")

    visitante = pessoa_visit(nome_visit=nome_visitante, doc_visit=doc_visitante, apt_visit=apt_visitante, car_visit=car_visitante, tel_visit=tel_visitante, sai_visit=saida_visitante)
    visitantes.append(visitante)

def filtrar_por_apartamento(lista, tipo="morador"):
    busca_apt = input(f"Digite o número do Apartamento/Casa para filtrar: ").strip()
    encontrados = []

    for pessoa in lista:
        # Verifica o atributo de apartamento dependendo do tipo
        apt_atual = pessoa.apt_mor if tipo == "morador" else pessoa.apt_visit
        
        if apt_atual == busca_apt:
            encontrados.append(pessoa)

    if not encontrados:
        print(f"\n[!] Nenhum {tipo} localizado no apartamento {busca_apt}.")
    else:
        print(f"\n=== {tipo.upper()}S NO APARTAMENTO {busca_apt} ===")
        for p in encontrados:
            # Exibe os detalhes
            if tipo == "morador":
                print(f"Nome: {p._nome_mor} | Tel: {p.tel_mor} | Carro: {p.car_mor}")
            else:
                print(f"Visitante: {p._nome_visit} | Tel: {p.tel_visit}")


def menu2():
    menu2 = """\n
            ===== MORADORES =====
            [cm] CADASTRAR NOVO MORADOR
            [bm] BUSCAR MORADOR
            [re] VOLTAR AO MENU ANTERIOR
            
            ==> """
    return input(textwrap.dedent(menu2))

def menu3(moradores):
    return criar_morador(moradores)

def menu4():
    return filtrar_por_apartamento

def menu5():
    menu5 = """\n
            ===== VISITANTES =====
            [cv] CADASTRAR NOVO VISITANTE
            [bv] BUSCAR VISITANTE
            [re] VOLTAR AO MENU ANTERIOR
            
            ==> """
    return input(textwrap.dedent(menu5))


def menu6():
    return filtrar_por_apartamento


def main():
    moradores = []
    visitantes = []

    while True:
        opcao = menu().lower()

        if opcao == "m":

            escolha = menu2()

            if escolha == "cm":
                criar_morador(moradores)
            
            elif escolha == "bm":
                filtrar_por_apartamento(moradores, tipo="morador")
            
            elif escolha == "re":
                continue  
            
            else:
               print("@@@ Opção inválida! @@@")
               return 

        
        elif opcao == "v":
            escolha2 = menu5()

            if escolha2 == "cv":
                criar_visitante(visitantes)

            elif escolha2 == "bv":
                filtrar_por_apartamento(visitantes, tipo="visitantes")

            elif escolha2 == "re":
                continue
            
            else:
                print("@@@ Opção inválida! @@@")
                return
        
        else:
            print ("@@@ Opção inválida! @@@")


main()