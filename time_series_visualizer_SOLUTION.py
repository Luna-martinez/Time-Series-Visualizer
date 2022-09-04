import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv").set_index('date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & 
        (df.value <= df.value.quantile(0.975))]

# Draw line plot
def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize = (12, 4))
  df.plot(ax = ax)
  ax.set(title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", 
       ylabel="Page Views", 
       xlabel="Date")
  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Prepare data for monthly bar plot
  df_bar = df.copy().groupby([df.index.year, df.index.month]).mean()

  # Draw bar plot
  ax = df_bar.unstack().plot(kind='bar')
  fig = ax.get_figure()
  ax.legend(title = "Months",
            labels = ['January', 'February', 'March', 'April',  
                      'May', 'June', 'July', 'August', 'September', 
                      'October', 'November', 'December'])
  ax.set(xlabel = "Years", ylabel = "Average Page Views")                 
  fig = ax.get_figure()
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, ax = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
  sns.boxplot(x='year', y='value', data=df_box, ax=ax[0]).set(
                  xlabel='Year', 
                  ylabel='Page Views',
                  title='Year-wise Box Plot (Trend)'
          )
  sns.boxplot(x='month', y='value', data=df_box.loc[~df_box.year.isin([2016, 2019]), :]).set(
                  xlabel='Month', 
                  ylabel='Page Views',
                  title='Month-wise Box Plot (Seasonality)'
          )
          
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig






