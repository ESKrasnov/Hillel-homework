try:
    print(f'lalalaal')
    raise ValueError
    #print('Close docker')
except Exception as e :
    print(f'Error {e}')
else:
    print('All sucsses')
finally:
    print('Close docker')

with open()