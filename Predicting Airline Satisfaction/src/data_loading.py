def load_raw_data(folder_path=FOLDER):
    train = pl.read_csv(f'{FOLDER}/train.csv').drop("id")
    test  = pl.read_csv(f'{FOLDER}/test.csv').drop("id")
    sample_submission = pd.read_csv(f'{FOLDER}/sample_submission.csv')
    
    print(f"Train Data's Shape: {train.shape}")
    print(f"Test Data's Shape:  {test.shape}")
    print(f"Submission File's Shape: {sample_submission.shape}")
    return train, test, sample_submission
