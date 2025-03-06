import requests
from .models import Weather

API_KEY = "278a4ebf1a0547b881b153445252901"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

CITY_LIST = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
    "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
    "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia",
    "Cuba", "Cyprus", "Czech Republic", "Democratic Republic of the Congo",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini",
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany",
    "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
    "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu",
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

def get_weather_data(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def save_weather_for_all_countries():
    for city in CITY_LIST:
        data = get_weather_data(city)

        if not data or "error" in data:
            print(f"Xatolik yuz berdi: {city}")
            continue

        name = data["location"]["name"]
        country = data['location']['country']
        lat = data['location']['lat']
        lon = data['location']['lon']
        temp_c = data['current']['temp_c']
        wind_kph = data['current']['wind_kph']
        cloud = data['current']['cloud']

        # Ranglarni aniqlash
        temp_color = get_temp_color(temp_c)
        wind_color = get_wind_color(wind_kph)
        cloud_color = get_cloud_color(cloud)

        Weather.objects.filter(name=name, country=country).delete()
        print("eski fetch datalar o'chirildi ")


        # `get_or_create` dan to'g'ri foydalanish
        weather, created = Weather.objects.get_or_create(
            name=name,
            country=country,
            defaults={
                'lat': lat,
                'lon': lon,
                'temp_c': temp_c,
                'temp_color': temp_color,
                'wind_kph': wind_kph,
                'wind_color': wind_color,
                'cloud': cloud,
                'cloud_color': cloud_color
            }
        )
        if created:
            print(f"Yangi ob-havo ma'lumoti qo'shildi: {name}, {country}")
        else:
            print(f"Ma'lumot avvaldan mavjud: {name}, {country}")

def get_temp_color(temp_c):
    if temp_c <= -30:
        return "#003366"
    elif temp_c <= -20:
        return "#4A90E2"
    elif temp_c <= -10:
        return "#B3DFFD"
    elif temp_c <= 0:
        return "#E6F7FF"
    elif temp_c <= 10:
        return "#D1F2D3"
    elif temp_c <= 20:
        return "#FFFACD"
    elif temp_c <= 30:
        return "#FFCC80"
    elif temp_c <= 40:
        return "#FF7043"
    elif temp_c <= 50:
        return "#D32F2F"
    return "#D32F2F"

def get_wind_color(wind_kph):
    if wind_kph <= 10:
        return "#E0F7FA"
    elif wind_kph <= 20:
        return "#B2EBF2"
    elif wind_kph <= 40:
        return "#4DD0E1"
    elif wind_kph <= 60:
        return "#0288D1"
    return "#01579B"

def get_cloud_color(cloud):
    if cloud <= 10:
        return "#FFF9C4"
    elif cloud <= 30:
        return "#FFF176"
    elif cloud <= 60:
        return "#E0E0E0"
    elif cloud <= 90:
        return "#9E9E9E"
    return "#616161"
