# Aprendendo Python

## Saída
```python
print("Hello world!")
```

## Entrada 
```python
input("Digite seu nome: ")
```
> obs.: Os dados entram como string

## Converter dados

Uma forma já é deixar explícito o tipo de dados, por exemplo:

```python
idade = int(input("Digite sua idade: "))
```

Outra forma é receber o dado e depois converter: 
```python
idade = input("Digite sua idade: ")
idade_int = int(idade)
```

## concatenação

```python
print("Hello " + "world") 
```
``` python
print("Maria Joana, ", idade)
```
```python
print("{} tem {} anos".format(nome, idade))
```
## Estruturas condicionais

```python
if(condicao):
    #code
elif(condicao):
    #code
else:
    #code
```
## Estruturas de repetição
### while
```python
i = 0
while(i<10):
    print(i)
    i=i+1
```

### do while
```python

```
### for
```python
for variavel in range(inicio, final, quantidade-de-incremento):
    print(variavel)
```
## random()
1. import random
2. random.random() - gera um número decimal
3. numero_aletorio = (random.rondom() * 100)+1 - se múltiplicar por 100 o intervalo vai ser de 0 a 100 e a soma para não sair no 0 e sim no intervalo de 1 a 100
4. round(numero_aletorio) - para arendondar 

random.randrange(1, 101) - a partir desse método dar para escolher o intervalo

## Função

### Criação da função:

 ```python
 def nome_da_funcao():
    # code
 ```

### Chamar a função:
```python
nome_da_funcao()
```
## Manipulação de strings

<a src="https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods">Funções para manipular str</a>

## List

```python
frutas = ["banana", "maçã", "pera"]
```
### funções para maninupalação de listas

<a src="https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods">Funções para manipular list</a> //link errado

## Tuple

É tipo uma lista imutável, ou seja, não é possível inserir, deletar e nem alterar seus dados.

```python
dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
```

