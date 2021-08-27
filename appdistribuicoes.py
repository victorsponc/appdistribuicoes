import streamlit as st
import matplotlib.pyplot as plt
import scipy.stats as ss
import random
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title = 'APP - Distribuições', 
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')

paginas = ['Home', 'União de Normais', 'Teorema do limite central', 'Eleição', 'Sobre']

pagina = st.sidebar.radio('Navegue por aqui', paginas)


#===============================================================================================================


if pagina == 'Home':
	'''
	# Estatística, o que raios é isso?
	'''
	#st.image('Imagem1.png', use_column_width = 'always')

	'''
	### Olá.
	### Estatística costuma ser um assunto que assusta muitos estudantes. Vemos demonstrações, fórmulas, e continuamos a inseguros sobre os principais conceitos. Isso acontece por que nós seres humanos, ao contrário do que gostamos de acreditar, não somos naturalmente dotados daquilo que podemos chamar de intuição estatística. Em outras palavras, não somos bons de chute. 
	### A estatística desafia o senso comum.
	### Se desejamos fazer uma pesquisa eleitoral, qual a quantidade mínima de pessoas que devemos entrevistar? Qual a confiabilidade do resultado obtido. Aliás, o que é confiança estatística? O que são distribuições de probabilidade e o que elas querem nos dizer?
	### O propósito deste webapp é fornecer uma ferramenta simples para que o usuário possa desenvolver a compreensão intuitiva de alguns conceitos estatísticos e responder a perguntas como essas.
	'''
	st.markdown('---')


#===============================================================================================================


if pagina == 'União de Normais':

	'''
	# Distribuições
	'''
	'Soma e multiplicação de distribuições normais'

	st.markdown('---')

	#curvas normais
	st.markdown('# Distribuições Normais')
	normal1 = ss.norm.rvs(loc = 400, scale = 50, size = 10000 )
	normal2 = ss.norm.rvs(loc = 1000, scale = 50, size = 10000 )
	plt.hist(normal1, edgecolor = 'white', bins = 50, color = "blue", alpha = 0.7)
	plt.hist(normal2, edgecolor = 'white', bins = 50, color = "blue", alpha = 0.7)

	#escolha de ação
	ação = st.selectbox('O que deseja fazer?',['Nada', 'Soma','Média'])
	if ação == 'Soma':
		curvares = normal1 + normal2
		mediares = curvares.mean()
		desviores = curvares.std()
	if ação == 'Média':
		curvares = (normal1 + normal2)/2
		mediares = curvares.mean()
		desviores = curvares.std()
	if ação == 'Nada':
		curvares = ""

	#plotagem
	plt.hist(curvares, edgecolor = 'white', bins = 50, color = "red")
	st.pyplot()

	#escritas
	if ação == 'Soma':
		col1, col2, col3 = st.columns(3)
		col3.markdown(f'Curva resultante em vermelho: Média = {mediares:.5}, S = {desviores:.4}')
	if ação == 'Média':
		col1, col3, col2 = st.columns(3)
		col3.markdown(f'Curva resultante em vermelho: Média = {mediares:.5}, S = {desviores:.4}')
	if ação == 'Nada':
		col3, col1, col2 = st.columns(3)
	
	col1.markdown('Curva normal 1: Média = 400, S = 50')
	col2.markdown('Curva normal 2: Média = 1000, S = 50')
	
	st.markdown('---')


#===============================================================================================================


