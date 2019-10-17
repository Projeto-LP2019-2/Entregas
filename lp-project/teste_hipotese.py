import statsmodels.stats.weightstats as ws
from app import getInvestimentos, getUbsNotasDesempenho

x1 = [2,3,4,3,5,6] 
x2 = [5,7,8,8,5,4]

def testeIndividual(x1,x2):
    """
    TODO: Cruzar dados.
    X1 = notas das UBS
    X2 = Investimento por estado
    """
    return ws.ttest_ind(x1,x2)

