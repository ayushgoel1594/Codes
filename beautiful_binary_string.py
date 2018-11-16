'''
Created on May 28, 2017

@author: ayush
'''
def baeutiful_binary_string(st):
    if '010' in st:
        st=st.replace('010','*')
    print(st.count('*'))
    pass
baeutiful_binary_string('0100101010')