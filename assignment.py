def calculate_discount(price, discount_percent):
    if (discount_percent >= 20) :
        return (price * (100 - discount_percent))/100
    return price
original_price = int(input('enter price:'))

discount = int(input('enter discount:'))

final_price = calculate_discount(original_price, discount)

print('The final price after discount is:', final_price)