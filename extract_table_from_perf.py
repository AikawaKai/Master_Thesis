import os
import pandas as pd

basic_tabular1 = """\\hspace*{-0.45in}
                    \\resizebox{.4\\textwidth}{!}{
                    \\begin{subtable}[t]{0.4\\textwidth}
                    \\centering\\footnotesize"""
title_caption = """\\caption*{{{}}}"""
sub_caption = """ """
basic_tabular2 = """
                    \\label{table1}
                    \\end{subtable}}"""
sep_tabular = """\\par\\bigskip\n"""
last_caption = "\\caption{{{}}}"

dict_translate_hier_method = {"TPR-DAGthreshold.free": "TPR-TF",
                              "ISO-TPRthreshold.free": "ISO-TPR-TF",
                              "TPR-DAGthreshold": "TPR-AT",
                              "GPAV": "GPAV",
                              "HTD": "HTD",
                              "flat": "flat",
                              "TPR-W": "TPR-W",
                              "ISO-TPRthreshold": "ISO-TPR-AT"}


if __name__ == '__main__':
    metrics = ["AUC", "PRC"]
    path = "./csv_results/"
    for metric in metrics:
        curr_path = path + metric + "/results/"
        files = [file_ for file_ in os.listdir(curr_path) if not file_.endswith("1")]
        for file_ in files:
            curr_csv = pd.read_csv(curr_path+file_, sep="\t")
            new_file = file_.split(".csv")[0]+"1"
            keys_ = list(curr_csv.keys())
            print(file_)
            header = """\\begin{tabular}{""" + "|"+"|".join(["l" for i in range(9)]) + "|" + """}\n\\hline"""
            keys_2 = ["onto"]+[dict_translate_hier_method[val] for val in keys_[2:]]
            columns = """&""".join([""" \\textbf{""" + val + """} """ for val in keys_2]) + "\\\\ \\hline"
            tot_string = ""
            with open(curr_path+new_file, "w") as curr_new_file:
                for i in range(3):
                    curr_row = [list(curr_csv.iloc[[i]][k]) for k in keys_][1:]
                    curr_line = [val[0] for val in curr_row]
                    curr_line = [curr_line[0]] + [eval(val) for val in curr_line[1:]]
                    onto = curr_line[0]
                    vals = [""" \\textbf{\\footnotesize{""" + str(val[0]) + """$\pm$""" + str(val[1]) + """}} """
                            if val[2] < 0.01 and val[0] > curr_line[1][0]
                            else """\\footnotesize{"""+str(val[0]) + """$\pm$""" + str(val[1]) + """}"""
                            for val in curr_line[2:]]
                    flat_val = """\\footnotesize{""" + str(curr_line[1][0]) + """$\pm$""" + str(curr_line[1][1]) + """}"""
                    curr_line = "&".join([onto, flat_val] + vals) + """\\\\ \\hline"""
                    tot_string += "\n" + curr_line
                tot_string = header + columns + tot_string + """\\end{tabular}"""
                end_string = basic_tabular1 + tot_string + basic_tabular2
                curr_new_file.write(end_string)