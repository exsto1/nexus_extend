def extraction_seq():
    matrix0 = open("macierz_sekwencja/test_matrix_new.csv")
    matrix = matrix0.readlines()
    matrix0.close()
    matrix = [i.rstrip().split(",") for i in matrix]
    matrix = [[int(i) for i in i1] for i1 in matrix]

    labels0 = open("macierz_sekwencja/representative_alignment.fasta")
    labels = labels0.readlines()
    labels0.close()
    labels = [i.rstrip().lstrip(">")[:7] for i in labels if ">" in i]

    result = []
    for i in range(len(labels)):
        result.append([labels[i]])
        result[i].extend(matrix[i])

    result2 = {}
    for i in range(len(result)):
        if result[i][0] not in result2:
            result2[result[i][0]] = [result[i][1:]]
        else:
            result2[result[i][0]].append(result[i][1:])

    for i in result2:
        temp = [0 for i in range(len(result2[i][0]))]
        for i1 in range(len(result2[i])):
            for i2 in range(len(result2[i][i1])):
                temp[i2] += result2[i][i1][i2]
        result2[i] = temp

    for i in result2:
        for i1 in range(len(result2[i])):
            if result2[i][i1] > 0:
                result2[i][i1] = 1

    return result2


if __name__ == "__main__":
    extraction_seq()

