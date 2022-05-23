def main():

    def operacoes():
        print("[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão ")
        operacao = int(input("\nSelecione a operação desejada: "))

        if operacao == 1:
            resultado = soma(valor1, valor2)
            print(resultado)
            opcoes()
        elif operacao == 2:
            resultado = subtracao(valor1, valor2)
            print(resultado)
            opcoes()
        elif operacao == 3:
            resultado = multiplicacao(valor1, valor2)
            print(resultado)
            opcoes()
        elif operacao == 4:
            resultado = divisao(valor1, valor2)
            print(resultado)
            opcoes()
        else:
            print("Opção inválida...")
            operacoes()

    def soma(valor1, valor2):
        soma = valor1 + valor2
        return soma

    def subtracao(valor1, valor2):
        subtracao = valor1 - valor2
        return subtracao

    def multiplicacao(valor1, valor2):
        multiplicacao = valor1 * valor2
        return multiplicacao

    def divisao(valor1, valor2):
        divisao = valor1 / valor2
        return divisao

    def opcoes():
        opcao = int(input("Tecle 1 para continuar ou 0 para encerrar: "))

        if opcao == 1:
            main()
        else:
            print("Encerrando aplicação... ")

    valor1 = float(input("Informe o primeiro valor: "))
    valor2 = float(input("Informe o segundo valor: "))
    operacoes()


main()