import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials



def request_casos():  
    url = 'https://covid19.mathdro.id/api?fbclid=IwAR3O5qKjXCERD2pkA-Y6mSorXBrL1lvu8JgyUvN0UPyfUYjDSRQ5R-pGizs'
    requisicao = requests.get(url) #faço a requisição no site para ter os dados
    dados = requisicao.json()#guardo os dados nesssa variavel
    #print(data['confirmed']['value'])#assim mostra os valores contidos no JSON acessando pelas chaves

    return dados

def atualizar_planilha(dados):

    nomes = ['confirmed', 'recovered', 'deaths']
    celula, coluna = 1, 1
    scope = ['https://spreadsheets.google.com/feeds']
    credenciais = ServiceAccountCredentials.from_json_keyfile_name('casos-covid19-cd13957856b8.json', scope)
    gc= gspread.authorize(credenciais) #pegar as credenciais para acessar a planilha
    id_planilha = gc.open_by_key('1J_MmJ4evuAnj5GNNxma0fn9QJe37yN5nq7APQrBma70')#pegar 'id' da planilha
    planilha = id_planilha.get_worksheet(0)#pego a planilha pelo id dela

    for n in nomes:
        
        planilha.update_cell(celula,coluna, '{} confirmados no Mundo'.format(n))#atualizando a planilha update_cell(cell, colum)
        planilha.update_cell(3,coluna, '{}'.format(dados[n]['value']))
        coluna += 1


r = request_casos()

atualizar_planilha(r)
