import csv

#nome do arquivo a ser lido
arq = 'Teste Python.txt' 

#variável tipo lista para armazenar o conteudo do arquivo lido
lista = [] 

#variavel para armazenar um dicionário que será o arquivo csv final
dic = {}

#lê o arquivo da variável arq
with open(arq,'r', encoding="utf8") as f: 
    for x in f:
        #retira quebra de linha
        a = x.replace('\n','') 
        
        #insere na variável lista
        lista.append(a) 

#retira linhas em branco
lista = [i for i in lista if len(i) > 0] 

#busca qual elemento da lista é o inicio do quadro 1
linhaIniEmit = lista.index('Quadro 1 - EMITENTE:') 

#busca qual elemento da lista é o inicio do quadro 2
linhaIniEspec = lista.index('Quadro 2 - Especificações do Crédito:') 

#busca o elemento que termina o quadro 2
fimEspec = lista.index('Quadro 3 - Dados do CORRESPONDENTE BANCÁRIO:') 

#faz iteração apenas entre o inicio e fim do quadro 1, a partir das variaveis linhaEmit e linhaEspec
for e in lista[linhaIniEmit:linhaIniEspec]: 
    #separa o valor do elemento da lista pelo :
    z = e.split(':') 
    
    # pode ter valor do elemento sem conteúdo, ex: campo e-mail sem ter sido informado
    if len(z) > 1:
        dic[z[0]] = z[1].strip()

#retira o primeiro elemento do dic pois é só o nome do quadro
del dic['Quadro 1 - EMITENTE'] 

# o quadro 2,Especificações, possui inicio de linha numerado e formatado com ponto, então, uso a variável conta pra incrementar 1 até 15 
conta = 1 

#faz loop pra iterar sobre a lista mais especificamente apenas para pegar o quadro 2
for i in range (linhaIniEspec + 1, fimEspec):
    
    #string para montar a frase completa do dicionario CHAVE:VALOR
    aux = ''   
    
    #só vai montar a string, a linha que possui : (dois pontos) ou o começa da linha é numerado de acordo com o contador
    if lista[i].find(':') != -1 or lista[i][:3].strip() == str(conta) + '.': 
        
        #o primeiro conteúdo da string é basicamente a chave do dic
        aux = str(lista[i])
        
        #se não achou : (dois pontos), então eu coloco ao final, pois mais a frente uso split por 2 pontos
        if aux.find(':') == -1:
            aux = aux + ':'
            
        #Se o IF acima é a chave do dic, este if abaixo é o value da chave do dic
        #então, verifica se o conteúdo do próximo elemento da lista pode conteúdo do elemento da lista atual
        #pois pode estar quebrando a linha
        if lista[i+1].find(':') == -1 and lista[i+1][:3] != str(conta) + '.' and aux.find(str(conta)) == -1:
            aux = str(aux) + ' ' + str(lista[i+1])

#         if lista[i+2].find(':') == -1 and lista[i+2][:3] == str(conta) + '.':
#             aux = aux + ' ' + str(lista[i+2])

        
        #só soma 1 no contador caso tenha passado pela linha que é chave do dic
        conta+=1
        
        #faz um split por dois pontos
        spl = aux.split(':')
        
        #o que está antes do dois pontos é a chave do dic e coluna do CSV
        key = spl[0].strip()
        
        #o que está depois do dois pontos, é valor do dic e valor da coluna do CSV
        value = spl[1].strip()
        
        #cria de fato o dic que será transformado em CSV
        dic[key] = value
        

#Cria o CSV
with open('Emitente.csv', 'w') as f:
    w = csv.DictWriter(f, dic.keys())
    w.writeheader()
    w.writerow(dic)