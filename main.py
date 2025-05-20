from config import REPORT_EMAIL
from notifier import send_report

def filter_and_summarize(data):
    total = sum([item for item in data if item >= 0])
    count = len([item for item in data if item >= 0])
    average = total / count if count != 0 else 0
    return total, count, average

def process_data(data):
    for item in data:
        print("Processing positive item:" if item >= 0 else "Skipping negative item:", item)

    total, count, average = filter_and_summarize(data)
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)

    send_report(REPORT_EMAIL)

data = [10, -5, 20, -2, 30]
process_data(data)


