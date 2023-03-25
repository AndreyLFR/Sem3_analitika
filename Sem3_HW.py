import pandas as pd
#Task 1.1
df = pd.read_csv('kc_house_data.csv')
print(f'Task 1.1. {df.head(6)}')

print(df.info())

#Task 1.2
df['delta_renovated'] = df['yr_renovated'] - df['yr_built']
df.loc[df['yr_renovated'] == 0, 'delta_renovated'] = 0
print(df[['delta_renovated', 'yr_renovated', 'yr_built']])

#Task 1.3
print(df['date'])
df['year of sale'] = df['date'].apply(lambda x: int(x[:4]))
df['month of sale'] = df['date'].apply(lambda x: int(x[4:6]))
print(df[['year of sale', 'month of sale', 'date']])

#Task 1.4
df.drop(columns=['date', 'zipcode', 'lat', 'long'], inplace=True)
print(df.info())

#Task 2.1
clients = pd.DataFrame({
    'client_id': [1459, 4684, 3498, 3942, 4535, 2308, 2866, 2765, 1472, 4236, 2295, 939, 3840, 280, 20, 4332, 3475, 4213, 3113, 4809, 2134, 2242, 2068, 4929, 1384, 1589, 3317, 2260, 1727, 1764, 1611, 1474],
    'house_id': [8965450190, 6823100225, 5104540330, 2131701075, 1522700060, 1189000207, 6821600300, 7137950720, 9510920050, 6131600255, 5428000070, 1788800910, 8100400160, 3123049142, 6306800010, 5083000375, 7920100025, 1951600150, 809001400, 339600110, 1622049154, 1099600250, 8563000110, 2768100205, 3995700435, 8861700030, 3303980210, 7731100066, 8146100580, 825069097, 3889100029, 9524100196]
})

clients_join = clients.set_index('house_id')
df_join = df.set_index('id')

joined = clients_join.join(df_join)
print(joined)

#Task 2.2
merged = clients.merge(df, left_on='house_id', right_on='id')
print(merged)

#Task 3.1
mean_price_bedroom = df.groupby('bedrooms').agg({'price': 'mean'}).sort_values('price')
print(mean_price_bedroom)

#Task 3.2
table_price_condition = df.groupby('condition').agg({'price': ['min', 'mean', 'max']})
print(table_price_condition)

#Task 3.3
table_waterfront_view = pd.crosstab(index=df['view'], columns=df['waterfront'])
print(table_waterfront_view)

#Task 3.4
table_floors_bedrooms = df.pivot_table(index='bedrooms', columns='floors', values='price', aggfunc='count', fill_value=0)
print(f'{table_floors_bedrooms}\n c 3 спальнями одноэтажный')

#Task 3.5
table_grade_condition = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)
print(table_grade_condition)