from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from backend.models import User
from .models import  SSL_Info, Seeker_Info,   Projects,  Employment_Status, Experience, Qualification, Seeker_Cv
from .serializer import  SSL_InfoSerializer, Seeker_InfoSerializer, ProjectsSerializer, Employment_StatusSerializer, ExperienceSerializer, QualificationSerializer, Seeker_CvSerializer, Seeker_ProfileSerializer, PasswordChangeSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from backend.serializer import UserSerializer

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

class SeekerSigninView(APIView):
    
    def post(self, request):

        print(request.data)
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        print(user)

        if user is not None:
            if user.is_seeker:
                login(request, user)
                sessionid = request.session.session_key
                return Response({'message': 'Signed in successfully', 'sessionid': sessionid}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You are not authorized to sign in as an Job Seeker'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class Seeker_ProfileView(viewsets.GenericViewSet):
    serializer_class = Seeker_ProfileSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['GET'])
    def profile(self, request):
        print("Requested User", request.user)
        
        user_profile = self.queryset.get(id=request.user.id)
        print("DB User", user_profile)
        serializer = self.get_serializer(user_profile)
        
        
        dic = serializer.data
        dic['header'] = request.headers
        return Response(dic)
    

    @action(detail=False, methods=['PUT', 'PATCH'])
    def update_profile(self, request):
        # print(request.PUT)

        user_profile = self.queryset.get(id=request.user.id)
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SeekerSignoutView(APIView):
    
    def get(self, request):
        
        logout(request)
        return Response({'message':f"Signed Our Successfuly"}, status=status.HTTP_200_OK)
    

def index(request):
    return HttpResponse("this is user dashboard")

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(seeker=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seeker=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.seeker != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.seeker != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.seeker != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Seeker_InfoView(BaseModelViewSet):
    serializer_class = Seeker_InfoSerializer
    queryset = Seeker_Info.objects.all()

class SSL_InfoView(BaseModelViewSet):
    serializer_class = SSL_InfoSerializer
    queryset = SSL_Info.objects.all()

class ProjectsView(BaseModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()

class Employment_StatusView(BaseModelViewSet):
    serializer_class = Employment_StatusSerializer
    queryset = Employment_Status.objects.all()

class ExperienceView(BaseModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class QualificationView(BaseModelViewSet):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()

class Job_Seeker_CvView(BaseModelViewSet):
    serializer_class = Seeker_CvSerializer
    queryset = Seeker_Cv.objects.all()

class CreateSeekerView(APIView):

    serializer_class = UserSerializer

    def post(self, request):
        
        print(self.serializer_class)
        print(request.data)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.is_seeker = True
            user.save()

            return Response({'message': 'Seeker created successfully'}, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            errors.update(serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not request.user.check_password(old_password):
                return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

            request.user.set_password(new_password)
            request.user.save()

            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView): # The Token will be Active for 1800 Seconds or 30Min and one try Only
    def post(self, request, format=None):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'No user with this email address'}, status=status.HTTP_400_BAD_REQUEST)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = f"http://127.0.0.1:8000/manager/password_reset/{uid}/{token}/"
            print(reset_link)

            email_subject = 'Password Reset Request'
            email_message = render_to_string('manager/password_reset_email.html', {
                'user': user,
                'reset_link': reset_link,
            })

            # send_mail(email_subject, email_message, 's.209.kaj@outlook.com', [user.email])
            # return render(request,'manager/password_reset_email.html')

            return Response({'message': f'Password reset link:{reset_link}'}, status=status.HTTP_200_OK)
            return Response({'message': 'Password reset link sent to your email'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):

    def post(self, request, uidb64, token, format=None):

        try:

            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print("uid", uid, "--", "user", user)
            print('Token Check: ', default_token_generator.check_token(user, token))

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            serializer = PasswordResetConfirmSerializer(data=request.data)

            if serializer.is_valid():
                new_password = serializer.validated_data['new_password']

                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)