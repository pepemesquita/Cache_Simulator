import math
import sys
import argparse
# python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada
parser = argparse.ArgumentParser(description='Simulador de Cache desenvolvida em python')

parser.add_argument('nsets', type=int, help='Número de conjuntos')
parser.add_argument('bsize', type=int, help='Tamanho do bloco')
parser.add_argument('assoc', type=int, help='Associatividade')
parser.add_argument('substituicao', type=str, help='Algoritmo de substituição')
parser.add_argument('flag_saida', type=int, help='Flag de saída do arquivo')
parser.add_argument('arquivo_de_entrada', type=str, help='Arquivo de entrada')

args = parser.parse_args()

print(args.nsets)
print(args.bsize)
print(args.assoc)
print(args.substituicao)
print(args.flag_saida)
print(args.arquivo_de_entrada)

