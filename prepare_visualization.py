# Importing libraries
import pandas as pd
import os

# Define root directories
data_path = "./data/"
output_path = "./output/"

# Create output directory if it does not exist
os.makedirs(output_path, exist_ok=True)

# Load data
file_oct_2023 = "./data/Societats_laborals_en_actiu_oct_2023.csv"
file_oct_2024 = "./data/Societats_laborals_en_actiu_oct_2024.csv"

def load_data(file_path):
    """Create a DataFrame from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None
    
data_oct_2023 = load_data(file_oct_2023)
data_oct_2024 = load_data(file_oct_2024)


# Dimernsion of the data
if data_oct_2023 is not None:
    print(f"Data from {file_oct_2023} has {data_oct_2023.shape[0]} rows and {data_oct_2023.shape[1]} columns.")
if data_oct_2024 is not None:
    print(f"Data from {file_oct_2024} has {data_oct_2024.shape[0]} rows and {data_oct_2024.shape[1]} columns.")

# Define column mapping to match (1st problem to solve)
column_mapping = {
    'cif': 'CIF',
    'n_m_inscripci': 'Núm. inscripció',
    'nom_societat': 'Nom societat',
    'data_constituci': 'Data constitució',
    'ccae': 'CCAE',
    'descripci_ccae': 'Descripció CCAE',
    'sector': 'Sector',
    'adre_a': 'Adreça',
    'cp': 'CP',
    'municipi': 'Municipi',
    'comarca': 'Comarca',
    'prov_ncia': 'Província',
    'capital_social_inicial': 'Capital social inicial',
    'valor_nom_acc_part': 'Valor nom. Acc. Part.',
    'n_m_total_acc_part': 'Núm. total acc/part',
    'socis': 'Socis',
    's_cies_dones': 'Sòcies (dones)',
    'socis_no_treballadors': 'Socis no treballadors',
    's_cies_no_treballadores_dones': 'Sòcies no treballadores (dones)',
    'persones_jur_diques_privades': 'Persones jurídiques privades',
    'persones_jur_diques_p_bliques': 'Persones jurídiques públiques'
}

# Function to reorder and select columns
def reorder_and_select_columns(data, column_mapping):
    available_columns = [col for col in column_mapping if col in data.columns]
    return data[available_columns].rename(columns=column_mapping)

# Apply column mapping
data_oct_2023 = reorder_and_select_columns(data_oct_2023, column_mapping)
data_oct_2023['Year'] = 2023
data_oct_2024['Year'] = 2024

# Preprocessing data - 2nd problem to solve
def preprocess_data(df, year):
    """Preprocess the dataset to normalize formats and add the year column."""
    if df is not None:
        # Normalize 'Data constitució' to datetime
        df['Data constitució'] = pd.to_datetime(df['Data constitució'], errors='coerce')
        
        # Convert 'Capital social inicial' and 'Valor nom. Acc. Part.' to float
        numeric_columns = ['Capital social inicial', 'Valor nom. Acc. Part.']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = df[col].astype(float)
        
        # Add the 'Year' column
        df['Year'] = year
    return df

# Preprocess both datasets
data_oct_2023 = preprocess_data(data_oct_2023, 2023)
data_oct_2024 = preprocess_data(data_oct_2024, 2024)

print(data_oct_2023.dtypes)
print(data_oct_2024.dtypes)

print("Columns in 2023 after renaming and reordering:", data_oct_2023.columns.tolist())
print("Columns in 2024:", data_oct_2024.columns.tolist())

# Verify the first row values for each column
def print_first_row_values(df, label):
    print(f"\nFirst row values for {label}:")
    for col in df.columns:
        print(f"{col}: {df[col].iloc[0]}")

print_first_row_values(data_oct_2023, "2023 Dataset")
print_first_row_values(data_oct_2024, "2024 Dataset")

# Create combined dataset
data_combined = pd.concat([data_oct_2023, data_oct_2024], axis=0)
print(f"\nData combined has {data_combined.shape[0]} rows and {data_combined.shape[1]} columns.")

# Check 'Data constitució' column type and validity
invalid_dates = data_combined['Data constitució'].isnull().sum()
print(f"Number of invalid dates in 'Data constitució': {invalid_dates}")

# Convert 'Capital social inicial' to euros for rows with dates before euro adoption (01/01/2002) - 3rd problem to solve
def convert_to_euros(row):
    if pd.to_datetime(row['Data constitució'], errors='coerce') < pd.Timestamp("2002-01-01"):
        return row['Capital social inicial'] / 166.386
    return row['Capital social inicial']

data_combined['Capital social inicial'] = data_combined.apply(convert_to_euros, axis=1)

# Save sorted dataset as CSV
sorted_csv_file = os.path.join(output_path, "societats_laborals_combined.csv")
data_combined.to_csv(sorted_csv_file, index=False, sep=";", encoding='utf-8')
print(f"Sorted dataset saved as CSV to {sorted_csv_file}.")

# Save sorted dataset as Excel
sorted_excel_file = os.path.join(output_path, "societats_laborals_combined.xlsx")
data_combined.to_excel(sorted_excel_file, index=False, engine='openpyxl')
print(f"Sorted dataset saved as Excel to {sorted_excel_file}.")
