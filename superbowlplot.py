#import modules
import matplotlib.pyplot as plt
import pandas as pd

#create dataframe from csv for plotting
superbowl_df = pd.read_csv('datasets/superbowl-ads.csv')
superbowl_products = superbowl_df.groupby(['Product Type']).count().reset_index()

#pulls colors from matplotlibs color prop cycle
prop = plt.rcParams['axes.prop_cycle']
colors = prop.by_key()['color']

#initialize plot
fig, ax = plt.subplots()
superbar = ax.bar(x = superbowl_products['Product Type'],
                  height = superbowl_df.groupby(['Product Type']).size(),
                  color = colors)

#configure and style bar graph
ax.set_facecolor('xkcd:black')
ax.set_xlabel('Products', color = 'xkcd:orange')
ax.set_ylabel('Amount of Ads(1969-2020)', color = 'xkcd:orange')

ax.bar_label(superbar, color = 'xkcd:white')
ax.spines['bottom'].set_color('xkcd:orange')
ax.spines['left'].set_color('xkcd:orange')
ax.tick_params(axis = 'x', colors = 'xkcd:white')
ax.tick_params(axis = 'y', colors = 'xkcd:white')

fig.set_size_inches(14, 7)
fig.set_facecolor('xkcd:black')

plt.xticks(rotation = 'vertical')
plt.tight_layout()
plt.show()

