from tabulate import tabulate

from tools import convert_ms_to_local_time, ms_to_hhmmss


def extract_infos_from_data(data):
    formatted_extract = [{'id': entry['id'], 'task_id':entry['task']['id'], 'task_name':f"'{entry['task']['name']}'", 'start_date':convert_ms_to_local_time(entry['start']),'end_date':convert_ms_to_local_time(entry['end']),'duration':int(entry['duration']) } for entry in data]
    return formatted_extract

def prepare_header_and_rows(time_entries):
    headers = ["Start Time", "End Time", "Duration","Task ID", "Task Name"]
    rows = [[entry['start_date'].strftime('%Y-%m-%d %H:%M:%S'),
            entry['end_date'].strftime('%Y-%m-%d %H:%M:%S'),
            ms_to_hhmmss(entry['duration']),
            entry['task_id'],
            str.replace(entry['task_name'],'|','-'),
            #entry['taskParent']
        ] for entry in time_entries]
    
    return headers,rows
def print_time_entries_as_table(headers,rows):
    table = tabulate(rows, headers, tablefmt='fancy_grid')
    print(table)

def print_total_time_spent(time_entries):
    time_spent = ms_to_hhmmss(sum([entry['duration'] for entry in time_entries]))
    print(f"\nTime tracked today: {time_spent}")

def print_markdown_table(headers,rows):
    # Create the header row
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    # Create the data rows
    data_rows = ["| " + " | ".join(map(str, row)) + " |" for row in rows]
    # Combine all rows
    markdown_table = "\n".join([header_row, separator_row] + data_rows)
    print(markdown_table)