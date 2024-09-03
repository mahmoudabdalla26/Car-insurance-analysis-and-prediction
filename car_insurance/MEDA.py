# Import necessary libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datasist.structdata import detect_outliers

# Define helper functions to load, clean, and visualize data

# function to load data
def load_data(file_path):                     
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

# function to clean data and preprocess
import numpy as np
import pandas as pd

def clean_data(df):
    """Perform data cleaning and preprocessing."""
    
    # Replace '?' with NaN in the entire DataFrame
    df.replace('?', np.nan, inplace=True)
    
    # Drop duplicate rows and reset the index
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    # Drop rows where 'is_claim' column has NaN values
    df.dropna(subset=['is_claim'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    # Drop the 'policy_id' column as it's not needed
    df.drop('policy_id', axis=1, inplace=True)
    
    # Convert columns to appropriate data types
    df['policy_tenure'] = df['policy_tenure'].astype(float)  # Convert to float
    df['age_of_policyholder'] = df['age_of_policyholder'].astype(float)  # Convert to float
    df['make'] = pd.to_numeric(df['make'], errors='coerce').round().astype('Int64')  # Convert to integer, coercing errors
    df['population_density'] = pd.to_numeric(df['population_density'], errors='coerce').round().astype('Int64')  # Convert to integer, coercing errors
    df['cylinder'] = pd.to_numeric(df['cylinder'], errors='coerce').round().astype('Int64')  # Convert to integer, coercing errors
    df['length'] = df['length'].astype(float)  # Convert to float
    df['height'] = df['height'].astype(float)  # Convert to float
    df['gross_weight'] = df['gross_weight'].astype(float)  # Convert to float
    df['is_claim'] = pd.to_numeric(df['is_claim'], errors='coerce').round().astype('Int64')  # Convert to integer, coercing errors
    
    # Extract numeric values from 'max_torque' and 'max_power' columns
    df['max_torque'] = df['max_torque'].str.extract(r'(\d+\.?\d*)').astype(float)  # Extract numeric values (including decimals)
    df['max_power'] = df['max_power'].str.extract(r'(\d+\.?\d*)').astype(float)  # Extract numeric values (including decimals)
    
    # Scale 'age_of_car' and 'age_of_policyholder' columns by 100
    df['age_of_car'] = df['age_of_car'] * 100
    df['age_of_policyholder'] = df['age_of_policyholder'] * 100
    
    # Handle missing values in numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns  # Select numerical columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())  # Fill missing values with median
    
    # Handle missing values in categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns  # Select categorical columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])  # Fill missing values with mode
    
    return df


# function to create pie chart 
def create_pie_chart(df, column):
    """Create a pie chart for a given column."""
    return px.pie(df, names=column, color_discrete_sequence=px.colors.sequential.Cividis, template='plotly_dark')

# function to create histograms 
def create_histograms(df, columns):
    """Create histograms for specified columns."""
    num_columns = len(columns)
    num_cols = 3
    num_rows = (num_columns + num_cols - 1) // num_cols

    fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=columns)
    for i, col in enumerate(columns):
        row = i // num_cols + 1
        col_num = i % num_cols + 1
        fig.add_trace(go.Histogram(x=df[col], name=col), row=row, col=col_num)
    fig.update_layout(height=1500, width=1000, showlegend=False, title_text='Histograms of DataFrame Columns')
    fig.update_layout(margin=dict(l=10, r=10, t=50, b=10), template='plotly_dark')
    return fig


def create_histogram_subplots(df, cols):
    """Create histograms for specified columns with subplots."""
    num_cols = 3  # Number of columns in the subplot grid
    num_rows = (len(cols) + num_cols - 1) // num_cols  # Calculate number of rows required

    # Create a subplot figure
    fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=[f'Histogram for {col}' for col in cols])

    # Loop through each column and add a histogram to the subplot grid
    for i, col in enumerate(cols):
        row = i // num_cols + 1  # Calculate the row index
        col_num = i % num_cols + 1  # Calculate the column index

        # Create the histogram for 'No Claims'
        fig.add_trace(
            go.Histogram(x=df[df['is_claim'] == 0][col], name=f'{col} - No Claims', opacity=0.7),
            row=row, col=col_num
        )
        
        # Create the histogram for 'Claims'
        fig.add_trace(
            go.Histogram(x=df[df['is_claim'] == 1][col], name=f'{col} - Claims', opacity=0.7),
            row=row, col=col_num
        )

    # Update layout for each subplot
    fig.update_xaxes(title_text='Value', row=row, col=col_num, tickangle=90)
    fig.update_yaxes(title_text='Count', row=row, col=col_num)

    # Update layout for the entire figure
    fig.update_layout(
        height=1500,
        width=1000,
        showlegend=False,
        title_text='Histograms of DataFrame Columns',
        template='plotly_dark',
        barmode='group'  # Change to 'group' for grouped bar charts
    )
    
    return fig

# function to create correlation heatmap to show correlation between features in the dataset
def correlation_heatmap(df, target_column, num_features):
    """Generate a heatmap of the features most correlated with the target column."""
    correlation_values = df.corr(numeric_only=True)[target_column].abs().sort_values(ascending=True)[:num_features]
    bottom_features = correlation_values.index
    subset_df = df[bottom_features]
    correlation_matrix = subset_df.corr()
    fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='RdBu_r', labels={'color': 'Correlation'}, title=f'Bottom {num_features} Correlation Heatmap')
    fig.update_layout(height=600, width=800, template='plotly_dark')
    return fig