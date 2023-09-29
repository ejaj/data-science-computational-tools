import pandas as pd

# Define the URL of the Wikipedia page containing the table
url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'
df_list = pd.read_html(url)
if len(df_list) > 0:
    selected_table = df_list[0]
    selected_table.to_csv('billionaires_data.csv', index=False)

    print('Billionaires data has been scraped and saved to "billionaires_data.csv".')
else:
    print('No tables found on the Wikipedia page.')
