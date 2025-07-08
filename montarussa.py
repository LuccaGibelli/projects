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
