import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)

# Change the second item in the first element in the stocks list 
stocks[0][1] = "CRJ"

print(f"stocks : {stocks}")
print(f"Copied stocks {stocks_copied}")