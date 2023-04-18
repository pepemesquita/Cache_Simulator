# Implementação de um Simulador de Caches
Este é o trabalho 2 desenvolvido pelos alunos Amanda Jhennifer Marques Vieira e Pedro Henrique Lima de Mesquita para a disciplina de Arquitetura e Organização de Computadores II do curso de Ciência da Computação da Universidade Federal de Pelotas.

O objetivo deste trabalho é implementar um simulador de cache com a política de substituição random. O simulador pode ser executado através do Python em sua máquina, ou então pelo repositório no Replit.

## Pré-requisitos:
Para executar o simulador em sua máquina é necessário ter o Python instalado. Caso ainda não tenha o Python instalado em sua máquina, você pode baixar o instalador adequado para o seu sistema operacional no site oficial do Python (https://www.python.org/downloads/).

Caso não queira instalar o Python em sua máquina podes optar por rodar o simulador no nosso repositório no replit (https://replit.com/join/ukgapfgtfg-pedro-henriq123)

## Como Executar:

1 - Baixe o arquivo .zip e extraia-o.

2 - Abra o CMD e navegue até o diretório onde você extraiu o arquivo .zip e navegue até a pasta, por exemplo.

	cd "C:\Users\your_username\Downloads\Cache_simulator-master"

3 - No diretório aberto, execute o seguinte comando para criar a cache:

	python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> <arquivo_de_entrada>

	cache_simulator - nome do arquivo de execução principal do simulador.
	nsets - número de conjuntos na cache (número total de “linhas” ou “entradas” da cache).
	bsize - tamanho do bloco em bytes.
	assoc - grau de associatividade (número de vias ou blocos que cada conjunto possui).
	substituição - política de substituição, sendo a única política a Random.
	flag_saida - flag que ativa o modo padrão de saída de dados.
	arquivo_de_entrada - arquivo com os endereços para acesso à cache.

Segue um exemplo com os parâmetros preenchidos no CMD:

	python .\cache_simulator.py 256 4 1 R 0 Endereços/bin_100.bin

## Caso deseje executar no Replit, siga as instruções abaixo:

No Replit, abra o shell e preencha o seguinte comando:

	python cache_simulator.py 256 4 1 R 0 bin_100.bin

## Saída

De acordo com o tipo de flag selecionada (0 ou 1), os resultados esperados para tais entradas são:

Se a flag for 0, a saída será:
	
	Total de Acessos: 100
	Taxa de Hit: 92.0%
	Taxa de Miss: 8.0%
	Taxa de Misses de Conflito: 0.0%
	Taxa de Misses Compulsórios: 100.0%
	Taxa de Misses Capacidade: 0.0%

Se a flag for 1, a saída será:

	100 0.92 0.08 0.0 1.0 0.0

Com esta implementação, esperamos ter oferecido uma maneira simples e intuitiva de simular a política de substituição random na cache. Em caso de dúvidas ou sugestões, fique à vontade para entrar em contato pelo meu e-mail phlmesquita@inf.ufpel.edu.br
