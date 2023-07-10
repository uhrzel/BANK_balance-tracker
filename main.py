import datetime

def update_balance_sheet():
    # Initialize balance to 0
    balance = 0.0
    
    try:
        with open('C:\\Users\\User\\Documents\\textFolder\\AUB_balance.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                balance = float(last_line.split(': ')[1].replace(',', ''))
    except FileNotFoundError:
        pass
    
    continue_process = 'Y'
    while continue_process.upper() == 'Y':
        deposit = input('Enter your deposit amount {} ({}): '.format(datetime.datetime.now().strftime('%m/%d/%y'), datetime.datetime.now().strftime('%I:%M %p')))
        confirm = input('Are you sure (Y/N): ')
        if confirm.upper() == 'Y':
            deposit = deposit.replace(',', '')  
            balance += float(deposit)  
            with open('C:\\Users\\User\\Documents\\textFolder\\AUB_balance.txt', 'a') as file:
                file.write(datetime.datetime.now().strftime('%B %d, %Y (%I:%M %p)') + ': ' + '{:,.2f}'.format(balance) + '\n')  # Format balance with commas
            print('Output: {}: {}'.format(datetime.datetime.now().strftime('%B %d,%Y'), '{:,.2f}'.format(balance)))  # Format balance with commas
        else:
            print('Deposit operation cancelled...')
        continue_process = input('Do you want to continue (Y/N): ')
        if continue_process.upper() == 'N':
            print('Your text file is updated successfully...')

update_balance_sheet()
