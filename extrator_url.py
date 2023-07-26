import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f'URL: {self.url}\nParâmetros: {self.get_url_parametros()}\nURL Base: {self.get_url_base()}'
    
    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def converte_moeda(self, moeda_origem):
        if self.get_valor_parametro(moeda_origem) == 'real':
            valor_convertido = int(self.get_valor_parametro('quantidade')) * 5.5
        elif self.get_valor_parametro(moeda_origem) == 'dolar':
            valor_convertido = int(self.get_valor_parametro('quantidade')) / 5.5
        return valor_convertido



VALOR_DOLAR = 5.5
extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")
print(extrator_url.converte_moeda('moedaOrigem'))
