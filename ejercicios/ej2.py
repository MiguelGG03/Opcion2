# Binomio de newton iterativo


def expand(func:str):
    for i in range(len(func)):
        if func[i]=='(':
            marc1=i
        elif func[i]==')':
            marc2=i
        elif func[i]=='^':
            marc3=func[i+1:]
    for i in range(marc1+1,marc2):
        try:
            termino_numerico=int(func[i])
        except:
            pass
        
    
    print(marc1)
    print(marc2)
    print(marc3)
    print(termino_numerico)

def main2():
    pr1 = input('Que funcion quieres expandir?\n'
                '>>>')
    expand(pr1)

if __name__ == '__main__':
    main2()