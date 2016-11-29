import pandas as pd
from .combine import combineToFloat

headerPessoasVar = ['V0001','V0002','V0011','V0300','V0010','v0010','V1001','V1002','V1003','V1004','V1006','V0502','V0504','V0601','V6033','V6036','V6037','V6040','V0606','V0613','V0614','V0615','V0616','V0617','V0618','V0619','V0620','V0621','V0622','V6222','V6224','V0623','V0624','V0625','V6252','V6254','V6256','V0626','V6262','V6264','V6266','V0627','V0628','V0629','V0630','V0631','V0632','V0633','V0634','V0635','V6400','V6352','V6354','V6356','V0636','V6362','V6364','V6366','V0637','V0638','V0639','V0640','V0641','V0642','V0643','V0644','V0645','V6461','V6471','V0648','V0649','V0650','V0651','V6511','V6513','V6514','v6514','V0652','V6521','V6524','v6524','V6525','V6526','v6526','V6527','V6528','v6528','V6529','V6530','v6530','V6531','v6531','V6532','v6523','V0653','V0654','V0655','V0656','V0657','V0658','V0659','V6591','V0660','V6602','V6604','V6606','V0661','V0662','V0663','V6631','V6632','V6633','V0664','V6641','V6642','V6643','V0665','V6660','V6664','V0667','V0668','V6681','V6682','V0669','V6691','V6692','V6693','V6800','V0670','V0671','V6900','V6910','V6920','V6930','V6940','V6121','V0604','V0605','V5020','V5060','V5070','v5070','V5080','v5080','V6462','V6472','V5110','V5120','V5030','V5040','V5090','V5100','V5130','M0502','M0601','M6033','M0606','M0613','M0614','M0615','M0616','M0617','M0618','M0619','M0620','M0621','M0622','M6222','M6224','M0623','M0624','M0625','M6252','M6254','M6256','M0626','M6262','M6264','M6266','M0627','M0628','M0629','M0630','M0631','M0632','M0633','M0634','M0635','M6352','M6354','M6356','M0636','M6362','M6364','M6366','M0637','M0638','M0639','M0640','M0641','M0642','M0643','M0644','M0645','M6461','M6471','M0648','M0649','M0650','M0651','M6511','M0652','M6521','M0653','M0654','M0655','M0656','M0657','M0658','M0659','M6591','M0660','M6602','M6604','M6606','M0661','M0662','M0663','M6631','M6632','M6633','M0664','M6641','M6642','M6643','M0665','M6660','M0667','M0668','M6681','M6682','M0669','M6691','M6692','M6693','M0670','M0671','M6800','M6121','M0604','M0605','M6462','M6472','V1005']
headerPessoasNome = ['UNIDADE DA FEDERAÇÃO','CÓDIGO DO MUNICÍPIO','ÁREA DE PONDERAÇÃO','CONTROLE','PESO AMOSTRAL','REGIÃO GEOGRÁFICA','CÓDIGO DA MESORREGIÃO','CÓDIGO DA MICRORREGIÃO','CÓDIGO DA REGIÃO METROPOLITANA','SITUAÇÃO DO DOMICÍLIO','RELAÇÃO DE PARENTESCO OU DE CONVIVÊNCIA COM A PESSOA RESPONSÁVEL PELO DOMICÍLIO','ORDEM LÓGICA','SEXO','VARIÁVEL AUXILIAR DA IDADE CALCULADA (ANOS E MESES)','VARIÁVEL AUXILIAR DA IDADE CALCULADA EM ANOS','VARIÁVEL AUXILIAR DA IDADE CALCULADA EM MESES (PARA AS PESSOAS MENORES DE 1 ANO)','FORMA DE DECLARAÇÃO DA IDADE','COR OU RAÇA','REGISTRO DE NASCIMENTO','DIFICULDADE PERMANENTE DE ENXERGAR','DIFICULDADE PERMANENTE DE OUVIR','DIFICULDADE PERMANENTE DE CAMINHAR OU SUBIR DEGRAUS','DEFICIÊNCIA MENTAL/INTELECTUAL PERMANENTE','NASCEU NESTE MUNICÍPIO','NASCEU NESTA UNIDADE DA FEDERAÇÃO','NACIONALIDADE','ANO QUE FIXOU RESIDÊNCIA NO BRASIL','UF OU PAÍS ESTRANGEIRO DE NASCIMENTO','UNIDADE DA FEDERAÇÃO DE NASCIMENTO – código','QUAL É O PAÍS ESTRANGEIRO DE NASCIMENTO – código','TEMPO DE MORADIA NA UF','TEMPO DE MORADIA NO MUNICÍPIO','UNIDADE DA FEDERAÇÃO E MUNICÍPIO OU PAÍS ESTRANGEIRO DE MORADIA ANTES DE MUDAR-SE PARA ESTE MUNICÍPIO','UF DE RESIDÊNCIA ANTERIOR – código','MUNICÍPIO DE RESIDÊNCIA ANTERIOR – código','PAÍS DE RESIDÊNCIA ANTERIOR – código','RESIDÊNCIA EM 31 DE JULHO DE 2005','UF DE RESIDÊNCIA EM 31 DE JULHO DE 2005 – código','MUNICÍPIO DE RESIDÊNCIA EM 31 DE JULHO DE 2005 – código','PAÍS DE RESIDÊNCIA EM 31 DE JULHO DE 2005 – código','SABE LER E ESCREVER','FREQUENTA ESCOLA OU CRECHE','CURSO QUE FREQUENTA','SÉRIE / ANO QUE FREQUENTA','SÉRIE QUE FREQUENTA','CONCLUSÃO DE OUTRO CURSO SUPERIOR DE GRADUAÇÃO','CURSO MAIS ELEVADO QUE FREQUENTOU','CONCLUSÃO DESTE CURSO','ESPÉCIE DO CURSO MAIS ELEVADO CONCLUÍDO','NÍVEL DE INSTRUÇÃO','CURSO SUPERIOR DE GRADUAÇÃO – código','CURSO DE MESTRADO – código','CURSO DE DOUTORADO – código','MUNICÍPIO E UNIDADE DA FEDERAÇÃO OU PAÍS ESTRANGEIRO QUE FREQUENTAVA ESCOLA (OU CRECHE)','UF QUE FREQUENTAVA ESCOLA (OU CRECHE) – código','MUNICÍPIO QUE FREQUENTAVA ESCOLA (OU CRECHE) – código','PAÍS ESTRANGEIRO QUE FREQUENTAVA ESCOLA (OU CRECHE) – código','VIVE EM COMPANHIA DE CÔNJUGE OU COMPANHEIRO(A)','NÚMERO DE ORDEM DO CÔNJUGE OU COMPANHEIRO(A)','NATUREZA DA UNIÃO','ESTADO CIVIL','NA SEMANA DE 25 A 31/07/10, DURANTE PELO MENOS 1 HORA, TRABALHOU GANHANDO EM DINHEIRO, PRODUTOS, MERCADORIAS OU BENEFÍCIOS','NA SEMANA DE 25 A 31/07/10, TINHA TRABALHO REMUNERADO DO QUAL ESTAVA TEMPORARIAMENTE AFASTADO(A)','NA SEMANA DE 25 A 31/07/10, DURANTE PELO MENOS 1 HORA, AJUDOU SEM QUALQUER PAGAMENTO NO TRABALHO REMUNERADO DE MORADOR DO DOMICÍLIO','NA SEMANA DE 25 A 31/07/10, DURANTE PELO MENOS 1 HORA, TRABALHOU NA PLANTAÇÃO, CRIAÇÃO DE ANIMAIS OU PESCA, SOMENTE PARA ALIMENTAÇÃO DOS MORADORES DO DOMICÍLIO (INCLUSIVE CAÇA E EXTRAÇÃO VEGETAL)','QUANTOS TRABALHOS TINHA','OCUPAÇÃO – código','ATIVIDADE – código','NESSE TRABALHO ERA','QUANTAS PESSOAS EMPREGAVA NESSE TRABALHO','ERA CONTRIBUINTE DE INSTITUTO DE PREVIDÊNCIA OFICIAL EM ALGUM TRABALHO QUE TINHA NA SEMANA DE 25 A 31 DE JULHO DE 2010','NO TRABALHO PRINCIPAL, QUAL ERA O RENDIMENTO BRUTO (OU A RETIRADA) MENSAL QUE GANHAVA HABITUALMENTE EM JULHO DE 2010','VALOR DO RENDIMENTO BRUTO (OU A RETIRADA) MENSAL NO TRABALHO PRINCIPAL (pode ter valor branco)','RENDIMENTO NO TRABALHO PRINCIPAL (pode ter valor branco)','RENDIMENTO NO TRABALHO PRINCIPAL EM Nº DE SALÁRIOS MÍNIMOS  (pode ter valor branco)','NOS DEMAIS TRABALHOS, QUAL ERA O RENDIMENTO BRUTO (OU A RETIRADA) MENSAL QUE GANHAVA HABITUALMENTE EM JULHO DE 2010','VALOR DO RENDIMENTO BRUTO (OU A RETIRADA) MENSAL NOS DEMAIS TRABALHOS (EM REAIS)','RENDIMENTO BRUTO NOS DEMAIS TRABALHOS EM Nº DE SALÁRIOS MÍNIMOS','RENDIMENTO EM TODOS OS TRABALHOS','RENDIMENTO EM TODOS OS TRABALHOS EM Nº DE SALÁRIOS MÍNIMOS','RENDIMENTO MENSAL TOTAL EM JULHO DE 2010','RENDIMENTO MENSAL TOTAL EM Nº DE SALÁRIOS MÍNIMOS EM JULHO DE 2010','RENDIMENTO DOMICILIAR (DOMICÍLIO PARTICULAR) EM JULHO DE 2010','RENDIMENTO DOMICILIAR (DOMICÍLIO PARTICULAR) EM Nº DE SALÁRIOS MÍNIMOS EM JULHO DE 2010','RENDIMENTO DOMICILIAR (DOMICÍLIO PARTICULAR) PER CAPITA EM JULHO DE 2010','RENDIMENTO DOMICILIAR (DOMICÍLIO PARTICULAR) PER CAPITA EM Nº DE SALÁRIOS MÍNIMOS EM JULHO DE 2010','NO TRABALHO PRINCIPAL, QUANTAS HORAS TRABALHAVA HABITUALMENTE POR SEMANA','NO PERÍODO DE 02 A 31 DE JULHO DE 2010, TOMOU ALGUMA PROVIDÊNCIA, DE FATO, PARA CONSEGUIR  TRABALHO?','SE TIVESSE CONSEGUIDO TRABALHO, ESTARIA DISPONÍVEL PARA ASSUMI-LO NA SEMANA DE 25 A 31 DE JULHO DE 2010?','EM JULHO DE 2010, TINHA RENDIMENTO MENSAL HABITUAL DE APOSENTADORIA OU PENSÃO DE INSTITUTO DE PREVIDÊNCIA OFICIAL (FEDERAL, ESTADUAL OU MUNICIPAL)?','EM JULHO DE 2010, TINHA RENDIMENTO MENSAL HABITUAL DE PROGRAMA SOCIAL BOLSA-FAMÍLIA OU PROGRAMA DE ERRADICAÇÃO DO TRABALHO INFANTIL (PETI)','EM JULHO 2010, TINHA RENDIMENTO MENSAL HABITUAL DE OUTROS PROGRAMAS SOCIAIS OU DE TRANSFERÊNCIAS','EM JULHO DE 2010, TINHA RENDIMENTO MENSAL HABITUAL DE OUTRAS FONTES (JUROS DE POUPANÇA, APLICAÇÕES FINANCEIRAS, ALUGUEL, PENSÃO, APOSENTADORIA DE PREVIDÊNCIA PRIVADA, ETC)?','EM JULHO DE 2010 QUAL FOI O VALOR TOTAL DESTE(S) RENDIMENTO(S)','EM QUE MUNICÍPIO E UNIDADE DA FEDERAÇÃO OU PAÍS ESTRANGEIRO TRABALHA','EM QUE UNIDADE DA FEDERAÇÃO TRABALHAVA - código','EM QUE MUNICÍPIO TRABALHAVA - código','EM QUE PAÍS ESTRANGEIRO TRABALHAVA - código','RETORNA DO TRABALHO PARA CASA DIARIAMENTE','QUAL É O TEMPO HABITUAL GASTO DE DESLOCAMENTO DE SUA CASA ATÉ O TRABALHO','QUANTOS FILHOS E FILHAS NASCIDOS VIVOS TEVE ATÉ 31 DE JULHO DE 2010','QUANTOS FILHOS NASCIDOS VIVOS TEVE ATÉ 31 DE JULHO DE 2010','QUANTAS FILHAS NASCIDAS VIVAS TEVE ATÉ 31 DE JULHO DE 2010','TOTAL DE FILHOS NASCIDOS VIVOS QUE TEVE ATÉ 31 DE JULHO DE 2010','DOS FILHOS E FILHAS QUE TEVE, QUANTOS ESTAVAM VIVOS EM 31 DE JULHO DE 2010','DOS FILHOS QUE TEVE, QUANTOS ESTAVAM VIVOS EM 31 DE JULHO DE 2010','DAS FILHAS QUE TEVE, QUANTAS ESTAVAM VIVAS EM 31 DE JULHO DE 2010','TOTAL DE FILHOS QUE TEVE, QUANTOS ESTAVAM VIVOS EM 31 DE JULHO DE 2010','QUAL É O SEXO DO ÚLTIMO FILHO TIDO NASCIDO VIVO ATÉ 31 DE JULHO DE 2010','IDADE DO ÚLTIMO FILHO TIDO NASCIDO VIVO ATÉ 31 DE JULHO DE 2010','EXISTÊNCIA DE FILHO TIDO NASCIDO VIVO NO PERÍODO DE REFERÊNCIA DE 12 MESES ANTERIORES A 31/07/2010','ESTE(A) FILHO(A) ESTAVA VIVO(A) EM 31 DE JULHO DE 2010','QUAL FOI O MÊS E O ANO QUE ESTE(A) FILHO(A) FALECEU','QUAL FOI O MÊS QUE ESTE(A) FILHO(A) FALECEU','QUAL FOI O ANO QUE ESTE(A) FILHO(A) FALECEU','QUANTOS FILHOS E FILHAS NASCIDOS MORTOS TEVE ATÉ 31 DE JULHO DE 2010','QUANTOS FILHOS NASCIDOS MORTOS TEVE ATÉ 31 DE JULHO DE 2010','QUANTOS FILHAS NASCIDAS MORTAS TEVE ATÉ 31 DE JULHO DE 2010','QUANTOS FILHOS E FILHAS NASCIDOS MORTOS TEVE ATÉ 31 DE JULHO DE 2010','TOTAL DE FILHOS TIDOS NASCIDOS VIVOS E NASCIDOS MORTOS','ASSINALE QUEM PRESTOU AS INFORMAÇÕES DESTA PESSOA','CONDIÇÃO DE ATIVIDADE NA SEMANA DE REFERÊNCIA','CONDIÇÃO DE OCUPAÇÃO NA SEMANA DE REFERÊNCIA','SITUAÇÃO DE OCUPAÇÃO NA SEMANA DE REFERÊNCIA','POSIÇÃO NA OCUPAÇÃO E CATEGORIA DO EMPREGO NO TRABALHO PRINCIPAL','SUBGRUPO E CATEGORIA DO EMPREGO NO TRABALHO PRINCIPAL','Qual é a sua religião ou culto? -  código   (banco de códigos; 999 = ignorado)','TEM MÃE VIVA?','Número de ordem da mãe da pessoa   (branco; 1 a 98; 99 = ignorado)','NÚMERO DA FAMÍLIA','Número de Pessoas na Família','Rendimento familiar per capita em julho de 2010 (0 a 999999','99)','Rendimento familiar per capita em nº de salários mínimos em julho de 2010 (0 a 9999,99999)','Qual era a ocupação que exercia no trabalho que tinha? - código 2000  (branco; banco de códigos de 2000)','Qual era a atividade principal do empreendimento em que tinha esse trabalho? - código 2000  (branco; banco de códigos de 2000)','CONDIÇÃO DE CONTRIBUIÇÃO PARA INSTITUTO DE PREVIDÊNCIA OFICIAL NO TRABALHO PRINCIPAL','CONDIÇÃO DE CONTRIBUIÇÃO PARA INSTITUTO DE PREVIDÊNCIA OFICIAL EM QUALQUER TRABALHO','TIPO DE UNIDADE DOMÉSTICA','INDICADORA DE FAMÍLIA','TIPO DE COMPOSIÇÃO FAMILIAR DAS FAMÍLIAS ÚNICAS E CONVIVENTES PRINCIPAIS','TIPO DE COMPOSIÇÃO FAMILIAR DAS FAMÍLIAS CONVIVENTES SECUNDÁRIAS','ORDEM LÓGICA NA FAMÍLIA','MI V0502','MI V0601','MI V6033','MI V0606','MI V0613','MI V0614','MI V0615','MI V0616','MI V0617','MI V0618','MI V0619','MI V0620','MI V0621','MI V0622','MI V6222','MI V6224','MI V0623','MI V0624','MI V0625','MI V6252','MI V6254','MI V6256','MI V0626','MI V6262','MI V6264','MI V6266','MI V0627','MI V0628','MI V0629','MI V0630','MI V0631','MI V0632','MI V0633','MI V0634','MI V0635','MI V6352','MI V6354','MI V6356','MI V0636','MI V6362','MI V6364','MI V6366','MI V0637','MI V0638','MI V0639','MI V0640','MI V0641','MI V0642','MI V0643','MI V0644','MI V0645','MI V6461','MI V6471','MI V0648','MI V0649','MI V0650','MI V0651','MI V6511','MI V0652','MI V6521','MI V0653','MI V0654','MI V0655','MI V0656','MI V0657','MI V0658','MI V0659','MI V6591','MI V0660','MI V6602','MI V6604','MI V6606','MI V0661','MI V0662','MI V0663','MI V6631','MI V6632','MI V6633','MI V0664','MI V6641','MI V6642','MI V6643','MI V0665  ','MI V6660','MI V0667','MI V0668','MI V6681','MI V6682','MI V0669','MI V6691','MI V6692','MI V6693','MI V0670','MI V0671','MI V6800','MI V6121','MI V0604','MI V0605','MI V6462','MI V6472','SITUAÇÃO DO SETOR']

