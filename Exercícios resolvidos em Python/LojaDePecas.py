#Este programa simula um sistema automatizado para que os clientes façam pedidos de forma automática.

def mostraMenuDeOpcoes():
    print("|--CÓDIGO--|-----------ITEM-----------|----PREÇO-R$-|")
    print("|-----1----|-------Bateria------------|-----200,00--|")
    print("|-----2----|-------Pneu---------------|-----350,00--|")
    print("|-----3----|-------Filtro de Óleo-----|-----50,00---|")
    print("|-----4----|-------Pastilha de Freio--|-----100,00--|")
    print("|-----5----|-------Sair do Sitema-----|-------------|")

def funcionamentoDoSistema(): 
    resposta = "s"
    preco1 = preco2 = preco3 = preco4 = 0
    while(resposta == 's' or resposta == 'S'):
    
        codigoDoProduto = int(input("Escolha um produto: "))
        match(codigoDoProduto):
         case 1:
            quantidade = int(input("Quantas baterias você deseja comprar?"))
            preco1 = quantidade*200
         case 2:
            quantidade = int(input("Quantos pneus você deseja comprar?"))
            preco2 = quantidade*350
         case 3:
            quantidade = int(input("Quantos filtros de óleo você deseja comprar?"))
            preco3 = quantidade*50
         case 4:
            quantidade = int(input("Quantas pastilhas de freio você deseja comprar?"))
            preco4 = quantidade*100
         case 5:
            print("Saindo do Sitema")
         case __:
            print("Código inválido")
        resposta = str(input("Você deseja realizar outro pedido? (S/N)"))
    precoFinal = preco1 + preco2 + preco3 + preco4
    print("O valor da sua compra foi:  R$",precoFinal)

def main():
   mostraMenuDeOpcoes()
   funcionamentoDoSistema()

if __name__ == "__main__":
   main()








    
            

