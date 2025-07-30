import os
lugares = {
    "lugares": ["Museu", "Jockey Club"],
    "datas": ['15/07', '12/07']
}
barra = f'|{"_"*40}|'
def mostrar_lugares():
    print(barra)
    print("| " \
    "LUGARES PARA TURISTAR                  |")
    for n in range(len(lugares["lugares"])):
        print(f"| {n+1}. {lugares['lugares'][n]} - {lugares['datas'][n]}")
    print(barra)

def adcionar_na_lista():
    
    resp1=input('| Digite o lugar que gostaria de adcionar:')
    resp2=input('| Quando gostaria de ir :')
    lugares["lugares"].append(resp1)
    lugares["datas"].append(resp2)
    



def apagar_da_lista():
    mostrar_lugares()
    
    retira=int(input('| Digite o número que será removido:'))
    lugar_removido =lugares["lugares"].pop(retira-1)
    lugares["datas"].pop(retira-1)
    print(f'| "{lugar_removido}" foi removido com sucesso')
    

 
def mostrar_opcoes():
    
        while True:
            os.system('cls')
            print("|__OPÇÕES_________________________|")
            print("|_________________________________|")
            print("|")
            print("| (1) Ver lista")
            print("| (2) Adicionar na lista")
            print("| (3) Apagar da lista ")
            print("| (4) Sair ")
            print("|__________________________________|")
            try:   
                opc=int(input("| Digite a opção:"))
                if opc == 1:
                    os.system('cls')
                    mostrar_lugares()
                    input('| Digite enter para continuar...')
                elif opc == 2:
                    adcionar_na_lista()
                    input('| Digite enter para continuar...')
                elif opc == 3:
                    os.system('cls')
                    apagar_da_lista()
                    input('| Digite enter para continuar...')
                elif opc == 4:
                    print('| Saindo...')
                    break

                else:
                    print("| Invalido, digite um número")
                    input('| Digite enter para continuar...')
            except:
                print('| Comando invalido')
                input('| Digite enter para continuar...')


mostrar_opcoes()    