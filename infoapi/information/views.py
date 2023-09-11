import json
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if not slack_name or not track:
        return JsonResponse({'error': 'Both slack_name and track parameters are required.'}, status=400)

    current_day_of_week = datetime.datetime.now().strftime("%A")

    # Get the current UTC time in the specified format
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Validate UTC time within +/-2 hours
    utc_time = datetime.datetime.strptime(
        current_utc_time, "%Y-%m-%dT%H:%M:%SZ")
    now = datetime.datetime.utcnow()
    if abs((utc_time - now).total_seconds()) > 7200:
        return JsonResponse({'error': 'UTC time validation failed.'}, status=400)

    github_url_file = 'https://github.com/yourusername/yourrepo/blob/main/yourfile.py'
    github_url_source = 'https://github.com/yourusername/yourrepo'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day_of_week,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_url_file,
        'github_repo_url': github_url_source,
    }

    return JsonResponse(response_data, status=200)
