import seaborn as sns
import matplotlib.pyplot as plt

def topRepos(df):
    plt.figure( figsize=(10, 15) )

    df.num_repos = df.num_repos / 1000

    sns.set_color_codes("pastel")

    ax = sns.barplot(
        x = "num_repos",
        y = "language",
        data = df.iloc[:len(df) + 1,:],
        label = "Total",
        color="b"
    )
    ax.axes.set_title('Top de repositorios por lenguaje', fontsize = 18)
    ax.set_xlabel("Número de Repositorios (en miles)",fontsize = 15)
    ax.set_ylabel("Lenguaje", fontsize = 15)

    plt.show()

def totalIssuesCount(df):
    total_by_date = df.groupby(['date']).sum() / 1000

    plt.figure( figsize=(10, 5) )
    sns.set_theme( style='whitegrid' )

    ax = sns.lineplot(
        x = 'date',
        y = 'count',
        data = total_by_date
    )
    ax.axes.set_title('Total de Ediciones', fontsize = 18)
    ax.set_xlabel("Año", fontsize = 15)
    ax.set_ylabel("Número de Ediciones (en miles)", fontsize = 15)

    plt.show()

def getTop(df, top):
    name_list = df.groupby(['name']).sum().sort_values('count', ascending = False)['count'][:top].index
    return name_list

def topIssuesLanguage(df, top):
    top_issues = df[ df.name.isin(getTop(df, top)) ]
    top_issues['count'] = top_issues['count'] / 1000

    plt.figure( figsize=(10, 5) )
    sns.set_theme( style = 'whitegrid' )

    ax = sns.lineplot(
        x = 'date',
        y = 'count',
        hue = 'name',
        data = top_issues,
    )
    ax.axes.set_title(f'Top {top} de Ediciones por Lenguaje', fontsize = 15)
    ax.set_xlabel("Año", fontsize = 12)
    ax.set_ylabel("Total de Ediciones (en miles)", fontsize = 12)

    plt.show()

def topPrsLanguage(df, top):
    print(type(df))
    top_prs = df[ df.name.isin(getTop(df, top)) ]
    top_prs['count'] = top_prs['count'] / 1000

    plt.figure( figsize = (10, 5) )
    sns.set_theme( style = 'whitegrid' )

    ax = sns.lineplot(
        x = 'date',
        y = 'count',
        hue = 'name',
        data = top_prs
    )
    ax.axes.set_title(f'Top {top} de PRS por Lenguaje', fontsize = 15)
    ax.set_xlabel("Año", fontsize = 12)
    ax.set_ylabel("Total PRS (en miles)", fontsize = 12)

    plt.show()