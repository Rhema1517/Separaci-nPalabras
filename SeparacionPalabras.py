def to_underscore(string):
    string=str(string)
    lista = []
    for n,l in enumerate(string):
        if l == l.upper()and not n == 0 and not l.isdigit():#isdigites si es un numero devuelve true
            lista.append('_')
        lista.append(l.lower())
    return ''.join(lista)
to_underscore(1)