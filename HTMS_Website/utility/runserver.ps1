# @REM "D:\Python Projects\helpdesk_management_system\Scripts\activate" && cd "D:\Python Projects\helpdesk_management_system\Scripts\HTMS_Website" && python manage.py runserver
# @REM pause
# & "D:\Python Projects\helpdesk_management_system\Scripts\Activate.ps1" ; 
# cd "D:\Python Projects\helpdesk_management_system\Scripts\HTMS_Website" ; 
# python manage.py runserver




Start-Process powershell -Verb runAs -ArgumentList "-Command Set-ExecutionPolicy -ExecutionPolicy Unrestricted; & 'D:\Python Projects\helpdesk_management_system\Scripts\Activate.ps1' ; cd 'D:\Python Projects\helpdesk_management_system\Scripts\HTMS_Website' ; python manage.py runserver"

Start-Process powershell -Verb runAs -ArgumentList "-Command Set-ExecutionPolicy -ExecutionPolicy Unrestricted; & cd 'D:\Python Projects\helpdesk_management_system\Scripts\HTMS_Website\HTMS_App\static\HTMS_App\js'; npm run start"


pause
