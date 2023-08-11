# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"11055","system":"gprdproduct"},{"code":"11056","system":"gprdproduct"},{"code":"13416","system":"gprdproduct"},{"code":"13837","system":"gprdproduct"},{"code":"14644","system":"gprdproduct"},{"code":"14649","system":"gprdproduct"},{"code":"16152","system":"gprdproduct"},{"code":"21110","system":"gprdproduct"},{"code":"21232","system":"gprdproduct"},{"code":"21374","system":"gprdproduct"},{"code":"21395","system":"gprdproduct"},{"code":"21422","system":"gprdproduct"},{"code":"22697","system":"gprdproduct"},{"code":"25735","system":"gprdproduct"},{"code":"25736","system":"gprdproduct"},{"code":"28096","system":"gprdproduct"},{"code":"29837","system":"gprdproduct"},{"code":"33167","system":"gprdproduct"},{"code":"33232","system":"gprdproduct"},{"code":"36194","system":"gprdproduct"},{"code":"42954","system":"gprdproduct"},{"code":"9341","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["biphasic-insulin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["biphasic-insulin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["biphasic-insulin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
