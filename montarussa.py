#and retorna True se ambas as condições forem True, e retorna Falsecaso contrário.
#or retorna True se pelo menos uma das condições for True, e Falsecaso contrário.
#not retorna True se a condição for False, e vice-versa.
#-------------------------------------------------------
  #if hunger > 4 and anger > 1:
    #print('Hangry')
#-------------------------------------------------------
  #if coffee > 0 or bubble_tea > 0:
    #print('😊')
#-------------------------------------------------------
  #if not tired:
    #print('Time to code!')
#-------------------------------------------------------

#Desde 1927, a montanha-russa "The Cyclone" encanta os visitantes de Coney Island (Brooklyn, NY). 🎢

#Eles estão instalando um novo sistema de entrada (a altura necessária é 137 cm e o custo é de 10 créditos) e precisam da sua ajuda para escrever o programa para ele!

#Pergunte ao usuário qual é sua altura e quantos créditos ele tem, e armazene os valores em uma heightvariável e uma creditsvariável.

#Use uma combinação de operadores relacionais e lógicos para criar as regras:

#Se eles forem altos o suficiente e tiverem créditos suficientes, imprima "Aproveite o passeio!"
#Caso contrário, se eles tiverem créditos suficientes, mas não forem altos o suficiente, imprima "Você não é alto o suficiente para andar".
#Caso contrário, se eles forem altos o suficiente, mas não tiverem créditos suficientes, imprima "Você não tem créditos suficientes".
#Caso contrário, imprima uma mensagem dizendo que eles não atenderam a nenhum dos requisitos.

#-------------------------------------------------------

altura = int(input('Qual a altura(cm)? '))
creditos = int(input('Quantos créditos você tem? '))

if altura >= 137 and creditos >= 10:
    print('Aproveite o passeio!')

elif altura < 137 and creditos < 10:
    print('Você não é alto o suficiente e não tem créditos suficientes.')

elif altura < 137:
    print('Você não é alto o suficiente para andar.')

elif creditos < 10:
    print('Você não tem créditos suficientes.')

else:
    print('Você não atendeu nenhum dos requisitos.')  # esse else agora é redundante, mas pode ficar
