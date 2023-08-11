# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"10572","system":"gprdproduct"},{"code":"12638","system":"gprdproduct"},{"code":"12654","system":"gprdproduct"},{"code":"14938","system":"gprdproduct"},{"code":"15710","system":"gprdproduct"},{"code":"16129","system":"gprdproduct"},{"code":"18592","system":"gprdproduct"},{"code":"25479","system":"gprdproduct"},{"code":"26621","system":"gprdproduct"},{"code":"27396","system":"gprdproduct"},{"code":"27402","system":"gprdproduct"},{"code":"4129","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-soluble---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-soluble---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-soluble---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
