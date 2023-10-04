
from django.shortcuts import get_object_or_404, render
from django.http import FileResponse, HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView

from .serializer import  Company_InfoSerializer, NotificationSerializer, Todo_ListSerializer, Notes_ListSerializer, JobsSerializer, Job_PreferencesSerializer, Job_PreScreenSerializer,  Job_ReviewsSerializer, ApplicationSerializer, Applicant_CandidateViewSerializer, Employer_ProfileSerializer, PasswordChangeSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from .models import  Company_Info, Notification, Todo_List, Notes_List, Jobs, Job_Preferences, Job_PreScreen, Job_Reviews, Application
from backend.serializer import UserSerializer
from backend.models import User

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail

from user.models import Seeker_Cv

class SigninView(APIView):
    
    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:

            if user.is_employer:
                login(request, user)
                return Response({'message': 'Signed in successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You are not authorized to sign in as an employer'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class SignoutView(APIView):
    
    def get(self, request):
        
        logout(request)
        return Response({'message':f"Signed Our Successfuly"}, status=status.HTTP_200_OK)

class index(viewsets.ModelViewSet):
    serializer_class = Todo_ListSerializer
    queryset = Todo_List.objects.all()

class FilterByEmployerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(employer=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data)
        request.data['employer'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilterByJobViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(job__employer=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        instance = Jobs.objects.filter(id=request.data['job'])[0]
        
        if instance.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.job.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.jobs.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.jobs.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyInfoView(FilterByEmployerViewSet):
    serializer_class = Company_InfoSerializer
    queryset = Company_Info.objects.all()

class Todo_ListView(FilterByEmployerViewSet):
    serializer_class = Todo_ListSerializer
    queryset = Todo_List.objects.all()

class Notes_ListView(FilterByEmployerViewSet):
    serializer_class = Notes_ListSerializer
    queryset = Notes_List.objects.all()

class JobsView(FilterByEmployerViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()

class Job_PreferencesView(FilterByJobViewSet):
    serializer_class = Job_PreferencesSerializer
    queryset = Job_Preferences.objects.all()

class Job_PreScreenView(FilterByJobViewSet):
    serializer_class = Job_PreScreenSerializer
    queryset = Job_PreScreen.objects.all()

class Job_ReviewsView(FilterByJobViewSet):
    serializer_class = Job_ReviewsSerializer
    queryset = Job_Reviews.objects.all()


class CreateEmployerView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.is_employer = True
            user.save()

            return Response({'message': 'Employer created successfully'}, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            errors.update(serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class Application(viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        
        queryset = self.queryset.filter(job__employer=request.user)

        serializer = self.serializer_class(queryset, many=True)

        response_data = []

        for application_data in serializer.data:            
            application = Application.objects.get(id=application_data['id'])

            seeker = application.seeker
            job = application.job

            response_item = {
                'id': application.id,
                'seeker_name': f"{seeker.first_name} {seeker.last_name}",
                'match': application.match,
                'applied_date': application.applied_date,
                'status': application.status,
                'job_title': job.title,
            }

            response_data.append(response_item)

        return Response(response_data)        

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)

        if instance.job.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(instance)

        response_item = {
            'id': instance.id,
            'seeker_name': f"{instance.seeker.first_name} {instance.seeker.last_name}",
            'match': instance.match,
            'applied_date': instance.applied_date,
            'status': instance.status,
            "seeker cv": instance.seeker.cv.id,
            'Seeker Data': {
                "Seeker Info": {
                    "First Name": instance.seeker.first_name,
                    "Last Name": instance.seeker.last_name,
                    "Email": instance.seeker.email,
                },
                "Seeker Qualifications": [
                    {
                        "Qualification Name": q.education_level,
                        "Institution": q.institute,

                    } for q in instance.seeker.qualification.all()
                ],
                "Seeker Projects": [
                    {
                        "Project Title": project.role,
                        "Description": project.description,

                    } for project in instance.seeker.projects.all()
                ],
            },
        }

        # Add the custom response item to the serialized data.
        serialized_data = serializer.data
        serialized_data.update(response_item)

        return Response(serialized_data)
    
    def update(self, request, *args, **kwargs):

        instance = self.get_object()
        if instance.job.employer != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Download_CV(APIView):
    
    def get(self, request, cv_id):
        
        cv = get_object_or_404(Seeker_Cv, id=cv_id)
        
        user = request.user
        has_access = Application.objects.filter(job__employer=user, seeker__cv=cv).exists()
        
        if not has_access:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        cv_file = cv.cv_file.open(mode='rb')

        response = FileResponse(cv_file)
        
        response['Content-Type'] = 'application/pdf'  # You can adjust the content type based on the file type
        response['Content-Disposition'] = f'attachment; filename="{cv.cv_file.name}"'
        
        return response
    
class ProfileView(viewsets.GenericViewSet):
    serializer_class = Employer_ProfileSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['GET'])
    def profile(self, request):
        print(request.user)
        
        user_profile = self.queryset.get(id=request.user.id)
        print(user_profile)
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

    @action(detail=False, methods=['PUT', 'PATCH'])
    def update_profile(self, request):

        user_profile = self.queryset.get(id=request.user.id)
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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


class NotificationListView(viewsets.GenericViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self,requst):
        return Response(self.queryset,status=status.HTTP_200_OK)





















