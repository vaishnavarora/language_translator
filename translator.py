from translate import Translator
trans = Translator(to_lang = 'ja')
try:
    with open("./test.txt", mode = 'r') as files:
        txt = files.read()
        transla = trans.translate(txt)
    with open("./test_lang_change.txt", mode = 'w',encoding = 'UTF-8') as files2:
        files2.write(transla)
except:
  print("error 104 file not found")
print("conversion successful")
