from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthSerializer(serializers.Serializer):
    """
    AuthSerializer is a serializer for handling user authentication data.
    Fields:
        username (str): The username of the user. This field is required.
        password (str): The password of the user. This field is write-only and required.
    """

    class Meta:
        fields = ["username", "password"]

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class LoginView(APIView):
    """
    LoginView handles user authentication.
    Methods:
        post(request):
            Authenticates a user based on provided credentials.
            - Request: Expects a JSON object with 'username' and 'password'.
            - Responses:
                - 200: Login successful.
                - 401: Invalid credentials.
                - 400: Bad request with validation errors.
    """

    @extend_schema(
        request=AuthSerializer,
        responses={
            200: {"description": "Login successful"},
            401: {"description": "Invalid credentials"},
        },
    )
    def post(self, request):
        serializer = AuthSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)

            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    LogoutView handles the user logout process.
    Methods:
        post(request):
            Logs out an authenticated user and returns a success response.
            If the user is not authenticated, returns an unauthorized response.
            Args:
                request (Request): The HTTP request object.
            Returns:
                Response: A response object with a success message and HTTP status 200 if logout is successful.
                          A response object with an error message and HTTP status 401 if the user is not authenticated.
    """

    @extend_schema(
        responses={200: {"description": "Logout successful"}},
    )
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        logout(request)
        return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)
