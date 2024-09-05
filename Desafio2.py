"""Aqui temos uma função que executa outras duas sendo a da criação da seuqncia e a segunda que verica se o numero existe nessa sequencia"""
def verificar_fibonacci():
    """Criação da sequencia fibonacci"""
    def fibonacci_sequencia(limite):
        fib_seq = [0, 1]
        while fib_seq[-1] < limite:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    
    """Verificação do numero digitado, se ele existe dentro da lista de números"""
    def is_in_fibonacci(numero):
        
        fib_seq = fibonacci_sequencia(numero)
        if numero in fib_seq:
            return f"O número {numero} pertence à sequência de Fibonacci."
        else:
            return f"O número {numero} não pertence à sequência de Fibonacci."
    
    try:
        num = int(input("Informe um número: "))
        """Aqui ele irá executar a função para realizar a verificação apartir do numero digitado pelo usuario"""
        resultado = is_in_fibonacci(num)
        print(resultado)
    except ValueError:
        print("Erro: Por favor, informe um número válido.")
        

verificar_fibonacci()



    