headerDomiciliosVar = ['V0001','V0002','V0011','V0300','V0010','v0010','V1001','V1002','V1003','V1004','V1006','V4001','V4002','V0201','V2011','V2012','v2012','V0202','V0203','V6203','v6203','V0204','V6204','v6204','V0205','V0206','V0207','V0208','V0209','V0210','V0211','V0212','V0213','V0214','V0215','V0216','V0217','V0218','V0219','V0220','V0221','V0222','V0301','V0401','V0402','V0701','V6529','V6530','v6530','V6531','v6531','V6532','v6532','V6600','V6210','M0201','M2011','M0202','M0203','M0204','M0205','M0206','M0207','M0208','M0209','M0210','M0211','M0212','M0213','M0214','M0215','M0216','M0217','M0218','M0219','M0220','M0221','M0222','M0301','M0401','M0402','M0701','V1005']
headerDomiciliosNome = ['UNIDADE DA FEDERAÇÃO','CÓDIGO DO MUNICÍPIO','ÁREA DE PONDERAÇÃO','CONTROLE','PESO AMOSTRAL','REGIÃO GEOGRÁFICA','CÓDIGO DA MESORREGIÃO','CÓDIGO DA MICRORREGIÃO','CÓDIGO DA REGIÃO METROPOLITANA','SITUAÇÃO DO DOMICÍLIO','ESPÉCIE DE UNIDADE VISITADA','TIPO DE ESPÉCIE','DOMICÍLIO, CONDIÇÃO DE OCUPAÇÃO','VALOR DO ALUGUEL (EM REAIS)','ALUGUEL EM Nº DE SALÁRIOS MÍNIMOS','MATERIAL PREDOMINANTE, PAREDES EXTERNAS','CÔMODOS, NÚMERO','DENSIDADE DE MORADOR/CÔMODO','CÔMODOS COMO DORMITÓRIO, NÚMERO','DENSIDADE DE MORADOR / DORMITÓRIO','BANHEIROS DE USO EXCLUSIVO, NÚMERO','SANITÁRIO OU BURACO PARA DEJEÇÕES, EXISTÊNCIA','ESGOTAMENTO SANITÁRIO, TIPO','ABASTECIMENTO DE ÁGUA, FORMA','ABASTECIMENTO DE ÁGUA, CANALIZAÇÃO','LIXO, DESTINO','ENERGIA ELÉTRICA, EXISTÊNCIA','EXISTÊNCIA DE MEDIDOR OU RELÓGIO, ENERGIA ELÉTRICA, COMPANHIA DISTRIBUIDORA','RÁDIO, EXISTÊNCIA','TELEVISÃO, EXISTÊNCIA','MÁQUINA DE LAVAR ROUPA, EXISTÊNCIA','GELADEIRA, EXISTÊNCIA','TELEFONE CELULAR, EXISTÊNCIA','TELEFONE FIXO, EXISTÊNCIA','MICROCOMPUTADOR, EXISTÊNCIA','MICROCOMPUTADOR COM ACESSO À INTERNET, EXISTÊNCIA','MOTOCICLETA PARA USO PARTICULAR, EXISTÊNCIA','AUTOMÓVEL PARA USO PARTICULAR, EXISTÊNCIA','ALGUMA PESSOA QUE MORAVA COM VOCÊ(S) ESTAVA MORANDO EM OUTRO PAÍS EM 31 DE JULHO DE 2010','QUANTAS PESSOAS MORAVAM NESTE DOMICÍLIO EM 31 DE JULHO DE 2010','A RESPONSABILIDADE PELO DOMICÍLIO É DE','DE AGOSTO DE 2009 A JULHO DE 2010, FALECEU ALGUMA PESSOA QUE MORAVA COM VOCÊ(S) (INCLUSIVE CRIANÇAS RECÉM-NASCIDAS E IDOSOS)','RENDIMENTO MENSAL DOMICILIAR EM JULHO DE 2010','RENDIMENTO DOMICILIAR, SALÁRIOS MÍNIMOS, EM JULHO DE 2010','RENDIMENTO DOMICILIAR PER CAPITA EM JULHO DE 2010','RENDIMENTO DOMICILIAR PER CAPITA, EM Nº DE SALÁRIOS MÍNIMOS, EM JULHO DE 2010','Espécie da Unidade Doméstica','ADEQUAÇÃO DA MORADIA','MI V0201','MI V2011','MI V0202','MI V0203','MI V0204','MI V0205','MI V0206','MI V0207','MI V0208','MI V0209','MI V0210','MI V0211','MI V0212','MI V0213','MI V0214','MI V0215','MI V0216','MI V0217','MI V0218','MI V0219','MI V0220','MI V0221','MI V0222','MI V0301','MI V0401','MI V0402','MI V0701','Situação do setor']

