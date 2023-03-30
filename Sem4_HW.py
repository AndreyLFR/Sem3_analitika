import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('kc_house_data.csv')
print(df.head(5))
print(df.info())

#Task 1
#частотность стоимости
plt.hist(df['price'], bins=100)
plt.xlim(None, 3500000)
plt.xlabel('цена')
plt.ylabel('кол-во')
plt.title('Плотность распределения домов в разрезе стоимости')
plt.show()
print(f'Task1.2. Частотность стоимости\nНаибольший выбор домов представлен в диапазоне цен от 300 до 750 тыс')

#распределение квадратуры жилой
plt.hist(df['sqft_living'], bins=50)
plt.xlim(None, 8000)
plt.xlabel('площадь дома кв.м.')
plt.ylabel('кол-во')
plt.title('Распределение квадратуры жилой')
plt.show()
print(f'Task1.3. Распределение квадратуры жилой\nНаибольший выбор домов представлен в диапазоне жилой площади от 1000 до 2800 метров')

#распределение года постройки
plt.hist(df['yr_built'], bins=15)
plt.xlabel('год постройки')
plt.ylabel('кол-во')
plt.title('Распределение недвижимости в зависимости от года постройки')
plt.show()
print(f'Task1.4. Распределение года постройки\nНаибольшее количество лотов в домах, построенных после 1940 года')

#распределение домов от наличия вида на набережную
plt.pie(df['waterfront'].value_counts().values, labels=['отсутствует', 'имеется'], autopct='%1.1f%%')
plt.title('Наличие вида на набережной у домов')
plt.show()

data_waterfront = df[df['waterfront'] == 1]['view'].value_counts()
plt.bar(data_waterfront.index, data_waterfront.values)
plt.title('Распределение домов на набережной в разрезе видов')
plt.xlabel('оценка вида')
plt.ylabel('кол-во')
plt.show()
print(f'Task2.1. Распределение домов от наличия вида на набережную\nДоля домов с видом на набережную незначительная и составляет 0.8%. Дома на набережной преимущественно имеют хороший вид')

#Распределение этажей домов
data_floors = df['floors'].value_counts()
plt.bar(data_floors.index, data_floors.values)
plt.title('Распределение домов в зависимости от этажей')
plt.xlabel('номер этажа')
plt.ylabel('кол-во')
plt.show()
print(f'Task2.2. Распределение этажей домов\nДоля домов выше 2 этажей незначительная')

#Распределение состояния домов
data_condition = df['condition'].value_counts()
plt.bar(data_condition.index, data_condition.values)
plt.title('Распределение домов в зависимости от состояния')
plt.xlabel('оценка состояния')
plt.ylabel('кол-во')
plt.show()
print(f'Task2.3. Распределение состояния домов\nДомов в плохом состоянии состоянии немного. Самое большое количество с оценкой 3')

#Исследуйте какие характеристики недвижимости влияют на стоимость с применением не менее 5 диаграмм
corr_matrx = df.corr()
corr_matrx = np.round(corr_matrx, 1)
sns.heatmap(corr_matrx, annot=True)
plt.show()

#зависимость стоимости от оценки
table_price_grade_mean = df.groupby('grade').agg({'price': 'mean'})
table_price_grade_min = df.groupby('grade').agg({'price': 'min'})
table_price_grade_max = df.groupby('grade').agg({'price': 'max'})
n_ticks = np.arange(table_price_grade_mean.shape[0])
plt.bar(n_ticks - 0.2, table_price_grade_min['price'], width=0.2)
plt.bar(n_ticks, table_price_grade_mean['price'], width=0.2)
plt.bar(n_ticks + 0.2, table_price_grade_max['price'], width=0.2)
plt.legend(['min', 'mean', 'max'])
plt.title('Стоимость недвижимости в зависимости \nот оценки дома')
plt.xlabel('оценка')
plt.ylabel('цена')
#pd.options.display.float_format ='{:f}'.format
plt.grid()
plt.xticks(n_ticks, table_price_grade_mean.index);
plt.show()

#оценка влияния на стоимость площади
print(df.sort_values('sqft_above')['sqft_above'])

def conver_sqft(x):
    if x < 2000: res = 'менее 1 тыс'
    elif 2000 <= x < 4000: res = 'менее 4 тыс'
    elif 4000 <= x < 6000: res = 'менее 6 тыс'
    elif 6000 <= x < 8000: res = 'менее 8 тыс'
    else: res = 'более 8 тыс'
    return res

df['convert_above'] = df['sqft_above'].apply(conver_sqft)
data = df.groupby('convert_above').agg({'price': 'mean'})
print(data)
print(data.index)
n_ticks = np.arange(data.shape[0])
plt.bar(n_ticks, data['price'])
plt.title('Зависимость цены от площади дома без учета подвала')
plt.xlabel('площадь')
plt.ylabel('средняя цена')
plt.grid()
plt.xticks(n_ticks, data.index, rotation=50);
plt.show()

sns.boxplot(x=df['price'], y=df['convert_above'], showfliers=False)
plt.xticks(rotation=50)
plt.show()

print(f'Согласно матрице корреляций наибольшее влияние на цену дома оказывает площадь (sqft living, sqft above) и оценка (grade). Чем выше оценка дома, тем выше стоимость дома. Чем больше дом без учета подвала, тем выше его цена')
