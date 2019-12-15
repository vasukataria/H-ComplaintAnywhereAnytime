from django.core.mail import send_mail

send_mail(
    'Complaint',
    '48 hours to go stll problem is not sorted.',
    'complaintanywhereanytime@gmail.com',
    ['vasukataria8@gmail.com'],
    fail_silently=False,
)

# To execute this file
    #python test_mail.py

# Make a cron job to run at 9 am everyday
# $ crontab -e   # Opens the crontab editor
# 0 9 * * * /path/to/script/to/run

# Help: https://crontab.guru/