def readCenso(recorte='pessoas', estado='todos', local='~/IBGE', ano='2010', RM='', header='var', dropna=False, fillna=999999, verbose=False):
    arquivo = 'Amostra_'

    if RM == 'incluir':
        print('TODO')
        return 0
    elif RM == 'apenas':
        RM = '_RM'+estado
    elif RM == 'excluir':
        RM = '_outras'

    if estado == 'todos':
        print('TODO')
        return 0
    elif estado == 'SP':
        codEstado = '35'
    elif estado == 'MG':
        codEstado = '31'
    else:
        print('TODO')

    if recorte == 'domicilios':

        widths = [2,5,13,8,3,13,1,2,3,2,1,2,2,1,6,4,5,1,2,2,1,2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,7,5,5,6,2,4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        arquivo = arquivo+recorte.title()+'_'+codEstado+RM+'.txt'
        leitura = local+'/'+ano+'/'+arquivo
        if verbose == True:
            print('Realizando leitura do arquivo em '+leitura+'.')
        df = pd.read_fwf(leitura,
                   widths = widths, names = headerDomiciliosVar, converters = {'V0010':int,'V2012':int, 'V6203':int, 'V6204':int, 'V6530':int, 'V6531':int, 'V6532':int
                                                             ,'v0010':int,'v2012':int, 'v6203':int, 'v6204':int, 'v6530':int, 'v6531':int, 'v6532':int})
        if verbose == True:
            print('Leitura realizada com sucesso.')

        if dropna == True and fillna != False:
            print("Escolha apenas um tipo de tratamento de valores nao existentes.")
            return 0
        elif dropna == True:
            if verbose == True:
                print('Eliminando entradas vazias.')
            df.dropna(inplace=True)
        elif fillna != False:
            if verbose == True:
                print('Substituindo entradas vazias por '+str(fillna))
            df.fillna(fillna, inplace=True)

        merge = ['V0010','V2012', 'V6203', 'V6204', 'V6530', 'V6531', 'V6532']
        if verbose == True:
            print('Convertendo numeros inteiros em decimais.')
        for i in merge:
            for j in range(0,df[i].count()-1):
                if pd.isnull(df[i].at[j]) or pd.isnull(df[i.lower()].at[j]):
                    combined = df[i].at[j]
                else:
                    combined = combineToFloat(df[i].at[j], df[i.lower()].at[j]) #Combina dois inteiros para formar um float
                df.set_value(j, i+'N', combined) #Cria nova coluna com os valores combinados
            df.drop(i, axis=1, inplace=True) #Elimina cantigas colunas desnecessarias
            df.drop(i.lower(), axis=1, inplace=True)
            df.rename(columns={i+'N': i}, inplace=True) #Renomeia a nova coluna para o nome original
        if verbose == True:
            print('Conversao realizada com sucesso.')

        if header == 'nome':
            changeHeader(df)

        if verbose == True:
            print('Operacoes finalizadas, retornando dataframe.')

        return df

    elif recorte == 'pessoas':

        widths = [2,5,13,8,3,13,1,2,3,2,1,2,2,1,3,3,2,1,1,1,1,1,1,1,1,1,1,4,1,7,7,3,3,1,7,7,7,1,7,7,7,1,1,2,2,1,1,2,1,1,1,3,3,3,1,7,7,7,1,2,1,1,1,1,1,1,1,4,5,1,1,1,1,6,6,4,2,1,6,4,5,7,4,5,7,4,5,7,5,5,6,2,4,5,3,1,1,1,1,1,1,6,1,7,7,7,1,1,1,2,2,2,1,2,2,2,1,3,1,1,1,2,4,1,2,2,2,2,1,2,1,1,1,1,1,3,1,2,2,2,6,2,4,5,4,5,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        arquivo = arquivo+recorte.title()+'_'+codEstado+RM+'.txt'
        leitura = local+'/'+ano+'/'+arquivo
        if verbose == True:
            print('Realizando leitura do arquivo em '+leitura+'.')
        df = pd.read_fwf(leitura,
                   widths = widths, names = header, converters = {'V0010':int,'V6514':int, 'V6524':int, 'V6526':int, 'V6528':int, 'V6530':int, 'V6531':int, 'V6532':int, 'V5070':int, 'V5080':int
                                                             ,'v0010':int,'v6514':int, 'v6524':int, 'v6526':int, 'v6528':int, 'v6530':int, 'v6531':int, 'v6532':int, 'v5070':int, 'v5080':int})
        if verbose == True:
            print('Leitura realizada com sucesso.')

        if dropna == True and fillna != False:
            print("Escolha apenas um tipo de tratamento de valores nao existentes.")
            return 0
        elif dropna == True:
            if verbose == True:
                print('Eliminando entradas vazias.')
            df.dropna(inplace=True)
        elif fillna != False:
            if verbose == True:
                print('Substituindo entradas vazias por '+str(fillna))
            df.fillna(fillna, inplace=True)

        merge = ['V0010','V6514', 'V6524', 'V6526', 'V6528', 'V6530', 'V6531', 'V6532', 'V5070', 'V5080']
        if verbose == True:
            print('Convertendo numeros inteiros em decimais.')
        for i in merge:
            for j in range(0,df[i].count()-1):
                combined = combineToFloat(df[i].at[j], df[i.lower()].at[j]) #Combina dois inteiros para formar um float
                df.set_value(j, i+'N', combined) #Cria nova coluna com os valores combinados
            df.drop(i, axis=1, inplace=True) #Elimina cantigas colunas desnecessarias
            df.drop(i.lower(), axis=1, inplace=True)
            df.rename(columns={i+'N': i}, inplace=True) #Renomeia a nova coluna para o nome original
        if verbose == True:
            print('Conversao realizada com sucesso.')

        if header == 'nome':
            changeHeader(df)

        if verbose == True:
            print('Operacoes finalizadas, retornando dataframe.')

        return df

def headerPessoas():
    return headerPessoas

def headerDomicilios():
    return headerDomicilios

def getDicPessoas():
    dic = dict(zip(headerPessoasVar, headerPessoasNome))
    return dic

def getDictDomicilios():
    dic = dict(zip(headerDomiciliosVar, headerDomiciliosNome))
    return dic

def changeHeader(df):
    if df.columns[len(df.columns)-1] == 'M6427':
        df.columns = headerPessoasNome
    elif df.columns[len(df.columns)-1] == 'M0701':
        df.columns = headerDomiciliosNome
