import sys
import math
import random


def main():
    if len(sys.argv) != 7:
        print("Numero de argumentos incorreto. Utilize:")
        print("python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
        exit(1)

    nsets = int(sys.argv[1])
    bsize = int(sys.argv[2])
    assoc = int(sys.argv[3])
    subst = sys.argv[4]
    flag = int(sys.argv[5])
    file = sys.argv[6]

    print(f'nsets = {nsets}')
    print(f'bsize = {bsize}')
    print(f'assoc = {assoc}')
    print(f'subst = {subst}')
    print(f'flag = {flag}')
    print(f'arquivo = {file}')

    n_bits_offset = int(math.log(bsize, 2))
    n_bits_indice = int(math.log(nsets, 2))

    access, miss_comp, hit, miss_capacidade, miss_conflito = 0, 0, 0, 0, 0
    ver_capacidade, misses_totais = 0, 0

    cache_tag = [[[0, 0] for j in range(assoc)] for i in range(nsets)]

    with open(file, "rb") as f:
        gera = random.Random()

        while True:
            buffer = f.read(4)
            if not buffer:
                break

            endereco = int.from_bytes(buffer, byteorder='big')
            tag = endereco >> (n_bits_offset + n_bits_indice)
            n_bloco = endereco // bsize
            idx = n_bloco % nsets

            if cache_tag[idx][0][1] == 0:
                miss_comp += 1
                misses_totais += 1
                cache_tag[idx][0][0] = tag
                cache_tag[idx][0][1] = 1

            else:
                miss_ocorrido = False

                for i in range(assoc):
                    if tag == cache_tag[idx][i][0] and cache_tag[idx][i][1] == 1:
                        hit += 1
                        miss_ocorrido = True
                        break

                    elif cache_tag[idx][i][1] == 0:
                        miss_comp += 1
                        misses_totais += 1
                        cache_tag[idx][i][0] = tag
                        cache_tag[idx][i][1] = 1
                        miss_ocorrido = True

                        if ver_capacidade < nsets * assoc:
                            ver_capacidade += 1
                        break

                if not miss_ocorrido:
                    r = gera.randint(0, assoc - 1)
                    cache_tag[idx][r][0] = tag
                    cache_tag[idx][r][1] = 1

                    if ver_capacidade < nsets * assoc:
                        ver_capacidade += 1

                    if ver_capacidade == nsets * assoc:
                        miss_capacidade += 1
                        misses_totais += 1

                    else:
                        miss_conflito += 1
                        misses_totais += 1

            access += 1

    taxa_hit = hit / access
    taxa_misses = misses_totais / access
    taxa_compulsorio = miss_comp / misses_totais
    taxa_capacidade = miss_capacidade / misses_totais
    taxa_conflito = miss_conflito / misses_totais

    if flag == 0:
        print(f'Total de Acessos: {access}')
        print(f'Taxa de Hit: {taxa_hit: .1%}')
        print(f'Taxa de Miss: {taxa_misses:.1%}')
        print(f'Taxa de Misses Compulsórios: {taxa_compulsorio:.1%}')
        print(f'Taxa de Misses Capacidade: {taxa_capacidade:.1%}')
        print(f'Taxa de Misses de Conflito: {taxa_conflito:.1%}')

    else:
        print(access, round(taxa_hit, 4), round(taxa_misses, 4), round(taxa_compulsorio, 2), round(taxa_capacidade, 2),
              round(taxa_conflito, 2))


if __name__ == '__main__':
    main()
