import os

# importação as classes
from pessoa import *
from manipulador import *

if __name__ == "__main__":
    # imstancia os objetos
    p = Pessoa(0,'','','','')
    m = Manipulador()

    while True:
        print("1 - Criar novo arquivo JSON: ")
        print("2 - Abrir e ler arquivo JSON: ")
        print("3 - Salvar novo usuario: ")
        print("4 - Alterar dados: ")
        print("5 - Deletar usuario: ")
        print("0 - Sair do programa: ")

        opcao = input("Informe a opção desejada: ")

        # limpeza do console
        os.system("cls")

        match opcao:
            case "0":
                print("Programa encerrado.")
                break
            case "1":
                novo_arquivo = input("Informe o nome do arquivo de deseja criar: ")
                print(m.criar_arquivo(novo_arquivo))
                continue
            case "2":
                abrir_arquivo = input("Informe o nome so arquivo deseja abrir: ")
                try:
                    os.system("cls")
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f"Arquivo aberto: {abrir_arquivo}.jason.\n")
                    for i in range(len(usuarios)):
                        for campo in usuarios[i]:
                            print(f"{campo.capitalize()}: {usuarios[i].get(campo)}.")
                        print(f"\n{'-'*30}\n")
                except Exception as e:
                    print(f"Não soi possivel abrir o arquivo. {e}.")
                finally:
                    continue
            case "3":
                try:
                    usuario = {}
                    campos = ('nome', 'cpf', 'email', 'profissao')
                    print(f"Arquivo aberto: {abrir_arquivo}.jason.\n")
                    usuario['codigo'] = len(usuarios)
                    for campo in campos:
                        usuario[campo] = input(f"Informe o campo {campo.capitalize()}: ")
                    
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f"Não soi possivel realizar a operação. {e}.")
                finally:
                    continue

            case "4":
                try:
                    print(f"Arquivo aberto: {abrir_arquivo}.json.\n")
                    codigo = int(input("Informe o código so usuario que deseja alterar os dados: "))
                    for campo in usuarios[codigo]:
                        print(f"Valor atual do campo {campo}: {usuarios[codigo].get(campo)}")
                        novo_dado = input(f"Informe o novo dado do campo {campo} ou aperte 'Enter' caso deseje manter o mesmo valor: ")
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado
                        else:
                            ...

                    print(m.salvar_dados(usuarios, abrir_arquivo))   
                except Exception as e:
                    print(f"Não soi possivel alterar dados. {e}.")
                finally:
                    continue
            case "5":
                try:
                    print(f"Arquivo aberto: {abrir_arquivo}.json. \n")
                    codigo =  int(input("Informe o codigo que deseja deletar: "))
                    nome_deletado = usuarios[codigo]['nome']
                    confirmacao = input(f"Deseja deletar o usuario {nome_deletado}?  Digite 'SIM' para confirmar ou digite qualuqer coisa para cancelar.")
                    if confirmacao == 'SIM':
                        del(usuarios[codigo])
                        print(m.salvar_dados(usuarios, abrir_arquivo))
                        print(f"Usuário {nome_deletado} deletado com sucesso!!")

                    else:
                        print(f"Usuário {nome_deletado} não foi excluido.")


                except Exception as e:
                    print(f"Não soi possivel deletar usuario. {e}.")

                finally:
                    continue

            case _:
                print("Opção invalida.")
                continue

