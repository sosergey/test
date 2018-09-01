import pandas as pd
fread = pd.read_csv('apple.csv',index_col='Date', parse_dates=True)
fread = fread.sort_index()

print(
    fread.resample('W')['Close'].mean()
      )

import matplotlib.pyplot as plt

new_sample_df = fread.loc['2012-Feb':'2017-Feb', ['Open']]
new_sample_df.plot()
plt.show()