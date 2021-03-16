def extraction_feautre(powtorzenia):
    file_handle = open("macierz_cechy/FeatureMatrix - Evo.tsv")
    file1 = file_handle.readlines()
    file_handle.close()

    file1 = [i.rstrip().split("\t")[0:3] for i in file1[1:]]
    lista_deskryptorow = [[i[1][0:7], i[2]] for i in file1 if len(i) == 3]

    result = {}
    for i in lista_deskryptorow:
        if i[0] not in result:
            result[i[0]] = [i[1] for i1 in range(powtorzenia)]

    return result


if __name__ == "__main__":
    extraction_feautre(1)
