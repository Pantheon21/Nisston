def fibonacci(n):
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] + fibonacci_seq[-2] <= n:
        next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_term)
    return fibonacci_seq

limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))
seq_fibonacci = fibonacci(limite)
print("Sequência de Fibonacci:", seq_fibonacci)
