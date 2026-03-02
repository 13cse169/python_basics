"""Pandas basics examples (guarded imports).

This script shows common pandas operations using in-memory data so it runs without external files.
It detects whether pandas (and matplotlib) are available and prints a helpful message if missing.
"""

from __future__ import annotations

import sys
from io import StringIO

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except Exception as e:
    PANDAS_AVAILABLE = False
    _PANDAS_IMPORT_ERROR = e

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False


def df_creation_examples():
    print("--- DataFrame creation and basic ops ---")
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 40],
        'city': ['NY', 'LA', 'NY', 'SF'],
        'score': [85.5, 92.0, 88.0, None]
    }
    df = pd.DataFrame(data)
    print(df)
    print('\ninfo:')
    print(df.info())
    print('\ndescribe:')
    print(df.describe())


def selection_and_filtering():
    print("--- Selection and filtering ---")
    df = pd.DataFrame({'A': range(10), 'B': [x * 2 for x in range(10)]})
    print('head:\n', df.head())
    print('df["A"] ->', df['A'].tolist())
    print('loc rows 2-5:\n', df.loc[2:5])
    print('iloc row 0-3 columns 0-1:\n', df.iloc[0:3, 0:2])
    print('filter even A:', df[df['A'] % 2 == 0])


def groupby_and_aggregations():
    print("--- groupby and aggregations ---")
    df = pd.DataFrame({
        'team': ['red', 'blue', 'red', 'blue', 'red'],
        'points': [10, 20, 15, 30, 40],
        'assists': [1, 2, 3, 4, 5]
    })
    print('df:\n', df)
    grp = df.groupby('team').agg({'points': 'sum', 'assists': 'mean'})
    print('\ngrouped:\n', grp)


def merge_and_join():
    print("--- merge / join examples ---")
    left = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Carol']})
    right = pd.DataFrame({'id': [2, 3, 4], 'role': ['Dev', 'QA', 'PM']})
    print('left:\n', left)
    print('right:\n', right)
    print('\nmerge inner:\n', pd.merge(left, right, on='id'))
    print('\nmerge outer:\n', pd.merge(left, right, on='id', how='outer'))


def pivot_and_pivot_table():
    print("--- pivot / pivot_table ---")
    df = pd.DataFrame({
        'date': pd.to_datetime(['2021-01-01', '2021-01-01', '2021-01-02']),
        'city': ['NY', 'LA', 'NY'],
        'temperature': [30, 22, 31]
    })
    print('df:\n', df)
    pv = df.pivot_table(index='date', columns='city', values='temperature')
    print('\npivot_table:\n', pv)


def missing_data_handling():
    print("--- missing data handling ---")
    df = pd.DataFrame({'A': [1, None, 3], 'B': [None, 2, 3]})
    print('original:\n', df)
    print('\ndropna:\n', df.dropna())
    print('\nfillna(0):\n', df.fillna(0))


def datetime_and_string_ops():
    print('--- datetime and string operations ---')
    df = pd.DataFrame({'date_str': ['2021-01-01', '2021-02-15', '2021-03-10'], 'name': ['Ann', 'Ben', 'Cara']})
    df['date'] = pd.to_datetime(df['date_str'])
    df['month'] = df['date'].dt.month
    df['name_upper'] = df['name'].str.upper()
    print(df)


def read_write_csv_example():
    print('--- read_csv / to_csv (StringIO) ---')
    csv = 'id,value\n1,10\n2,20\n3,30\n'
    df = pd.read_csv(StringIO(csv))
    print('read from string:\n', df)
    buf = StringIO()
    df.to_csv(buf, index=False)
    print('written csv string:\n', buf.getvalue())


def plotting_example():
    print('--- plotting example (requires matplotlib) ---')
    df = pd.DataFrame({'x': range(10), 'y': [i * i for i in range(10)]})
    if not MATPLOTLIB_AVAILABLE:
        print('matplotlib not available; skipping plot (install matplotlib to enable)')
        return
    ax = df.plot(x='x', y='y', kind='line', title='y = x^2')
    fig = ax.get_figure()
    # show briefly - in non-interactive environments this will not display
    try:
        fig.savefig('pandas_plot_example.png')
        print('saved plot to pandas_plot_example.png')
    except Exception as e:
        print('could not save plot:', e)


def main():
    if not PANDAS_AVAILABLE:
        print('pandas is not installed in this environment.')
        print('Import error:', _PANDAS_IMPORT_ERROR)
        print('Install pandas (pip install pandas) to run these examples.')
        return

    df_creation_examples()
    selection_and_filtering()
    groupby_and_aggregations()
    merge_and_join()
    pivot_and_pivot_table()
    missing_data_handling()
    datetime_and_string_ops()
    read_write_csv_example()
    plotting_example()


if __name__ == '__main__':
    main()
