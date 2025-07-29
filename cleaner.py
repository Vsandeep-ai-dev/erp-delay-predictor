import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data("data/erp_data.csv", "data/erp_data_clean.csv")
    print("✅ Data cleaned.")
