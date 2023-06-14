import pandas as pd

def take_type(hash_code):
    if len(hash_code) == 32:
        return 'MD5'
    if len(hash_code) == 40:
        return 'SHA1'
    if len(hash_code) == 64:
        return 'SHA256'
    return '...'

df = pd.read_csv('IOC_27_04_09_00.csv', sep =';')

##print((df.columns.tolist()))
##df['Activity'] = df['Activity'].astype('string')
df['Type'] = df['Type'].astype('string')
df['IOC'] = df['IOC'].astype('string')
df['Attribution'] = df['Attribution'].astype('string')
df.loc[df['Type'] == 'IP-address', 'Type'] = 'IP'
df['temp'] = df['IOC'].apply(take_type)
df.loc[df['Type'] == 'Hash', 'Type'] = df['temp']
df['processed'] = df['Type']+","+df['IOC']+","+df['Attribution']
df = df[df['Type'] != 'SHA256'].copy()
proc_df = df['processed'].copy()
proc_df.to_csv('example23.csv',header=None,index=False)
