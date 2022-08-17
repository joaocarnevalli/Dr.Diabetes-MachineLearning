# Checkpoint 4 - Coding for security - Machine learning - scikit-learn - Dr. Diabetes
# Desafio: Como saber se tenho diabetes?
# Integrantes: João Pedro Zobolli Carnevalli     RM:94587 
#              Renato Kim                        RM:94146
#              Gustavo Kondo                     RM:95636
#              Kaiky Amaral                      RM:93284

# Importando as "Arvores" da biblioteca sklearn
from sklearn import tree 

# Importando a biblioteca sys
import sys

# Importando a biblioteca time
import time

from time import sleep

# Função de slowprint (Efeito de escrever)
def slowprint(a):
    for c in a+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

# Função de fastprint (Efeito de escrever)
def fastprint(a):
    for c in a+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./150)

# Função de fastprint, só que mais rapido (Efeito de escrever)
def fastprintmaisfast(a):
    for c in a+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)

# As informações contidas nas features, são, respectivamente: [Glicemia em Jejum, Glicemia Pós-Sobrecarga, Glicemia Casual]
features = [
#   Glicemia normal
    [75, 120, 150], [80, 125, 160], [85, 130, 170], [90, 135, 180], [95, 139, 190], [99, 136, 195], [82, 126, 185],
    [76, 121, 152], [81, 126, 162], [86, 131, 172], [91, 136, 182], [96, 138, 192], [99, 137, 196], [83, 127, 186],
    [77, 122, 154], [82, 127, 164], [87, 132, 176], [92, 137, 184], [97, 136, 198], [99, 138, 197], [84, 128, 187],
    [78, 123, 156], [83, 128, 166], [88, 133, 174], [93, 138, 186], [98, 134, 194], [99, 122, 198], [85, 139, 188],
    [79, 124, 158], [84, 129, 168], [89, 134, 178], [94, 139, 188], [99, 132, 196], [99, 124, 199], [86, 90, 189],

#   Tolerancia Glicose diminuída
    [100, 140, 170], [110, 150, 180], [120, 160, 190], [90, 170, 160], [101, 180, 170], [124, 190, 150], [105, 200, 185],
    [101, 141, 171], [111, 151, 181], [121, 161, 191], [91, 171, 161], [114, 181, 171], [114, 191, 151], [105, 200, 195],
    [102, 142, 172], [112, 152, 182], [122, 162, 192], [92, 172, 162], [121, 182, 172], [111, 192, 152], [105, 200, 175],
    [103, 143, 173], [113, 153, 183], [123, 163, 193], [93, 173, 163], [102, 183, 173], [103, 193, 153], [105, 200, 165],
    [104, 144, 174], [114, 154, 184], [124, 164, 194], [94, 174, 164], [106, 184, 174], [99, 194, 154], [105, 200, 155],
    [105, 145, 175], [115, 155, 185], [125, 165, 195], [95, 175, 165], [118, 185, 175], [120, 195, 155], [105, 200, 145],
    [106, 146, 176], [116, 156, 186], [126, 166, 196], [96, 176, 166], [123, 186, 176], [102, 196, 156], [105, 200, 142],
    [107, 147, 177], [117, 157, 187], [122, 167, 197], [97, 177, 167], [115, 187, 177], [110, 197, 157], [105, 200, 167],
    [108, 148, 178], [118, 158, 188], [123, 168, 198], [98, 178, 168], [109, 188, 178], [95, 198, 158], [105, 200, 198],
    [109, 149, 179], [119, 159, 189], [124, 169, 199], [99, 179, 169], [108, 189, 179], [121, 199, 159], [105, 200, 199],

#   Diabestes
    [126, 200, 200], [130, 210, 210], [150, 215, 220], [140, 220, 230], [160, 205, 240], [170, 210, 210], [180,220,245],
    [127, 201, 209], [131, 219, 211], [151, 216, 221], [141, 229, 231], [161, 206, 249], [179, 211, 211], [182,221,235],
    [128, 202, 208], [132, 218, 212], [152, 217, 222], [142, 228, 232], [162, 207, 248], [178, 212, 212], [184,222,225],
    [129, 203, 207], [133, 217, 213], [153, 218, 223], [143, 227, 233], [163, 208, 247], [177, 213, 213], [186,223,215],
    [128, 204, 206], [134, 216, 214], [154, 219, 224], [144, 226, 234], [164, 209, 246], [176, 214, 214], [188,224,205],
    [127, 205, 205], [135, 215, 215], [155, 214, 229], [145, 225, 235], [165, 201, 245], [175, 215, 225], [192,225,250],
    [126, 206, 204], [136, 214, 216], [156, 213, 225], [146, 224, 236], [166, 202, 243], [174, 216, 226], [194,226,240],
    [127, 207, 203], [137, 213, 217], [157, 212, 226], [147, 223, 237], [167, 203, 242], [173, 217, 227], [198,227,220],
    [129, 208, 202], [138, 212, 218], [158, 211, 227], [148, 222, 238], [168, 204, 241], [172, 218, 228], [196,228,220],
    [128, 209, 201], [139, 211, 219], [159, 210, 228], [149, 221, 239], [169, 205, 240], [171, 219, 229], [190,229,210],
]
# Sendo assim, levando a primeira lista como exemplo, 75 = Glicemia em Jejum, 120 = Glicemia Pós-Sobrecarga e 150 = Glicemia Casual.

labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,     # Glicemia Normal

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,       # glicose diminuída
        1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,       # Diabetes
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] 

# Classificando e ajustando as labels e as features
classif = tree.DecisionTreeClassifier() # Classificador
classif.fit(features, labels) # Ajusta as labels respectivamente com as features

diagnostico = False
positivo = ["sim", "s", "Sim", "yes", "Yes", "y"]
negativo = ["nao", "não", "n", "Não", "Nao", "no", "No"]
answer = 'x'
while True:
    try:
        fastprint("\nSelect Language:\n(ptbr) - Portuguese\n(eng) - English US")
        lang = str(input("-: "))
        if lang == "ptbr" or lang =="PTBR":
            fastprintmaisfast(f"\n{'-'*63}\n| Bem vindo ao nosso programa de pré-diagnóstico de Diabetes! |\n{'-'*63}\n")
            while True:
                respostas = 0
                value = 0
                fastprint("\nPara começarmos, informe seu nome")
                while True:
                    try:
                        nome = str(input("-: "))
                        if nome == "" or nome == " ":
                            fastprint("\nValor errado!")
                            fastprint("Digite seu nome\n")
                        else:
                            break
                    except SyntaxError or ValueError:
                        fastprint("Valor errado!")
                        fastprint("Digite seu nome")
                fastprint(f"\n\nOlá {nome}, Agora nos informe os níveis de glicemia coletados nas seguintes situações: ")
            

            # Obtendo o valor em jejum
                while True:
                    try:
                        fastprint("\nEm jejum")
                        g_jejum = float(input("-: "))
                        if g_jejum <55:
                            fastprint("\nTem certeza sobre esse valor?")
                            sleep(0.5)
                            fastprint("\nele esta muito abaixo do normal!")
                            sleep(0.5)
                            fastprint("\ninsira um valor maior que 55!\n")
                        else:
                            break
                    except ValueError:
                        print("\nDigite algum valor valido!")

            # Obtendo o valor pós-sobrecarga            
                while True:
                    try:
                        fastprint("\nPós-sobrecarga")            
                        g_possobrecarga = float(input("-: "))
                        if g_possobrecarga < 55:
                            fastprint("\nTem certeza sobre esse valor?")
                            sleep(0.5)
                            fastprint("ele esta muito abaixo do normal!")
                            sleep(0.5)
                            fastprint("insira um valor maior que 55!\n")  
                        else:
                            break
                    except ValueError:
                        print("\nDigite algum valor valido!")

            # Obtendo o valor em estado normal
                while True:
                    try:
                        fastprint("\nEm seu estado normal")
                        g_normal = float(input("-: "))
                        if g_normal < 55:
                            fastprint("\nTem certeza sobre esse valor?")
                            sleep(0.5)
                            fastprint("ele esta muito abaixo do normal!")
                            sleep(0.5)
                            fastprint("insira um valor maior que 55!\n")
                        else:
                            break
                    except ValueError:
                        print("\nDigite algum valor válido!")

            # Definindo o diagnóstico a partir dos inputs
                predict = classif.predict([[g_jejum, g_possobrecarga, g_normal]])

            # Tratamento dos resultados do programa
                if predict == 0:                                        # Glicemia normal
                    fastprint(f"\n{nome}, segundo nossa analise, você esta com a glicemia normal :D\n")
                    diagnostico == 0
                    if diagnostico == False:
                        fastprint("Gostaria de responder umas perguntas para ter certeza do diagnostico?")
                        diag = str(input("Resposta: "))
                        diag = diag.upper()
                        if diag == "SIM" or diag == "S":
                            slowprint("\nOk...\n")
                            diagnostico = True
                        else:
                            slowprint("\nOk...\n")
                elif predict == 1:                                      # Tolerancia diminuida
                    fastprint(f"\n{nome}, segundo nossa analise, você esta com a tolerância a glicose diminuída!\n")
                    diagnostico = True
                    fastprint("\nPara que possamos ter certeza, responda as próximas perguntas\n")
                else:                                                   # Diabetes
                    fastprint(f"\n{nome}, segundo nossa analise, você esta com diabetes mellitus :(\n")
                    diagnostico = True
                    fastprint("\nPara que possamos ter certeza, responda as próximas perguntas\n")

            # Tratamento para ver se há necessidade ou não de procurar um especialista para apurar as informações
                if diagnostico == True:
            # Primeira pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*49}\n| Voce tem sentido muita sede e/ou a boca seca? |\n{'-'*49}")
                            questions = str(input("Resposta: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")
            # Segunda pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*49}\n| Voce tem sentido mais fome que o normal?      |\n{'-'*49}")
                            questions = str(input("Resposta: "))  
                            questions.lower()              
                            if questions in positivo:
                                respostas = respostas + 1                    
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")
            # Terceira pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*49}\n| Voce tem se sentido mais cansado ultimamente? |\n{'-'*49}")
                            questions = str(input("Resposta: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1                    
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")
            # Quarta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*49}\n| Voce tem urinado com mais frequencia?         |\n{'-'*49}")
                            questions = str(input("Resposta: ")) 
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")
            # Quinta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*49}\n| Voce percebeu alguma mudança em sua visão?    |\n{'-'*49}")
                            questions = str(input("Resposta: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")

            # Sexta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*59}\n| Voce sentiu formigamento e/ou dormencia nas mãos e pés? |\n{'-'*59}")
                            questions = str(input("Resposta: ")) 
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Digite SIM ou NAO")
                        except ValueError or SyntaxError:
                            print("Digite SIM ou NAO")

                if respostas >= 3:
                    fastprint("\nRecomendamos que voce procure um médico especialista!\n")
                else:
                    print("\nObrigado por responder as perguntas!\n")
            # O usuario quer continuar utilizando o programa?
                while True:
                    try:
                        answer = input("Gostaria de fazer outra consulta? ")
                        answer.lower()
                        if answer in positivo:
                            fastprint("\nReiniciando o programa!")
                            break
                        if answer in negativo:
                            fastprint("\nObrigado por usar nossa solução")
                            break
                    except ValueError:
                        print("Digite Sim ou Nao")
                if answer in negativo:
                    break

        elif lang == "eng" or lang == "ENG":
            fastprintmaisfast(f"\n{'-'*50}\n| Welcome to our Diabetes pre-diagnosis program! |\n{'-'*50}\n")
            while True:
                diagnostico = False
                respostas = 0
                value = 0
                fastprint("\nTo get started, enter your name")
                while True:
                    try:
                        nome = str(input("-: "))
                        if nome == "" or " ":
                            fastprint("Wrong value!")
                            fastprint("Enter your name")
                        else:
                            break
                    except ValueError or SyntaxError:
                            fastprint("Wrong value!")
                            fastprint("Enter your name")
                fastprint(f"\n\nHello {nome}, Now tell us the blood glucose levels collected in the following situations:")

        # Obtendo o valor em jejum
                while True:
                    try:
                        fastprint("\nIn fasting")
                        g_jejum = float(input("-: "))
                        if g_jejum <55:
                            fastprint("\nAre you sure about this value?")
                            sleep(0.5)
                            fastprint("\nIt's way below normal!")
                            sleep(0.5)
                            fastprint("\nenter a value greater than 55!\n")
                        else:
                            break
                    except ValueError:
                        print("\nEnter any valid value!")

            # Obtendo o valor pós-sobrecarga            
                while True:
                    try:
                        fastprint("\nAfterload")            
                        g_possobrecarga = float(input("-: "))
                        if g_possobrecarga < 55:
                            fastprint("\nAre you sure about this value?")
                            sleep(0.5)
                            fastprint("It's way below normal!")
                            sleep(0.5)
                            fastprint("enter a value greater than 55!\n")  
                        else:
                            break
                    except ValueError:
                        print("\nEnter any valid value!")

            # Obtendo o valor em estado normal
                while True:
                    try:
                        fastprint("\nin its normal state")
                        g_normal = float(input("-: "))
                        if g_normal < 55:
                            fastprint("\nAre you sure about this value?")
                            sleep(0.5)
                            fastprint("It's way below normal!")
                            sleep(0.5)
                            fastprint("Enter a value greater than 55!\n")
                        else:
                            break
                    except ValueError:
                        print("\nEnter any valid value!")

            # Definindo o diagnóstico a partir dos inputs
                predict = classif.predict([[g_jejum, g_possobrecarga, g_normal]])

            # Tratamento dos resultados do programa
                if predict == 0:                                        # Glicemia normal
                    fastprint(f"\n{nome}, according to our analysis, you have normal blood glucose :D\n")
                    diagnostico == 0
                    if diagnostico == False:
                        fastprint("Would you like to answer some questions to be sure of the diagnosis?")
                        diag = str(input("Answer: "))
                        diag = diag.upper()
                        if diag == "YES" or diag == "Y":
                            print("Ok\n")
                            diagnostico = True
                        else:
                            print("Ok\n")
                elif predict == 1:                                      # Tolerancia diminuida
                    fastprint(f"\n{nome}, according to our analysis, you have impaired glucose tolerance!\n")
                    diagnostico = True
                    fastprint("\nSo that we can be sure, please answer the next questions\n")
                else:                                                   # Diabetes
                    fastprint(f"\n{nome}, according to our analysis, you have diabetes mellitus :(\n")
                    diagnostico = True
                    fastprint("\nSo that we can be sure, please answer the next questions\n")

            # Tratamento para ver se há necessidade ou não de procurar um especialista para apurar as informações
                if diagnostico == True:
            # Primeira pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*56}\n| Have you been feeling very thirsty and/or dry mouth? |\n{'-'*56}")
                            questions = str(input("Answer: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")
            # Segunda pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*51}\n| Have you been feeling hungrier than usual?      |\n{'-'*51}")
                            questions = str(input("Answer: "))  
                            questions.lower()              
                            if questions in positivo:
                                respostas = respostas + 1                    
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")
            # Terceira pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*44}\n| Have you been feeling more tired lately? |\n{'-'*44}")
                            questions = str(input("Answer: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1                    
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")
            # Quarta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*44}\n| Have you been urinating more often?      |\n{'-'*44}")
                            questions = str(input("Answer: ")) 
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")
            # Quinta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*46}\n| Did you notice any change in your vision?  |\n{'-'*46}")
                            questions = str(input("Answer: "))
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")

            # Sexta pergunta
                    while True:
                        try:
                            fastprintmaisfast(f"{'-'*65}\n| Did you feel tingling and/or numbness in your hands and feet? |\n{'-'*65}")
                            questions = str(input("Answer: ")) 
                            questions.lower()
                            if questions in positivo:
                                respostas = respostas + 1
                                break
                            elif questions in negativo:
                                break
                            else:
                                fastprint("Type YES or NO")
                        except ValueError or SyntaxError:
                            print("Type YES or NO")

                if respostas >= 3:
                    fastprint("\nWe recommend that you look for a specialist doctor!\n")
                    fastprint("Thanks for answering the questions!\n")
                else:
                    print("\nThanks for answering the questions!\n")
            # O usuario quer continuar utilizando o programa?
                while True:
                    try:
                        answer = input("Would you like to make another query? ")
                        answer == answer.lower()
                        if answer in positivo:
                            fastprint("\nRestarting the program!")
                            break
                        if answer in negativo:
                            fastprint("\nThanks for using our solution")
                            break
                    except ValueError:
                        print("Type Yes or No")
                if answer in negativo:
                    break
        else:
            fastprint("\nEnter the correct language!")
    except ValueError or SyntaxError:
        fastprint("\nEnter the correct language!")
    if answer in negativo:
        break
