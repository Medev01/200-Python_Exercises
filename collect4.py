from collections import ChainMap


stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

# ChainMap Methode
stocks = ChainMap(stocks_1,stocks_2)
products = ChainMap(techs,finance,gaming)

print(products['Samsung'])
print(stocks)
''' DISPLAY TE VALUE OF PLW'''
print(stocks['PLW'])