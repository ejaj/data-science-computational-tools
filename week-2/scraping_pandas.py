import pandas as pd

"""
Reference:
https://towardsdatascience.com/scraping-tabular-data-with-pandas-python-10cf2a133cbf
"""

url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

df_list = pd.read_html(url)
print(len(df_list))

print(df_list[10])

# df = pd.read_html(url, index_col=1)[2]
# print(df.head(4))

# df = pd.read_html(url, match='Number and combined net worth of billionaires by year')[0].head()
#
# print(df.head(10))


# df = pd.read_html(url)[0].tail()
# print(df.head(10))

# df = pd.read_html(
#     url,
#     na_values=["Forbes: The World's Billionaires website"]
# )[0].tail()
# print(df.head(10))
#
# df = pd.read_html(url, skiprows=3, header=0)[0].head()
# print(df.head(10))
