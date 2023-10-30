# importa a biblioteca VPython e numpy

from vpython import *
from numpy import *



scene = canvas(title='main', width=1300, height=700, background=color.gray(0.7))
# define as constantes físicas
altura_inicial = -100  # de -99 a 99
velocidade_inicial = vector(0.0, 0.0, 0.0)  # m/s
aceleracao_gravidade = 9.81
intervalo_tempo = 0.2  # s
massa_especifica_fluido = 2
massa_objeto = 1.5


# define o objeto como uma esfera
objeto = sphere(pos=vector(0, 0, 0), radius=7)
objeto.velocity = velocidade_inicial
objeto.pos.y = altura_inicial
objeto.velocity = objeto.velocity

# define o recipiente como como uma caixa
recipiente = box(pos=vector(0, 0, 0), size=vector(50, 200, 50), color=(color.blue), opacity=0.2)
recipiente.pos.y = -(recipiente.size.y/2)
superficie = box(pos=vector(0, 0, 0), size=vector(100, 0.5, 100), color=color.blue)
fundo = -recipiente.size.y

# fórmula da força de empuxo:
aceleracao_empuxo_y = ((massa_especifica_fluido / massa_objeto) - 1) * aceleracao_gravidade
aceleracao_empuxo = vector(0.0, aceleracao_empuxo_y, 0.0)  # m/s^2

# parâmetros para calcular aceleração quando o objeto alcançar a superfície
h = 0 - (objeto.pos.y - objeto.radius)
incremento = 0.02
aceleracao_superficie_y = (((massa_especifica_fluido / massa_objeto) * log(h / (h + incremento)))-1) * aceleracao_gravidade
aceleracao_superficie = vector(0.0, aceleracao_superficie_y, 0.0)

# define o intervalo de tempo para a animação
rate(10)
counter = 0

tempo = list()
velocidade = list()
aceleracao = list()
t = -1

# simula o movimento do objeto
while (objeto.pos.y <= 0) and (objeto.pos.y > fundo + objeto.radius):  # estabelece uma condição de posição do objeto

    # atualiza a posição do objeto
    objeto.pos += objeto.velocity * intervalo_tempo + aceleracao_empuxo * (intervalo_tempo ** 2)
    # atualiza a velocidade do objeto
    objeto.velocity += aceleracao_empuxo * intervalo_tempo
    # aguarda um intervalo de tempo para animar o movimento
    rate(50)
    aceleracao_superficie = aceleracao_empuxo

    velocidade.append(objeto.velocity.y)
    aceleracao.append(aceleracao_empuxo_y)
    t=t+1
    tempo.append(t)

    while objeto.pos.y > (0 - objeto.radius):

        #atualização das variáveis com o objeto em contato com a superficie

        h = (0 - (objeto.pos.y - objeto.radius))
        logaritmo = log((h / (h + incremento)))
        incremento = 0.1

        aceleracao_superficie_y = ((massa_especifica_fluido / massa_objeto) * logaritmo - 1) * aceleracao_gravidade
        aceleracao_superficie = vector(0.0, aceleracao_superficie_y, 0.0)

        # verificação das variáveis nesse loop
# -----------------------------------------------------------------------------------------------------------------------------------------------------
        counter = counter + 1
        #if counter%2 == 0:
            #  print("_________________________________________________________________________________________________________________________________________")
            #  print('massa do fluido/massa do objeto = ',massa_especifica_fluido / massa_objeto )
            #  print('incremento = ', incremento)
            #  print('h = ',h)
            #  print('log(h / (h + incremento)) = ', logaritmo)
            #  print('(massa_especifica_fluido / massa_objeto) * log(h / (h + incremento))) - 1) = ' ,(massa_especifica_fluido / massa_objeto) * log(h / (h + incremento)) - 1)
            #  print('aceleracao = ', aceleracao_superficie)
            #  print('velocidade do objeto', objeto.velocity)

        if counter >= 40:
            break

# --------------------------------------------------------------------------------------------------------------------------------------------------------
        # atualiza a posição do objeto
        objeto.pos += objeto.velocity * intervalo_tempo + aceleracao_superficie * (intervalo_tempo ** 2)

        # atualiza a velocidade do objeto
        objeto.velocity += aceleracao_superficie * intervalo_tempo

        # aguarda um intervalo de tempo para animar o movimento
        rate(50)

        t = t + 1
        velocidade.append(objeto.velocity.y)
        aceleracao.append(aceleracao_superficie_y)
        tempo.append(t + 1)
print(tempo)
print(aceleracao)
print(velocidade)

import matplotlib.pyplot as plt



plt.plot(tempo,velocidade)
plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.title("Velocidade do Objeto no Tempo")


plt.plot(tempo,aceleracao)
plt.xlabel('Tempo')
plt.ylabel('Aceleração')
plt.title("Aceleração do Objeto no Tempo")
plt.show()
