from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# Create your views here. 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        
        content = {'message': 'Welcome User!!'}
        return Response(content)



from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(('POST',))
def LogoutView(request):
    """Blacklist the refresh token: extract token from the header
      during logout request user and refresh token is provided"""
    Refresh_token = request.data["refresh"]
    token = RefreshToken(Refresh_token)
    token.blacklist()
    return Response("Successful Logout", status=status.HTTP_200_OK)

@api_view(('POST',))
def LogoutAllView(request):
    tokens = OutstandingToken.objects.filter(user_id=request.user.id)
    for token in tokens:
        t, _ = BlacklistedToken.objects.get_or_create(token=token)
    return Response("logged out of all devices",status=status.HTTP_205_RESET_CONTENT)