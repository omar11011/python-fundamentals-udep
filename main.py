import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plugins.adjust_date import adjustDate
from plugins.filter_languages import filterLanguages
from plugins.graph import topRepos, totalIssuesCount, topIssuesLanguage, topPrsLanguage
from plugins.regresion import filterPerLenguage, linearModel, prediction

# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

if __name__ == '__main__':
    os.system('cls')

    issues = pd.read_csv('./data/issues.csv')
    prs = pd.read_csv('./data/prs.csv')
    repos = pd.read_csv('./data/repos.csv')

    pd.options.mode.chained_assignment = None 

    # Ajustando fechas
    issues = adjustDate(issues)
    prs = adjustDate(prs)

    # Seleccionando datos de algunos lenguajes
    repos = filterLanguages(repos, 'language')
    prs = filterLanguages(prs, 'name')
    issues = filterLanguages(issues, 'name')

    # Gráfico del número total de repositorios por lenguaje 
    # topRepos(repos)

    # Gráfico del total de ediciones
    # totalIssuesCount(issues)}

    # Gráfico del Top 5 de Ediciones
    # topIssuesLanguage(issues, 5)

    # Gráfico del Top 5 de PRS
    # topPrsLanguage(prs, 5)

    searchedLanguage = "JavaScript"
    data_model = filterPerLenguage(issues, searchedLanguage)
    linear_model = linearModel(data_model)
    prediction_model = prediction(data_model, linear_model)

    # print(prediction)

    plt.plot(data_model["year"], data_model["count"] / 1000, "o", color = "blue")
    plt.plot(pd.DataFrame(data_model["year"]), prediction_model / 1000, c = "red", linewidth = 3)
    plt.xlabel("Año")
    plt.ylabel("Total de Ediciones (en miles)")
    plt.show()

    exit()