file_handle = open("clan_outgroup_ali_short_names.nex")
file = file_handle.readlines()
file_handle.close()

seq_len = 0

for i in range(len(file)):
    if "PF" in file[i]:
        seq_len = len(file[i].rstrip().split(" ")[-1])
        break

print(seq_len)

file_handle = open("FeatureMatrix - Evo.tsv")
file1 = file_handle.readlines()
file_handle.close()

file1 = [i.rstrip().split("\t")[0:3] for i in file1[1:]]
print(file1)
lista_deskryptorow = [[i[1][0:7], i[2]] for i in file1 if len(i) == 3]
print(lista_deskryptorow)


if seq_len:
    newfile = open("clan_outgroup_ali_short_names_new.nex", "w")
    for i in range(len(file)):
        if "FORMAT" in file[i]:
            newfile.write(f"FORMAT datatype=mixed(PROTEIN:1-{seq_len},continuous:{seq_len+1}) interleave=yes gap=- missing=?;\n")
        elif "DIMENSIONS" in file[i]:
            newfile.write(f"DIMENSIONS  NTAX=207 NCHAR={seq_len+1};\n")
        else:
            state = False
            for i1 in lista_deskryptorow:
                if i1[0] in file[i]:
                    print(i1[0], file[i])
                    newfile.write(file[i].rstrip() + i1[1] + "\n")
                    state = True
                    break
            if not state:
                newfile.write(file[i].rstrip() + "?\n")

