import plotly.express as px
import pandas as pd


def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html


def count_chart(df):
    # Same counts as the table above
    counts = df['manufacturer'].value_counts().reset_index()
    counts.columns = ['Manufacturer', 'Count']

    fig = px.bar(
        counts,
        x='Manufacturer',
        y='Count',
        color='Manufacturer',
        text_auto=True,
        title='Number of Vehicles by Manufacturer'
    )

    # bargap = space between the bars (0 to 1, bigger = more space)
    fig.update_layout(bargap=0.4, template='plotly_white')

    return fig.to_html(full_html=False, include_plotlyjs='cdn')