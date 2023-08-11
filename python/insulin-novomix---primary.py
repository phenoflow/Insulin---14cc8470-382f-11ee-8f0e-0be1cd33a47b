# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"10001","system":"gprdproduct"},{"code":"10208","system":"gprdproduct"},{"code":"10243","system":"gprdproduct"},{"code":"10244","system":"gprdproduct"},{"code":"10245","system":"gprdproduct"},{"code":"10484","system":"gprdproduct"},{"code":"10887","system":"gprdproduct"},{"code":"11337","system":"gprdproduct"},{"code":"12299","system":"gprdproduct"},{"code":"12818","system":"gprdproduct"},{"code":"13277","system":"gprdproduct"},{"code":"14270","system":"gprdproduct"},{"code":"14290","system":"gprdproduct"},{"code":"14928","system":"gprdproduct"},{"code":"1588","system":"gprdproduct"},{"code":"1592","system":"gprdproduct"},{"code":"1593","system":"gprdproduct"},{"code":"1594","system":"gprdproduct"},{"code":"1595","system":"gprdproduct"},{"code":"1649","system":"gprdproduct"},{"code":"17731","system":"gprdproduct"},{"code":"1805","system":"gprdproduct"},{"code":"1806","system":"gprdproduct"},{"code":"1842","system":"gprdproduct"},{"code":"1843","system":"gprdproduct"},{"code":"1844","system":"gprdproduct"},{"code":"18593","system":"gprdproduct"},{"code":"1886","system":"gprdproduct"},{"code":"20995","system":"gprdproduct"},{"code":"21347","system":"gprdproduct"},{"code":"22058","system":"gprdproduct"},{"code":"2220","system":"gprdproduct"},{"code":"2221","system":"gprdproduct"},{"code":"2454","system":"gprdproduct"},{"code":"2455","system":"gprdproduct"},{"code":"2456","system":"gprdproduct"},{"code":"2459","system":"gprdproduct"},{"code":"24800","system":"gprdproduct"},{"code":"26403","system":"gprdproduct"},{"code":"27614","system":"gprdproduct"},{"code":"2812","system":"gprdproduct"},{"code":"2929","system":"gprdproduct"},{"code":"3396","system":"gprdproduct"},{"code":"33966","system":"gprdproduct"},{"code":"3439","system":"gprdproduct"},{"code":"35260","system":"gprdproduct"},{"code":"3550","system":"gprdproduct"},{"code":"3551","system":"gprdproduct"},{"code":"36513","system":"gprdproduct"},{"code":"39006","system":"gprdproduct"},{"code":"39086","system":"gprdproduct"},{"code":"4163","system":"gprdproduct"},{"code":"42395","system":"gprdproduct"},{"code":"46666","system":"gprdproduct"},{"code":"4706","system":"gprdproduct"},{"code":"4715","system":"gprdproduct"},{"code":"4784","system":"gprdproduct"},{"code":"4790","system":"gprdproduct"},{"code":"5021","system":"gprdproduct"},{"code":"5255","system":"gprdproduct"},{"code":"5845","system":"gprdproduct"},{"code":"5891","system":"gprdproduct"},{"code":"5892","system":"gprdproduct"},{"code":"5933","system":"gprdproduct"},{"code":"6061","system":"gprdproduct"},{"code":"6209","system":"gprdproduct"},{"code":"6958","system":"gprdproduct"},{"code":"6965","system":"gprdproduct"},{"code":"7228","system":"gprdproduct"},{"code":"7231","system":"gprdproduct"},{"code":"7267","system":"gprdproduct"},{"code":"7300","system":"gprdproduct"},{"code":"7319","system":"gprdproduct"},{"code":"7349","system":"gprdproduct"},{"code":"8203","system":"gprdproduct"},{"code":"9521","system":"gprdproduct"},{"code":"9618","system":"gprdproduct"},{"code":"9737","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-novomix---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-novomix---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-novomix---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
