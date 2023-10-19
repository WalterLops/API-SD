from rest_framework import generics
from .models import CadastroDispositivo, Falha
from django.shortcuts import render
from .serializers import CadastroDispositivoSerializer, FalhaSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])  
        user.save()

class CustomTokenObtainPairView(TokenObtainPairView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.user
            response.data['user_id'] = user.id
        return response

class CustomTokenRefreshView(TokenRefreshView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.user
            response.data['user_id'] = user.id
        return response

def endpoint_list(request):
    return render(request, "endpoints.html")

def escolher_documentacao(request):
    if request.method == 'POST':
        escolha = request.POST.get('documentacao')
        if escolha == "swagger":
            return render(request, 'documentacao.html', {'escolha': 'swagger'})
        elif escolha == "drf":
            return render(request, 'documentacao.html', {'escolha': 'drf'})

    return render(request, 'documentacao.html')

## API --

class CadastroDispositivoList(generics.ListCreateAPIView):
    queryset = CadastroDispositivo.objects.all()
    serializer_class = CadastroDispositivoSerializer
    #permission_classes = [IsAuthenticated]

class CadastroDispositivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CadastroDispositivo.objects.all()
    serializer_class = CadastroDispositivoSerializer
    #permission_classes = [IsAuthenticated]

class FalhaList(generics.ListCreateAPIView):
    queryset = Falha.objects.all()
    serializer_class = FalhaSerializer
    #permission_classes = [IsAuthenticated]

class FalhaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Falha.objects.all()
    serializer_class = FalhaSerializer
    #permission_classes = [IsAuthenticated]
