import PyPDF2
import glob
import re

text = ''

with open(glob.glob("*.pdf")[0], "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for i in range(len(reader.pages)):
        text += reader.pages[i].extract_text()

text_list = text.split('\n')
t_val = 0

PH_TVAL = [4, 3, 2, 1, 0]
IS_TVAL = [7, 6, 3, 1, 0]

for text in text_list:

    if re.match('【.*】', text):
        genre = text

    if re.match('\s+[1-9]+\.0?\s+[Ａ|Ｂ|Ｃ|Ｄ|Ｓ]', text):

        if re.match('.*[一般教養|初習|自由].*', genre):
            continue

        if re.match('.*[必修|基礎].*', genre):
            comp_mul = 1.5
        else:
            comp_mul = 1.0

        split_text = re.split('\s+', text)
        
        if split_text[2] == 'Ｓ':
            t_val += PH_TVAL[0] * float(split_text[1]) * comp_mul
        elif split_text[2] == 'Ａ':
            t_val += PH_TVAL[1] * float(split_text[1]) * comp_mul
        elif split_text[2] == 'Ｂ':
            t_val += PH_TVAL[2] * float(split_text[1]) * comp_mul
        elif split_text[2] == 'Ｃ':
            t_val += PH_TVAL[3] * float(split_text[1]) * comp_mul
        else:
            t_val += PH_TVAL[4] * float(split_text[1]) * comp_mul
        
print(t_val)

