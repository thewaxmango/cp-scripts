FILEIN = "to_ahk_in.txt"
FILEOUT = "to_ahk_out.txt"

with open(FILEIN, 'r') as fin:
    with open(FILEOUT, 'w') as fout:
        for line in fin:
            fout.write(line.rstrip().replace("\t", "") + "`n")