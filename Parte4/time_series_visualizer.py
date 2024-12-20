import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_grouped.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1]).set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")
    fig.savefig('box_plot.png')
    return fig
