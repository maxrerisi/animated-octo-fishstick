from task_processing import create_new_task
import os


# TODO big thing is going to be figuring out relative importing


# some flask decorator
def create_task():
    # TODO figure out a way to turn a github folder into individual files (bc i don't wanna clone and then rename)
    worker_link: str = None
    manager_link: str = None
    # manager should have a "task list"
    os.system(f"mkdir cluster/manager/task-{create_new_task()}")


create_task()

# task list:
# ("xgb", "fold 1")
# ("xgb", "fold 2")
# ("svm", "fold 1")
# ("svm", "fold 2")

# runner.py
# import model_data, data_data
# def func(mdl_str, fold):
# mdl = model_data[mdl_str]["model"]
# grid = model_data[mdl_str]["grid"]
# X_train_outer ... y_test_outer = data_data[fold]
# run ur little grid search
# post results


# TODO is there a way to async things so it just keeps everything running (as opposed to round robin)
