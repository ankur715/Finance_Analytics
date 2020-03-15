# #!/usr/bin/env python
# # coding: utf-8

# # In[1]:


# import matplotlib.pyplot as plt
# from matplotlib import style
# import numpy as np

# style.use('ggplot')


# # Next, we'll begin to build the visualization function:
# # 
# # 

# # In[2]:


# def visualize_data():
#     df = pd.read_csv('sp500_joined_closes.csv')


# # At this point, we could graph any company:
# # 
# # 

# # In[ ]:


# df['AAPL'].plot()
# plt.show()


# # Let's look into the correlation of all of these companies. Building a correlation table in Pandas is actually unbelievably simple:

# # In[ ]:


# df_corr = df.corr()
# print(df_corr.head())


# # The .corr() automatically will look at the entire DataFrame, and determine the correlation of every column to every column. I've seen paid websites do exactly this as a service. So, if you need some side capital, there you have it!

# # In[ ]:


# df_corr.to_csv('sp500corr.csv')


# # Instead, we're going to graph it. To do this, we're going to make a heatmap. There isn't a super simple heat map built into Matplotlib, but we have the tools to make on anyway. To do this, first we need the actual data itself to graph:

# # In[ ]:


# data1 = df_corr.values


# # This will give us a numpy array of just the values, which are the correlation numbers. Next, we'll build our figure and axis. Then we'll create a heatmap.

# # In[ ]:


# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)

# heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)


# # This heatmap is made using a range of colors, which can be a range of anything to anything, and the color scale is generated from the cmap that we use. You can find all of the options for color maps here. We're going to use RdYlGn, which is a colormap that goes from red on the low side, yellow for the middle, and green for the higher part of the scale, which will give us red for negative correlations, green for positive correlations, and yellow for no-correlations. We'll add a side-bar that is a colorbar as a sort of "scale" for us:
# # 
# # Next, we're going to set our x and y axis ticks so we know which companies are which, since right now we've only just plotted the data:

# # In[ ]:


# fig1.colorbar(heatmap1)
# ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
# ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)

# ax1.invert_yaxis()
# ax1.xaxis.tick_top()


# # What this does is simply create tick markers for us. We don't yet have any labels.
# # 
# # This will flip our yaxis, so that the graph is a little easier to read, since there will be some space between the x's and y's. Generally matplotlib leaves room on the extreme ends of your graph since this tends to make graphs easier to read, but, in our case, it doesn't. Then we also flip the xaxis to be at the top of the graph, rather than the traditional bottom, again to just make this more like a correlation table should be. Now we're actually going to add the company names to the currently-nameless ticks:
# # 
# # We rotate the xticks, which are the actual tickers themselves, since normally they'll be written out horizontally. We've got over 500 labels here, so we're going to rotate them 90 degrees so they're vertical. It's still a graph that's going to be far too large to really see everything zoomed out, but that's fine. The line that says heatmap1.set_clim(-1,1) just tells the colormap that our range is going to be from -1 to positive 1. It should already be the case, but we want to be certain. Without this line, it should still be the min and max of your dataset, so it would have been pretty close anyway.

# # In[ ]:


# column_labels = df_corr.columns
# row_labels = df_corr.index
# ax1.set_xticklabels(column_labels)
# ax1.set_yticklabels(row_labels)

# plt.xticks(rotation=90)
# heatmap1.set_clim(-1,1)
# plt.tight_layout()
# #plt.savefig("correlations.png", dpi = (300))
# plt.show()


# # In[4]:


import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

style.use('ggplot')

def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()
    print(df_corr.head())
    df_corr.to_csv('sp500corr.csv')
    data1 = df_corr.values
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
    fig1.colorbar(heatmap1)

    ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
    ax1.invert_yaxis()
    ax1.xaxis.tick_top()
    column_labels = df_corr.columns
    row_labels = df_corr.index
    ax1.set_xticklabels(column_labels)
    ax1.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap1.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()


visualize_data()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




