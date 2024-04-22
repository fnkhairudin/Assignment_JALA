import mlflow
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score


# fungsi untuk melakukan model training
def log_training_model(est, 
                       model_name:str, 
                       score_result:list, 
                       target_name,
                       dataset:pd.DataFrame, 
                       name_experiment:str,
                       columntransformer, 
                       **kwargs
                       ):
    """Fungsi untuk melakukan training model dan logging pada dagshub x mlflow

    ## Parameters:
        est : Estimator object
        model_name : Estimator name
        score_result : Empty list to store the metric result
        dataset : train dataset
        name_experiment : experiment name
        columntransformer : variabel yang menyimpan ColumnTransformer

    ## Return:
        None
    """
    # model params
    mlflow.log_params(est.get_params())

    # pipeline
    pipe = Pipeline([
                ('preprocess_1', columntransformer), # scaling RobustScaller
                ('model', est)
                ]).set_output(transform='pandas')
    
    # ytrain
    ytrain = dataset[target_name]

    # training model
    print(f"training model {model_name}", end='\r')
    pipe.fit(dataset.drop(columns=target_name), ytrain)
    
    # hasil prediksi
    ypred = pipe.predict(dataset.drop(columns=target_name))

    # set_tag
    tags = {"model_name": model_name, "experiment-n": name_experiment,}
    # tags untuk mlflow ui
    mlflow.set_tags(tags)

    # hasil metrik evaluasi
    score_result.append({
    'Model' : model_name,
    'MAE': mean_absolute_error(ytrain, ypred),
    'r2_score': r2_score(ytrain, ypred),
    **kwargs
    })

    # log metrics pada mlflow ui
    mlflow.log_metrics({
                    'MAE': mean_absolute_error(ytrain, ypred),
                    'r2_score': r2_score(ytrain, ypred),
                    })
    
    # log model pada mlflow ui
    mlflow.sklearn.log_model(est, "sk_model")
    
    print(f"training model {model_name} is DONE.", end='\r')