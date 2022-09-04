import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('Languages.xlsx')
# Read the values of the file in the dataframe
df = pd.DataFrame(excel_data, columns=['code', 'vn', 'en', 'ja'])

df['vn'] = df['vn'].str.replace('\n', '\\n')
df['en'] = df['en'].str.replace('\n', '\\n')
df['ja'] = df['ja'].str.replace('\n', '\\n')

sample = "<item name=\"{0}\">{1}</item>"

# write xml file
fvn = open("vn/string_code.xml", "w", encoding="utf-8")
fja = open("ja/string_code.xml", "w", encoding="utf-8")
fen = open("en/string_code.xml", "w", encoding="utf-8")
for index, row in df.iterrows():
    # vn file
    if (isinstance(row['vn'], str) == False):
        fvn.write(sample.replace("{0}", row['code']).replace("{1}", '')+'\n')
    else:
        fvn.write(sample.replace("{0}", row['code']).replace("{1}", row['vn'])+'\n')
    # en file
    if (isinstance(row['en'], str) == False):
        fen.write(sample.replace("{0}", row['code']).replace("{1}", '')+'\n')
    else:
        fen.write(sample.replace("{0}", row['code']).replace("{1}", row['en'])+'\n')
    # vn file
    if (isinstance(row['ja'], str) == False):
        fja.write(sample.replace("{0}", row['code']).replace("{1}", '')+'\n')
    else:
        fja.write(sample.replace("{0}", row['code']).replace("{1}", row['ja'])+'\n')
# close file
fvn.close()
fen.close()
fja.close()
