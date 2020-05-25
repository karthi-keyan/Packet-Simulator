import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn import svm

def getModel():
    train_data = pd.read_csv("Train_data.csv")
    test_data = pd.read_csv("Test_data.csv")
    #train_data.describe()

    LE = LabelEncoder()

    data=train_data
    data = data.drop(["num_outbound_cmds","is_host_login"],axis=1)
    data = data.dropna(how='any')
    data['protocolType'] = LE.fit_transform(data['protocol_type'])
    data['Service'] = LE.fit_transform(data['service'])
    data['Flag'] = LE.fit_transform(data['flag'])
    data['Class'] = LE.fit_transform(data['class'])
    data = data.drop(["protocol_type","service","flag","class"],axis=1)
    train_data=data

    data=test_data
    data = data.drop(["num_outbound_cmds","is_host_login"],axis=1)
    data = data.dropna(how='any')
    data['protocolType'] = LE.fit_transform(data['protocol_type'])
    data['Service'] = LE.fit_transform(data['service'])
    data['Flag'] = LE.fit_transform(data['flag'])
    data = data.drop(["protocol_type","service","flag"],axis=1)
    test_data=data

    data_temp = train_data.drop(["Class"],axis=1)
    clss = train_data["Class"]
    km = KMeans(
        n_clusters=2, init='random',
        n_init=10, max_iter=300, 
        tol=1e-04, random_state=0
    )
    '''
    km = svm.LinearSVC()'''
    model = km.fit(data_temp)
    return model

