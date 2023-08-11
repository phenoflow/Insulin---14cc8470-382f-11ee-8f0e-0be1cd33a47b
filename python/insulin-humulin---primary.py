# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"10277","system":"gprdproduct"},{"code":"11107","system":"gprdproduct"},{"code":"14357","system":"gprdproduct"},{"code":"14918","system":"gprdproduct"},{"code":"14944","system":"gprdproduct"},{"code":"1840","system":"gprdproduct"},{"code":"19513","system":"gprdproduct"},{"code":"21235","system":"gprdproduct"},{"code":"4093","system":"gprdproduct"},{"code":"4198","system":"gprdproduct"},{"code":"4199","system":"gprdproduct"},{"code":"4760","system":"gprdproduct"},{"code":"7537","system":"gprdproduct"},{"code":"8841","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-humulin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-humulin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-humulin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
