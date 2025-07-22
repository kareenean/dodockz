import requests

url = "http://localhost:5678/webhook/ai-agent"
data = {
    "chatInput": "клиника по хирургии",
    "sessionId": "test2" 
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:\n", response.text)

#1) найти хирурга по всему Казахстану?
#2) лучший хирург Казахстана 
#3) лучшая клиника по хирургии 
#4) узи в астане