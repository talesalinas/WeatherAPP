from django.shortcuts import render
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=424AD744-AE89-490D-9F44-51C24F70E950

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=424AD744-AE89-490D-9F44-51C24F70E950")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air Quality is cosidered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(51 - 100) Air quality is Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(51 - 100) Air quality is Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(51 - 100) Air quality is Very Unhealthy"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(51 - 100) Air quality is Hazardous"
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color,
        })
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=424AD744-AE89-490D-9F44-51C24F70E950")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air Quality is cosidered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(51 - 100) Air quality is Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(51 - 100) Air quality is Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(51 - 100) Air quality is Very Unhealthy"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(51 - 100) Air quality is Hazardous"
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color,
        })

def about(request):
    return render(request, 'about.html', {})

def cities(request):
    return render(request, 'cities.html', {})