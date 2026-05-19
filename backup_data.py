import os
import sys
import django
import json
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core import serializers
from jobs.models import Job
from accounts.models import CustomUser

def backup_data():
    """Backup all important data to JSON files"""

    backup_dir = os.path.join(os.path.dirname(__file__), 'backups')
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')


    jobs = Job.objects.all()
    jobs_data = serializers.serialize('json', jobs, indent=2)
    jobs_file = os.path.join(backup_dir, f'jobs_backup_{timestamp}.json')
    with open(jobs_file, 'w', encoding='utf-8') as f:
        f.write(jobs_data)
    print(f"✅ Jobs backed up: {jobs.count()} records -> {jobs_file}")


    users = CustomUser.objects.all()
    users_data = serializers.serialize('json', users, indent=2)
    users_file = os.path.join(backup_dir, f'users_backup_{timestamp}.json')
    with open(users_file, 'w', encoding='utf-8') as f:
        f.write(users_data)
    print(f"✅ Users backed up: {users.count()} records -> {users_file}")


    with open(os.path.join(backup_dir, 'jobs_latest.json'), 'w', encoding='utf-8') as f:
        f.write(jobs_data)
    with open(os.path.join(backup_dir, 'users_latest.json'), 'w', encoding='utf-8') as f:
        f.write(users_data)

    print(f"\n🎉 Backup complete! Files saved in: {backup_dir}")

def restore_jobs():
    """Restore jobs from latest backup"""
    backup_dir = os.path.join(os.path.dirname(__file__), 'backups')
    jobs_file = os.path.join(backup_dir, 'jobs_latest.json')

    if not os.path.exists(jobs_file):
        print("❌ No backup found!")
        return

    with open(jobs_file, 'r', encoding='utf-8') as f:
        jobs_data = f.read()


    for obj in serializers.deserialize('json', jobs_data):
        obj.save()

    print(f"✅ Jobs restored from backup!")
    print(f"Total jobs now: {Job.objects.count()}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'restore':
        restore_jobs()
    else:
        backup_data()
        print("\n💡 Tip: Run 'python backup_data.py restore' to restore from backup")
