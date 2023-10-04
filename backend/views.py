from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import ContactUsSerializer

class ContactUsView(APIView):

    serializer_class = ContactUsSerializer

    def post(self, request):
        print(request.data)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            contactus = serializer.save()
            contactus.save()

            return Response({'message': 'Contact Form Submited Successfuly'}, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            errors.update(serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)