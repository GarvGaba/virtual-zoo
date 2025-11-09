from django import template
import re

register = template.Library()


@register.filter
def extract_youtube_id(url):
    if not url:
        return None
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/v\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/.*[?&]v=([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url, re.IGNORECASE)
        if match:
            return match.group(1)
    return None


@register.filter
def extract_vimeo_id(url):
    if not url:
        return None
    pattern = r'vimeo\.com\/(?:video\/)?(\d+)'
    match = re.search(pattern, url, re.IGNORECASE)
    if match:
        return match.group(1)
    return None
