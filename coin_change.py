def coin_change(coffee_price, eur_inserted):
    # Return the change given a coffee price and euro inserted in a dictionary of the form:
    # {'euro_coin_value':'number_of_coins', 'euro_coin_value':'number_of_coins', ...}
    #
    # Example run:
    # coin_change(coffee_price=3.14, eur_inserted=10)
    #
    # Example return:
    # {2: 3, 0.5: 1, 0.2: 1, 0.1: 1, 0.05: 1, 0.01: 1}

    if coffee_price < 0:
        return 'Wrong coffee price'
    change = round(eur_inserted - coffee_price, 2)

    if change < 0:
        return 'Not enough money inserted'
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coins_change = {}
    for coin in coins:
        while change - coin >= 0:
            if coin not in coins_change:
                coins_change[coin] = 1
            else:
                coins_change[coin] = coins_change[coin] + 1
            change = round(change - coin, 2)

    return coins_change
