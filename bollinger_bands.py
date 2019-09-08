def initialize(context):
    context.jj = sid(4151)
    
    schedule_function(check_bands,date_rules.every_day())
    

def check_bands(context, data):
    cur_price = data.current(context.jj, 'price')
    
    prices = data.history(context.jj, 'price', 20, '1d')
    
    avg = prices.mean()
    std = prices.std()
    lower_band = avg - 2.1*std
    upper_band = avg + 2.1*std
    
    if cur_price <= lower_band:
        order_target_percent(context.jj, 1.0)
        print("Buying")
    elif cur_price >= upper_band:
        order_target_percent(context.jj, -1.0)
        print("shorting")
    else:
        pass
