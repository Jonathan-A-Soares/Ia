import datetime
from googletrans import Translator

x = datetime.datetime.now()


print(x.strftime("%c"))


translator = Translator()
t = translator.translate('veritas lux mea', src='la')
print(t)
