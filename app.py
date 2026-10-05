# Safe Link AI - Simple Phishing Detector
def check_url(url):
    suspicious_words = ['login', 'verify', 'bank', 'free', 'gift']
    if len(url) > 50 or any(word in url for word in suspicious_words):
        return "⚠️ Phishing Risk Detected!"
    else:
        return "✅ Safe Link"

# Test
url = input("Enter URL to check: ")
print(check_url(url))  
