import pandas as pd
import numpy as np

def calculate_analytics(tasks):

    task_data = []

    for task in tasks:
        task_data.append({
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed = np.sum(df["status"] == "Completed")

    pending = np.sum(df["status"] == "Pending")

    completion_percentage = 0

    if total_tasks > 0:
        completion_percentage = (completed / total_tasks) * 100

    return {
        "total_tasks": int(total_tasks),
        "completed_tasks": int(completed),
        "pending_tasks": int(pending),
        "completion_percentage": round(completion_percentage, 2)
    }