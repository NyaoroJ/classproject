# Given information
basic_pay = 45000
commission_rate = 0.045

# Sales data
sales_data = {
    'James': 56000,
    'John': 74000
}

# Function to calculate net pay
def calculate_net_pay(total_sales):
    commission = total_sales * commission_rate
    net_pay = basic_pay - commission
    return net_pay

# Calculate and display net pay for each salesman
for salesman, total_sales in sales_data.items():
    net_pay = calculate_net_pay(total_sales)
    print(f"{salesman}'s Net Pay: {net_pay:.2f}")
