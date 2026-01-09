import re

def is_phishing(url):
    if len(url) > 75:
        return True
    if "@" in url:
        return True
    if re.search(r"//.+//", url):
        return True
    if url.count('.') > 5:
        return True
    return False

url = input("Enter a URL: ")

if is_phishing(url):
    print("⚠ This URL looks suspicious (possible phishing).")
else:
    print("✅ This URL looks safe.")
