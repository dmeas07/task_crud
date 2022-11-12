import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(task_id):
    task_dictionary = {
        "id": task_id
    }

    url = "%s/%s" % (BASE_URL, task_id)
    response = requests.put(url, json=task_dictionary)
    if response.status_code == 204:
        print("Task Delete Success!")
    else:
        print("DELETE Failed!")


if __name__ == "__main__":
    task_id = input("Target task id: ")
    delete_task(task_id)