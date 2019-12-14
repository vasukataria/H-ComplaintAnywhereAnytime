from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)

# To execute this file
# python test_mail.py

# Make a cron job to run at 9 am everyday
# $ crontab -e   # Opens the crontab editor
# 0 9 * * * /path/to/script/to/run

# Help: https://crontab.guru/