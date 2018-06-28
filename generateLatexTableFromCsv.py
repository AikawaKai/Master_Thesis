import os
import sys


basic_tabular1 = """\\hspace*{-0.45in}
                    \\resizebox{.4\\textwidth}{!}{
                    \\begin{subtable}[t]{0.4\\textwidth}
                    \\centering\\footnotesize"""
title_caption = """\\caption{{{}}}"""
sub_caption = """ """
basic_tabular2 = """
                    \\label{table1}
                    \\end{subtable}}"""
sep_tabular = """\\par\\bigskip\n"""
last_caption = "\\caption{{{}}}"


def getWinLoss(val):
    list_ = eval(val)
    if list_[0]==list_[1]==list_[2] == 0:
        return "-"
    print(list_)
    return str(list_[0]) + "-" + str(list_[1]) + "-" + str(list_[2])

def getFract(val):
    list_ = eval(val)
    return " " + str(list_[0]) + "/" + str(list_[1]) + " "

def vanish(matrix):
    firstrow = matrix[0]
    matrix = matrix[1:]
    nrow = len(matrix)
    ncol = len(matrix[0])
    for i in range(nrow):
        for j in range(ncol):
            if j==0 or j>=i+1 :
                matrix[i][j] = matrix[i][j]
            else:
                matrix[i][j] = "[0, 0, 0]"
    return [firstrow] + matrix

def gen_tabular(csv_file):
    with open(csv_file, "r") as csv_file:
        lines = [["WIN-TIE-LOSS" if l == "" else l for l in [l.strip() for l in line.split("\t")]] for line in csv_file.readlines()]
        lines = vanish(lines)
    header = """\\begin{tabular}{""" + "|"+"|".join(["l" for i in range(0, 2)]) + "|" + """}\n\\hline"""
    title = """&""".join([""" \\textbf{"""+val+"""} """ for val in lines[0][:2]]) + "\\\\ \\hline"
    body = [title]
    for line in lines[2:]:
        curr_line = "&".join([""" \\textbf{"""+line[i]+"""} """ if i==0 else getWinLoss(line[i])
                              for i in range(0, 2)])+"""\\\\ \\hline"""
        #print(curr_line)
        body.append(curr_line)
    end = """\\end{tabular}"""
    final_string = "\n".join([header] + body + [end])
    return final_string


def gen_tabular2(csv_file):
    with open(csv_file, "r") as csv_file:
        lines = [["WIN-TIE-LOSS" if l == "" else l for l in [l.strip() for l in line.split("\t")]] for line in csv_file.readlines()]
        lines = vanish(lines)
    header = """\\begin{tabular}{""" + "|"+"|".join(["l" for i in range(1, len(lines[0]))]) + "|" + """}\n\\hline"""
    first_line = lines[0][0:1]+lines[0][2:]
    title = """&""".join([""" \\textbf{"""+val+"""} """ for val in first_line]) + "\\\\ \\hline"
    body = [title]
    for line in lines[2:]:
        line = line[0:1] + line[2:]
        curr_line = "&".join([""" \\textbf{"""+line[i]+"""} """ if i==0 else getWinLoss(line[i])
                              for i in range(0, len(line))])+"""\\\\ \\hline"""
        #print(curr_line)
        body.append(curr_line)
    end = """\\end{tabular}"""
    final_string = "\n".join([header] + body + [end])
    return final_string



def genSubCaption(metric, ontos, fs):
    string = "Confronto tra i diversi metodi di correzione gerarchica e i metodi flat, per la metrica {}, " \
             "date le diverse ontologie ({}) e i due metodi di riduzione della dimensionalità usati ({}). " \
             "Le tabelle contano le volte in cui, fissato un algoritmo di ML, un metodo ensemble o flat (riga)" \
             " supera un altro metodo (colonna) a livello di performance. Un metodo viene considerato migliorativo " \
             "rispetto al metodo flat, se il test di Wilcoxon rifiuta l'ipotesi nulla (p-value $<$ 0.01)" \
             " e se la media della performance per classe è maggiore.".format(metric, ontos, fs)
    return string

def genSubCaption2(metric, ontos, fs):
    string = "Confronto tra i diversi metodi di correzione gerarchica, per la metrica {}, " \
             "date le diverse ontologie ({}) e i due metodi di riduzione della dimensionalità usati ({}). " \
             "Le tabelle contano le volte in cui, fissato un algoritmo di ML, un metodo ensemble" \
             " ne supera un altro(colonna) a livello di performance. Un metodo viene considerato migliorativo " \
             "rispetto al metodo flat, se il test di Wilcoxon rifiuta l'ipotesi nulla (p-value $<$ 0.01 con correzione di Bonferroni)" \
             " e se la media della performance per classe è maggiore.".format(metric, ontos, fs)
    return string



def write_by_fs(fs_):
    for metric in metrics:
        total_string = ""
        for onto in ontos:
            curr_path = path + "/" + metric + "/" + onto + "/"
            print(curr_path)
            if fs_ is not None:
                curr_files = sorted([f for f in os.listdir(curr_path) if f.endswith(".csv") and fs_ in f],
                                    key=lambda x: x.lower())
            if fs_ is None:
                curr_files = sorted([f for f in os.listdir(curr_path) if f.endswith(".csv")],
                                    key=lambda x: x.lower())
            i = 0
            for file in curr_files:
                if fs_ is not None:
                    string = gen_tabular2(curr_path+file)
                else:
                    string = gen_tabular(curr_path + file)
                fs = file.split(".csv")[0]
                curr_string = basic_tabular1 + "\n" + title_caption.format(""" \\textbf{[""" + metric+"] ["+onto+"] ["+ fs + """]}""") \
                              + "\n" + string + "\n" + basic_tabular2
                if i % 2 == 0:
                    if fs_ is None:
                        #curr_string += sep_tabular
                        pass
                    else:
                        curr_string += sep_tabular
                else:
                    if fs_ is None:
                        curr_string += sep_tabular
                    else:
                        pass
                i += 1
                # print(curr_string)
                total_string += "\n"+curr_string
        if metric == "AUC":
            if fs_ is None:
                with open("testAUC", "w") as w:
                    w.write(total_string+"\n"+last_caption.format(genSubCaption(metrics[0], "BP, MF, CC", "FS, PCA")))
            else:
                with open("testAUC_"+fs, "w") as w:
                    w.write(total_string+"\n"+last_caption.format(genSubCaption2(metrics[0], "BP, MF, CC", "FS, PCA")))
        else:
            if fs_ is None:
                with open("testPRC", "w") as w:
                    w.write(
                        total_string + "\n" + last_caption.format(genSubCaption(metrics[1], "BP, MF, CC", "FS, PCA")))
            else:
                with open("testPRC_"+fs, "w") as w:
                    w.write(total_string+"\n"+last_caption.format(genSubCaption2(metrics[1], "BP, MF, CC", "FS, PCA")))

if __name__ == "__main__":
    path = "/home/kai/Documenti/UNIMI/Master_Thesis/csv_results/"
    metrics = ["AUC", "PRC"]
    ontos = ["BP", "MF", "CC"]
    write_by_fs(None)
    write_by_fs("FS")
    write_by_fs("PCA")



