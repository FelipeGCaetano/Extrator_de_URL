endereco = "Rua Marquês de Santo Amaro 201, Jardim Gabriella, Jandira, SP, 06626-130"

import re # Regular Expression -- RegEx

# 5 digitos + hífen (opcional) + 3 dígitos


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match 
if busca:
    cep = busca.group() #Retorna a string encontrada 
    print(cep)