import pickle

media_path = "/vol/web/model_ai/"
filename = f"{media_path}model_ads_click.sav"

# load the model from disk
multiple_linear = pickle.load(open(filename, 'rb'))

scale_name = media_path+"scale_ads_click.sav"
# load the model from disk
scale = pickle.load(open(scale_name, 'rb'))

def predict_using_model(sex,age,salary):
    X_test = scale.transform([[sex,age,salary]])

    xoso = multiple_linear.predict(X_test)
    print(xoso[0])
    if xoso[0] == 1:
        return True
    else:
        return False
