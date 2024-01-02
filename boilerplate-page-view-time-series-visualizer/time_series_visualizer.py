import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from datetime import datetime
def parse_date(x):
    return datetime.strptime(x, "%Y-%m-%d")
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date',
    date_parser=parse_date)

# Clean data
df['page_views_rank'] = df['value'].rank(pct=True)
df = df[(df['page_views_rank'] >= 0.025) & (df['page_views_rank'] <=
                                            0.975)]
df = df.drop('page_views_rank', axis=1)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))

    ax = sns.lineplot(data=df, x="date", y="value")

    ax.set(
        xlabel="Date",
        ylabel="Page Views"
    )

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
