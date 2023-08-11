# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"10229","system":"gprdproduct"},{"code":"10264","system":"gprdproduct"},{"code":"10910","system":"gprdproduct"},{"code":"10915","system":"gprdproduct"},{"code":"14362","system":"gprdproduct"},{"code":"16160","system":"gprdproduct"},{"code":"17809","system":"gprdproduct"},{"code":"19877","system":"gprdproduct"},{"code":"19878","system":"gprdproduct"},{"code":"21590","system":"gprdproduct"},{"code":"22155","system":"gprdproduct"},{"code":"23099","system":"gprdproduct"},{"code":"25812","system":"gprdproduct"},{"code":"31258","system":"gprdproduct"},{"code":"35701","system":"gprdproduct"},{"code":"36430","system":"gprdproduct"},{"code":"41120","system":"gprdproduct"},{"code":"44378","system":"gprdproduct"},{"code":"7400","system":"gprdproduct"},{"code":"7793","system":"gprdproduct"},{"code":"8118","system":"gprdproduct"},{"code":"9565","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-flexpen---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-flexpen---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-flexpen---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
