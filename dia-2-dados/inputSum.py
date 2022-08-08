# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores. 7
# Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída 
# de erros no seguinte formato: "Erro ao somar valores, {valor} é um valor inválido". 
# Ao final, você deve imprimir a soma dos valores válidos.

# Receba os valores em um mesmo input, solicitando à pessoa usuária que separe-os com um espaço. 
# Receba os valores no formato str e utilize o método split para pegar cada valor separado. 
# O método isdigit, embutido no tipo str, pode ser utilizado para verificar se a string corresponde a um número natural.


def sum_numbers():
    numbers = input('Digite os números, separados por espaço: ')

    split_numbers = numbers.split()
    sum = 0

    for number in split_numbers:
        if(number.isdigit() == False):
            return print(f'Erro ao somar valores. {number} é um valor inválido')
        
        sum = sum + int(number)

    return print(f'A soma é: {sum}')

sum_numbers()