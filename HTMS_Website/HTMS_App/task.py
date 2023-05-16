import os
import pandas as pd
from django.contrib.auth.models import Group
from django.db.models import Q
from django.utils import timezone
from HTMS_App.models import Requests
from HTMS_App.email_sender import Email_Sender

def automated_techinicans_report():
    # Get the "Technicians" group
    technicians_group = Group.objects.get(name='Technicians')
    # Get the current time
    now = timezone.now()

    # Get a list of all requests created within the last 24 hours
    recent_requests = Requests.objects.filter(
        Q(request_creation_date__gte=now - timezone.timedelta(hours=24))
    )
    data = []
    # Count the number of open requests and closed requests for each user
    for technician in technicians_group.user_set.all():
        technician_requests = recent_requests.filter(request_technician=technician)
        open_requests_count = technician_requests.filter(request_closed_time=None).count()
        closed_requests_count = technician_requests.exclude(request_closed_time=None).count()
        first_name = technician.first_name.capitalize()
        last_name = technician.last_name.capitalize()
        data.append({
            'Technician': f"{first_name} {last_name} ({technician.username})",
            'Total Requests Assigned': technician_requests.count(),
            'Open Requests': open_requests_count,
            'Closed Requests': closed_requests_count
        })

    dir_loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create a pandas DataFrame from the data
    excel_file_path = f"{dir_loc}/logs/Incident_Count_by_Technicians.xlsx"

    # Create an Excel file with the DataFrame
    excel_data = pd.DataFrame(data=data)

    # Set destination directory to save excel.
    generate_excel = pd.ExcelWriter(
        excel_file_path,
        engine="xlsxwriter",
        datetime_format="dd-mm-yyyy hh:mm:ss",
        date_format="dd-mm-yyyy",
    )

    # Write excel to file using pandas to_excel
    page_name = "Auto_Generated"
    excel_data.to_excel(generate_excel, startrow=0, sheet_name=page_name, index=False)

    # Indicate workbook and worksheet for formatting
    workbook = generate_excel.book
    worksheet = generate_excel.sheets[page_name]

    # Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
    for i, col in enumerate(excel_data.columns):
        # find length of column i
        try:
            column_len = excel_data[col].astype(str).str.len().max()

        except:
            column_len = 12

        # Setting the length if the column header is larger
        # than the max column value length
        try:
            column_len = max(column_len, len(col)) + 4

        except:
            column_len = 12

        # set the column length
        worksheet.set_column(i, i, column_len)

    generate_excel.close()

    Email_Sender(
    "Ahmed Qureshi <ahmed.qureshi@kokilabenhospitals.com>",
    "srinivasan.raman@kokilabenhospitals.com",
    "ahmed.qureshi@kokilabenhospitals.com",
    "Automated Email -- Incident Assigned to Technician Count",
    "",
    "172.20.200.29",
    25,
    excel_file_path
    )
    # Email_Sender(
    # "Ahmed Qureshi <ahmed.qureshi@kokilabenhospitals.com>",
    # "ahmed.qureshi@kokilabenhospitals.com",
    # "ahmed.qureshi@kokilabenhospitals.com",
    # "Automated Email -- Incident Assigned to Technician Count",
    # "",
    # "172.20.200.29",
    # 25,
    # excel_file_path
    # )