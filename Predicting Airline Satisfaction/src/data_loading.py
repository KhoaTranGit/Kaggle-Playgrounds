def clean_col(col):
    return re.sub(r"[ /-]+", "_", col.lower())
    
def load_raw_data(folder_path=FOLDER):
    train = pl.read_csv(f'{folder_path}/train.csv').drop("id").rename(clean_col)
    test  = pl.read_csv(f'{folder_path}/test.csv').drop("id").rename(clean_col)
    sample_submission = pd.read_csv(f'{folder_path}/sample_submission.csv')

    print(f"Train Data's Shape: {train.shape}")
    print(f"Test Data's Shape:  {test.shape}")
    print(f"Submission File's Shape: {sample_submission.shape}")
    return train, test, sample_submission
