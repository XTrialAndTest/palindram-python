def sales(sale,buy):
    profit=sale-buy
    return   f'${sale}-${buy}= ${profit}'

print(sales(eval(input('enter the sale price: ')),eval(input('enter the buy price: '))))
