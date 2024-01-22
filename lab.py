from loteria_caixa import MegaSena

loterias = ('MegaSena', 'LotoFacil', 'Quina', 'LotoMania', 'TimeMania', 'DuplaSena', 'Federal', 'Loteca', 'DiadeSorte', 'SuperSet') 

n = 3005

for loteria in loterias:
    try:
        a = vars()[f'{loteria}({n})']
        print(a)
    except:
        print('deu ruim')

