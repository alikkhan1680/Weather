from .serializers import Weather_infoSerializers, UserSerializer
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken




class CountryDataAPIView(APIView):
    def post(self, request):
        country_name = request.data.get("country_Name")  # ✅ POST so‘rovini to‘g‘ri olish

        if not country_name:
            return Response({"Xatolik": "Davlat nomini kiritish kerak"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            countr = Weather.objects.get(country=country_name)  
            serializer = Weather_infoSerializers(countr)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Weather.DoesNotExist:
            try:
                capital = Weather.objects.get(name=country_name)
                serializer = Weather_infoSerializers( capital)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Weather.DoesNotExist:
                return Response({"error": "country or capital not founded"})


class Register(APIView):
    def post(self, request):
        print("Kelgan request:", request.data)  # Debug uchun

        # Avval username borligini tekshiramiz
        if User.objects.filter(username=request.data.get("username")).exists():
            return Response({"error": "Bu username allaqachon ishlatilgan, boshqasini tanlang"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # JWT token yaratish
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "message": "Foydalanuvchi yaratildi",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_data": serializer.data
            }, status=status.HTTP_201_CREATED)

        print("Xato tafsilotlari:", serializer.errors)  # Xato tafsilotlarini chiqarish
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)  # Refresh va Access token yaratish
            user_data = UserSerializer(user).data  # Foydalanuvchi ma'lumotlari
            
            return Response({
                "access_token": str(refresh.access_token),  # Access token
                "refresh_token": str(refresh),  # Refresh token
                "user_data": user_data
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Login yoki parol noto‘g‘ri"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data, "print request")  # Faqat request emas, request.data ni ko'rish

        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token talab qilinadi"}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Refresh tokenni qora ro‘yxatga qo‘shish
            return Response({"message": "Logged out successfully"}, status=200)
        except TokenError:  # Aniqroq xato tutish
            return Response({"error": "Noto‘g‘ri yoki eskirgan refresh token"}, status=400)

        


        