if pagina == 'Teorema do limite central':

	'''
	# Teorema do limite central
	'''
	'Vamos verificar as transformação nas distribuições, considerando o teorema'
	
	'''
	#### Algumas citações de Charles Wheelan no livro Estatística: O que é, para que serve, como funciona
	'''

	'Se as amostras de uma população são grandes e aleatórias as médias das amostras serão distribuídas normalmente em torno da média da população.'
	'A maioria das médias das amostras estará razoavelmente perto da média da população. O erro padrão é que define “razoavelmente perto”.'
	'O TLC nos diz a probabilidade de que a média de uma amostra se situe dentro de uma certa distância da média da população.”.'


	st.markdown('---')

	#normal
	st.markdown('# Distribuição Normal')
	normal = ss.norm.rvs(loc = 100, scale = 50, size = 10000 )
	plt.hist(normal, edgecolor = 'white', bins = 50, alpha = 0.5)
	#transformação para normal
	size_amostra_normal = int(st.number_input('Quantidade de amostras para média', 1, 10000, 1, 1))
	lista_normal = []
	for i in range(10000):
		amostra_normal = ss.norm.rvs(loc = 100, scale = 50, size = size_amostra_normal)
		lista_normal.append(amostra_normal.mean())
	plt.hist(lista_normal, color = 'yellow', edgecolor = 'white', bins = 50, alpha = 0.5)
	st.pyplot()	
	st.markdown('---')

	#exponencial
	col9, col10 = st.columns(2)
	st.markdown('# Distribuição Exponencial')
	exponencial = ss.expon.rvs(loc = 0, size = 10000)
	plt.hist(exponencial, edgecolor = 'white', bins = 50)
	#transformação para normal
	bins_amostra_exponencial = int(col10.number_input('Bins Amarelo - Qtd. Colunas', 1, 10000, 50, 10))
	size_amostra_exponencial = int(col9.number_input('Quantidade de amostras para média exponencial', 1, 10000, 1, 1))
	lista_exponencial = []
	for i in range(10000):
		amostra_exponencial = ss.expon.rvs(loc = 0, size = size_amostra_exponencial)
		lista_exponencial.append(amostra_exponencial.mean())
	plt.hist(lista_exponencial, color = 'yellow', edgecolor = 'white', bins = bins_amostra_exponencial, alpha = 0.5)
	st.pyplot()
	st.markdown('---')

	#uniforme
	st.markdown('# Distribuição Uniforme')
	uniforme = ss.uniform.rvs(loc = 0, scale = 10, size = 10000)
	plt.hist(uniforme, edgecolor = 'white', bins = 50)
	#transformação para normal
	col11, col12 = st.columns(2)
	bins_amostra_uniforme = int(col12.number_input('Bins Amarelo -- Qtd. Colunas', 1, 10000, 50, 10))
	size_amostra_uniforme = int(col11.number_input('Quantidade de amostras para média uniforme', 1, 10000, 1, 1))
	lista_uniforme = []
	for i in range(10000):
		amostra_uniforme = ss.uniform.rvs(loc = 0, scale = 10, size = size_amostra_uniforme)
		lista_uniforme.append(amostra_uniforme.mean())
	plt.hist(lista_uniforme, color = 'yellow', edgecolor = 'white', bins = bins_amostra_uniforme, alpha = 0.5)
	st.pyplot()

	#poisson
	st.markdown('# Distribuição Poisson')
	poisson = ss.poisson.rvs(mu = 5, size = 10000)
	plt.hist(poisson, edgecolor = 'white', bins = 30)
	#transformação para normal
	size_amostra_poisson = int(st.number_input('Quantidade de amostras para média poisson', 1, 10000, 1, 1))
	lista_poisson = []
	for i in range(10000):
		amostra_poisson = ss.poisson.rvs(mu = 5, size = size_amostra_poisson)
		lista_poisson.append(amostra_poisson.mean())
	plt.hist(lista_poisson, color = 'yellow', edgecolor = 'white', bins = 50, alpha = 0.5)
	st.pyplot()

	st.markdown('---')


#===============================================================================================================


