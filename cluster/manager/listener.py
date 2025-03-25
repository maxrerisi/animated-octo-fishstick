from task_processing import create_new_task
import os, requests


# TODO big thing is going to be figuring out relative importing


# TODO some flask decorator or maybe i call it using --flags
def create_task():
    worker_link: str = None  # just runner.py
    manager_link: str = None
    columns_of_note: tuple["str"] = ("fold_col", "label_col")
    # manager should have a "task list"
    task_ID = create_new_task()
    os.system(f"mkdir cluster/manager/task-{task_ID}")
    for file in ["references.json", "task_list.csv", "requirements.txt"]:
        file_link = f"{manager_link}/{file}"
        file = f"{task_ID}/{file}"
        response = requests.get(file_link)
        if response.status_code == 200:
            with open(file, "wb") as f:
                f.write(response.content)
        else:
            print(
                f"Failed to download file. Status code: {response.status_code}"
            )  # TODO how to better handle these errors

        # os.system(f"python3 {local_filename}")

    tasks: list = None
    for task in tasks:
        run_task(*task, data_pull_link, param_pull_link, output_post_link)
        # needs something like:
        # while true
        #   sleep(1)
        #   for worker:
        #       if free:
        #           assign next task


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

# TODO input data is simply an
