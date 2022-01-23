languages = ['JavaScript', 'Python', 'PHP', 'C', 'C++', 'C#', 'Java', 'Ruby', 'HTML', 'Perl', 'R', 'CSS', 'TypeScript', 'Go', 'Shell']

def filterLanguages(df, column):
    df["verify"] = df[column].apply(lambda x: x in languages)
    df = df[ df["verify"] == True ]
    df = df.drop(['verify'], axis=1)

    return df