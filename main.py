import time
import os


# Skip screen
def skip(sec):
    # Pula a cena
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    time.sleep(sec)
    return os.system(command)


# Script

# TMB Homens
# 66 + (13,7p) + (5A) - (6,8I)

# TMB Mulheres
# 655 + (9,6p) + (1,8A) - (4,7I)

def tmb(weight, height, age, gender):
    if gender == "male":
        weight_r = weight * 13.7
        height_r = height * 5
        age_r = age * 6.8
        result = 66 + weight_r + height_r - age_r
    else:
        weight_r = weight * 9.6
        height_r = height * 1.8
        age_r = age * 4.7
        result = 655 + weight_r + height_r - age_r
    return result


def activity_rate(activity):
    if activity == "sedentário":
        return 0.5
    elif activity == "levemente ativo":
        return 0.7
    elif activity == "ativo":
        return 1
    else:
        print("Não foi possível calcular o nível de atividade do indivíduo")
        return 1


def bulking(tmb_result, activity):
    workout = 350
    activity_kcal = (tmb_result / 5) * activity_rate(activity)
    result = tmb_result + activity_kcal + 400
    result_workout = result + workout
    conclusion = f"Ingestão Kcal por dia sem treinar = {round(result)}\n" \
                 f"Ingestão Kcal por dia treinando = {round(result_workout)}\n\n\n" \
                 f"Observações: \n" \
                 f"Foi considerado um gasto calórico de {round(activity_kcal)} Kcal por atividade diária\n" \
                 f"Foi considerado um gasto calórico de {round(workout)} Kcal por treino de músculação"
    return conclusion


def cutting(tmb_result, activity):
    workout = 350
    activity_kcal = (tmb_result / 5) * activity_rate(activity)
    result = tmb_result + activity_kcal - 700
    result_workout = result + workout
    conclusion = f"Ingestão Kcal por dia sem treinar = {round(result)}\n" \
                 f"Ingestão Kcal por dia treinando = {round(result_workout)}\n\n\n" \
                 f"Observações: \n" \
                 f"Foi considerado um gasto calórico de {round(activity_kcal)} Kcal por atividade diária\n" \
                 f"Foi considerado um gasto calórico de {round(workout)} Kcal por treino de músculação"
    return conclusion


def person(name, weight, height, age, gender, activity, objective):
    basal = tmb(weight, height, age, gender)
    basal = '{:.2f}'.format(basal)
    if gender == "male":
        gender = "masculino"
    else:
        gender = "feminino"
    print(f"\nResultados para {name}")
    print("sexo: " + gender)
    print("Taxa Metabólica Basal = " + basal + " Kcal")
    print("Atividade física fora treino: " + activity)
    print(f"Objetivo: {objective}")
    print()
    if "ut" in objective:
        objective = cutting(float(basal), activity)
        print("Déficit calórico estipulado: 700kcal/dia ")
        print("Perda de 1kg de tecido lipidico em: 11 dias")
        print()
        print(objective)
    elif "ulk" in objective:
        objective = bulking(float(basal), activity)
        print("Superávit calórico estipulado: 400kcal/dia ")
        print()
        print(objective)
    else:
        print("Não foi possível determinar o seu objetivo")


def start():
    # nome
    name = input("Nome: ")

    # peso
    weight = input("Peso em KG: ")
    if "," in weight:
        weight = weight.replace(",", ".")

    # altura
    height = input("Altura em cm: ")
    while "," in height or "." in height:
        print("Você precisa digitar sua altura em cm (eg. 180 para um 1,80m)")
        height = input("Altura em cm: ")

    # idade
    age = input("Idade: ")

    # genero
    gender = "0"
    x = 0
    while x != 1:
        gender = input("Sexo: \n [ 1 ] Masculino \n [ 2 ] Feminino"
                       "\n\n\n Digite o número correspondente: ")
        if gender == "1":
            gender = "male"
            x = 1
        elif gender == "2":
            gender = "female"
            x = 1
        else:
            print("Você não digitou corretamente..")
            skip(1)

    # atividade
    activity = "0"
    x = 0
    while x != 1:
        activity = input("\nAtividade física fora treino: \n [ 1 ] sedentário \n [ 2 ] levemente ativo \n [ 3 ] ativo"
                         "\n\n Digite o número correspondente: ")
        if activity == "1":
            activity = "sedentário"
            x = 1
        elif activity == "2":
            activity = "levemente ativo"
            x = 1
        elif activity == "3":
            activity = "ativo"
            x = 1
        else:
            print("Você não digitou corretamente..")
            skip(1)

    # objetivo
    objective = "0"
    x = 0
    while x != 1:
        objective = input("\nObjetivo: \n [ 1 ] ganho de peso (Bulking) \n [ 2 ] perda de peso (Cutting)"
                          "\n\n Digite o número correspondente: ")
        if objective == "1":
            objective = "bulking"
            x = 1
        elif objective == "2":
            objective = "cutting"
            x = 1
        else:
            print("Você não digitou corretamente..")
            skip(1)

    skip(1)
    person(name, float(weight), int(height), int(age), gender, activity, objective)


while True:
    try:
        start()
        restart = input("\nPressione [Enter] para reiniciar..")
        skip(1)
    except ValueError:
        skip(1)
        print("\nAlgo deu errado ao preencher os dados!")
        print("Reiniciando...")
        time.sleep(3)
        skip(1)
        print()
        