if pagina == 'Eleição':

	'''
	# Simulador de confiança, pesquisa eleitoral
	'''
	'Tamanho amostral, margem de erro, população e confiança'
	st.markdown('---')
	
	#Entrada de p% real para candidatos:
	col13, col14, col15, col16 = st.columns(4)
	pcanda = int(col13.number_input('Proporção Real de % Intenção Candidato A', 1, 100, 10, 5))
	pcandb = int(col14.number_input('Proporção Real de % Intenção Candidato B', 1, 100, 20, 5))
	pcandc = int(col15.number_input('Proporção Real de % Intenção Candidato C', 1, 100, 30, 5))
	pcandd = int(col16.number_input('Proporção Real de % Intenção Candidato D', 1, 100, 40, 5))
	
	#% total acumulada
	st.markdown('Total: {}%'.format(pcanda + pcandb + pcandc + pcandd))
	if pcanda + pcandb + pcandc + pcandd < 100:
		st.markdown('A somatória da probabilidade está menor que 100%')

	if pcanda + pcandb + pcandc + pcandd > 100:
		st.markdown('A somatória da probabilidade está maior que 100%')

	#proporção real
	propreal = [pcanda, pcandb, pcandc, pcandd]

	#tamanho da população
	npopulação = int(st.number_input('Tamanho da população', 1, 200000000, 100000, 100000))

	#auxiliar para proporção da população
	auxa = "A" * pcanda * int(npopulação/100)
	auxb = "B" * pcandb * int(npopulação/100)
	auxc = "C" * pcandc * int(npopulação/100)
	auxd = "D" * pcandd * int(npopulação/100)

	#população com proporção real
	população = auxa + auxb + auxc + auxd

	#amostras e replicas para cálculo
	col17, col18, col19 = st.columns(3)
	kamostras = int(col17.number_input('Tamanho da amostra', 1, 2000000, 100, 100))
	kreplicas = int(col19.number_input('Réplicas', 1, 200000, 100, 100))
	margemerro = int(col18.number_input('Margem de erro em %', 1, 100, 2, 1))
	res = []
	for i in range(kreplicas):
		amostra = random.sample(população, k = kamostras)
		a = amostra.count("A")/kamostras*100
		b = amostra.count("B")/kamostras*100
		c = amostra.count("C")/kamostras*100
		d = amostra.count("D")/kamostras*100
		estimatitivas = [a, b, c, d]
		erros = np.array(estimatitivas) - np.array(propreal)
		r = np.all(abs(erros) < margemerro)
		res.append(r)

	confiança = np.array(res).mean()

	#respostas
	texto1 = f'Tamanho da população: {npopulação:_}'
	texto2 = f'Tamanho da Amostra: {kamostras:_}'

	
	col17.markdown(texto2.replace('_','.'))
	col18.markdown(f'Margem de Erro estabelecida: {margemerro}%')
	col17.markdown(texto1.replace('_','.'))
	col18.markdown('Confiança estimada: {:2.2%}'.format(confiança))
	
	exibir_dist_conf = col19.selectbox('Exibir margem de confiança?',['Não', 'Sim'])
	rep_exp_conf = 10
	if exibir_dist_conf == 'Sim':
		confloop = []
		for i in range(rep_exp_conf):
			resloop = []
			for i in range(kreplicas):
				amostra = random.sample(população, k = kamostras)
				a = amostra.count("A")/kamostras*100
				b = amostra.count("B")/kamostras*100
				c = amostra.count("C")/kamostras*100
				d = amostra.count("D")/kamostras*100
				estimatitivas = [a, b, c, d]
				erros = np.array(estimatitivas) - np.array(propreal)
				r = np.all(abs(erros) < margemerro)
				resloop.append(r)

			confiança = np.array(resloop).mean()
			confloop.append(confiança)

		conf_minimo = (min(confloop))
		conf_maximo = (max(confloop))

		st.markdown('---')
		st.markdown('A margem de confiança para este experimento, com {} repetições fica entre {:2.2%} e {:2.2%}'.format(rep_exp_conf, conf_minimo, conf_maximo))
		st.markdown('---')

	st.markdown('---')
	'''
	## Calculadora para tamanho de amostra
	'''
	st.markdown('---')

	col20, col21, col22 = st.columns(3)

	#calc_ncand = int(col20.number_input('Canditatos', 1, 20, 4, 1))
	calc_tampop = int(col20.number_input('Tamanho população', 1, 200000000, 100000, 100000))
	calc_margerro = int(col21.number_input('Margem de erro %', 1, 100, 2, 1))
	calc_conf = int(col22.number_input('Confiança', 1, 100, 95, 1))
	
	e = calc_margerro/100
	Z = ss.norm.ppf(calc_conf/100)
	N = calc_tampop
	p = .5

	calc_tamamostra = (N*Z**2*p*(1-p))/((N-1)*(e**2)+(Z**2)*p*(1-p))
	st.markdown(calc_tamamostra)

	calc2_tamamostra = ((Z**2*p*(1-p))/e**2)/(1+((Z**2*p*(1-p))/(e**2*N)))
	st.markdown(calc2_tamamostra)


	n0 = 1/e**2

	calc3_tamamostra = (N*n0)/(N+n0)
	st.markdown(calc3_tamamostra)

	st.markdown('---')
	



