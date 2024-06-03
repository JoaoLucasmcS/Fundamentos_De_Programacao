import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'clientes.json')




def cadastrar_clientes(nome , idade , email):
    with open(arquivo,'r') as arquivo_json:
        clientes = json.load(arquivo_json)

    clientes.append({'nome': nome, 'idade': idade, 'email': email}) 

    with open(arquivo,'w') as arquivo_json:
        json.dump(clientes, arquivo_json, indent=4)
        print("Usuário adicionado com sucesso.")    



def listar_clientes():
    with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
        clientes = json.load(arquivo_json)
    print(json.dumps(clientes, indent=4, ensure_ascii=False))    



def deletar_cliente(nome_cliente_removido):
    with open(arquivo, 'r') as arquivo_json:
        clientes = json.load(arquivo_json)

    for usuario in clientes:
        if usuario['Nome'] == nome_cliente_removido:
            clientes.remove(usuario)
            break

    with open(arquivo, 'w') as arquivo_json:
        json.dump(clientes, arquivo_json, indent=4)
        print("Usuário excluído com sucesso.")     



def main():
    print("MENU")
    print("1.Cadastrar Cliente")
    print("2.Listar Clientes")
    print("3.Deletar Cliente")
    resposta_menu = (int(input("Digite qual opção você deseja: ")))
    if resposta_menu == 1:
        nome = input("Nome do cliente: ")
        idade = input("Idade do cliente: ")
        email = input("Email do cliente: ")
        cadastrar_clientes(nome,idade,email)
    elif resposta_menu == 2:
        listar_clientes()
    elif resposta_menu == 3:
        nome_cliente_removido = input("Qual nome do cliente a ser removido: ")
        deletar_cliente(nome_cliente_removido)
    else: 
        print("Opção Inválida, Digite 1 , 2 ou 3")



if __name__ == "__main__":
    main()
