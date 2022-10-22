from googletrans import Translator

translater=Translator()

out=translater.translate("How are you?",dest="en")

print(out)
