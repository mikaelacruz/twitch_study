import os
import pandas as pd


def combine_csv_files(file_paths):
    # List to store DataFrames
    dfs = []

    # Read each CSV file into a DataFrame, remove the first row and column if applicable, and append to the list
    for file_path in file_paths:
        print("Reading file:", file_path)  # Print file path for debugging
        df = pd.read_csv(file_path)

        # Remove the first row if the file is not the first one
        if 'SullyGnome(1)' in file_path or 'SullyGnome(2)' in file_path or 'SullyGnome(3)' in file_path or 'SullyGnome(4)' in file_path:
            df = df.iloc[1:]

        # Remove the first column
        df = df.iloc[:, 1:]

        dfs.append(df)

    # Concatenate DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df


if __name__ == "__main__":
    # List of file paths for CSV files
    file_paths = [
        '/Users/miki/Downloads/Most watched Twitch streamers, 2023 (English) - SullyGnome.csv',
        '/Users/miki/Downloads/Most watched Twitch streamers, 2023 (English) - SullyGnome(1).csv',
        '/Users/miki/Downloads/Most watched Twitch streamers, 2023 (English) - SullyGnome(2).csv',
        '/Users/miki/Downloads/Most watched Twitch streamers, 2023 (English) - SullyGnome(3).csv',
        '/Users/miki/Downloads/Most watched Twitch streamers, 2023 (English) - SullyGnome(4).csv'
    ]  # Replace with actual file paths

    # Combine CSV files into one DataFrame
    combined_df = combine_csv_files(file_paths)

    # Print combined DataFrame
    print(combined_df)

    # Save combined DataFrame to a CSV file in the downloads directory
    downloads_dir = os.path.expanduser('~/Downloads')
    combined_csv_path = os.path.join(downloads_dir, 'combined_data.csv')
    combined_df.to_csv(combined_csv_path, index=False)
    print(f"Combined DataFrame saved to: {combined_csv_path}")
