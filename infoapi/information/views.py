from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz


# Create your views here.

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Unknown')
    current_day = datetime.now(pytz.utc).strftime('%A')
    current_utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
    track = request.GET.get('track', 'Unknown')
    github_file_url = 'https://github.com/yourusername/yourrepository/blob/master/path/to/your/file.py'
    github_source_code_url = 'https://github.com/yourusername/yourrepository'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_source_code_url': github_source_code_url,
        'status_code': 'Success'
    }

    return JsonResponse(response_data)
