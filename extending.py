import numpy as np
from extract_info_from_seq_matrix import extraction_seq
from extract_info_from_feature_matrix import extraction_feautre


def get_total_length(data):
    tot_len = []
    for i in range(len(data)):
        for i1 in data[i]:
            tot_len.append(len(data[i][i1]))
            break
    return tot_len


def load_nexus_data(file_name):
    file_handle = open(file_name)
    file = file_handle.readlines()
    file_handle.close()

    seq_len = None

    for i in range(len(file)):
        if "PF" in file[i]:
            seq_len = len(file[i].rstrip().split(" ")[-1])
            break

    return file, seq_len


def file_modify(file, newfile_name, matrix, seq_len, matrix_len):
    if seq_len:
        newfile = open(newfile_name, "w")
        for i in range(len(file)):
            if "FORMAT" in file[i]:
                newfile.write(f"FORMAT datatype=mixed(PROTEIN:1-{seq_len},Standard:{seq_len+1}-{seq_len+sum(matrix_len)}) interleave=yes gap=- missing=?;\n")
            elif "DIMENSIONS" in file[i]:
                newfile.write(f"DIMENSIONS  NTAX=207 NCHAR={seq_len+sum(matrix_len)};\n")
            elif "PF" in file[i]:
                temp = ""
                for i1 in range(len(matrix)):
                    state = False
                    for i2 in matrix[i1]:
                        if i2 in file[i]:
                            temp += "".join([str(i0) for i0 in matrix[i1][i2]])
                            state = True
                    if not state:
                        temp += "?"*matrix_len[i1]
                newfile.write(file[i].rstrip() + temp + "\n")
            else:
                newfile.write(file[i])
#
#
# new_matrix = np.zeros((len(lista_deskryptorow), len(lista_deskryptorow)))
# for i in range(len(lista_deskryptorow)):
#     for i1 in range(len(lista_deskryptorow)):
#         if lista_deskryptorow[i][1] == lista_deskryptorow[i1][1]:
#             new_matrix[i, i1] = 1
#
#
# do_zapisu = [i[0] for i in lista_deskryptorow]
# header_txt = ";" + ";".join(do_zapisu)
# np.savetxt("macierz_cech", new_matrix, "%d", delimiter=";")
#
# old_file = open("macierz_cechy/macierz_cech").readlines()
# old_file = [lista_deskryptorow[i][0] + ";" + old_file[i] for i in range(len(old_file))]
#
# print(len(lista_deskryptorow), new_matrix.shape[0])
#
# new_file = open("macierz_cechy/nowa_macierz.csv", "w")
# new_file.write(header_txt + "\n")
# for i in old_file:
#     new_file.write(i)


if __name__ == "__main__":
    seq_matrix_data = extraction_seq()
    feauture_matrix_data = extraction_feautre(10)
    matrix_data = [seq_matrix_data, feauture_matrix_data]
    expand_length = get_total_length(matrix_data)
    nexus_file, base_length = load_nexus_data("clan_outgroup_ali_short_names.nex")
    file_modify(nexus_file, "newfile.nexus", matrix_data, base_length, expand_length)
