# Projeto: VemPython/aula009
# Autor: rafael
# Data: 14/03/18 - 16:20
# Objetivo: TODO Manipulando texto

frase = 'Curso em Video Python'

# Fateamento simples - Apenas o index
print(frase[3])

# Fateamento limitado
print(frase[3:13])

# Fateamento com inicio infinito
print(frase[:13])

# Fateamento com final infinito
print(frase[13:])

# Fateamento limitado com saltos
print(frase[1:15:2])

# Contador de letras
print(frase.count('o'))

# Caixa alta
print(frase.upper())

# Caixa baixa
print(frase.lower())

# Tamanho da frase
print(len(frase))

# Remove espaços indesejados, antes e depois da frase
print(frase.strip())

# Substitui qlqr conjunto de caracteres na frase
print(frase.replace('Python', 'Android'))

# Verifica a Existência de alguma palavra dentro da String
print('Curso' in frase)

# Localiza a posição de alguma palavra dentro da String
print(frase.find('Curso'))

# Frase dividida (pelos espaços)
print(frase.split())

# 3 Aspas duplas
print("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")
