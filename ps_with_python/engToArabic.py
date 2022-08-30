
QWERTY = {
    'a': 'ش',
    'b': "لا",
    'c': "ؤ",
    'd': "ي",
    'e': "ث",
    'f': "ب",
    'g': "ل",
    'h':"ا",
    'i':"ه",
    'j':"ت",
    'k':"ن",
    'l':"م",
    'm':"ة",
    'n':"ى",
    'o':"خ",
    'p':"ح",
    'q':"ض",
    'r':"ق",
    's':"س",
    't':"ف",
    'u':"ع",
    'v':"ر",
    'w':"ص",
    'x':"ء",
    'y':"غ",
    'z':"ئ",
    ' ': ' ',
    "[": "ج",
    ",": "و" ,
    "`": "ذ" ,
    ".": "ز",
    "]":"د"
}
#gh hk[. uahk ,vhdh ph[hj
str = list(input('Enter the text: '))
for i in range(len(str)):

    try:
        print(QWERTY[str[i]], end='')
    except:
          0 + 0
#output example
'''
Enter the text: gh hk[. uahk ,vhdh ph[hj
لا انجز عشان ورايا حاجات
'''
