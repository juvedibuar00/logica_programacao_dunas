# programa.py

import utilidades  # Importa o módulo inteiro

def main():
    a = utilidades.ler_numero("Digite o primeiro número: ")
    b = utilidades.ler_numero("Digite o segundo número: ")
    resultado = utilidades.somar(a, b)
    utilidades.exibir_resultado(resultado)

main()
