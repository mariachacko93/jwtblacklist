from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# Create your views here. 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken



class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)


# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             access_token = request.data["access_token"]
#             token1 = AccessToken(access_token)
#             token1.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


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

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)
        return Response(status=status.HTTP_205_RESET_CONTENT)