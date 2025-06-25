from django_tenants.utils import schema_context
from django.shortcuts import render
from .serializers import RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from public.models import Client,Domain
from public.serializers import ClientSerializer
from organization.serializers import OrganizationSerializer

# Create your views here.
class RegisterConsultancyView(APIView):
    def post(self,request):
        print("Entered here")
        data = request.data.copy()
        data['user_type'] = 'consultancy'
        
        client_data = {
            "schema_name": data['org_name'],
            "name": data['org_name']
        }

        client_serializer = ClientSerializer(data=client_data)
        if not client_serializer.is_valid():
            return Response(client_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
        org_data = {
            "org_name": data['org_name'],
            "org_address": data['org_address'],
            "org_phone": data['org_phone']
        }
       
        organization_serializer = OrganizationSerializer(data=org_data)
        
        if not organization_serializer.is_valid():
            return Response(organization_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        client = Client(schema_name=data['org_name'],name=data['org_name'])
        client.save()
        # client.create_schema()
        domain = Domain()
        domain.domain = f"{data['org_name']}.localhost"
        domain.tenant = client
        domain.is_primary = True
        domain.save()

        data['client'] = client
        print(data)
        user_serializer = RegisterUserSerializer(data=data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        user_serializer = user_serializer.save()
         
        with schema_context(client.schema_name): 
            organization_serializer.save()
        
        return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)

class DemoView(APIView):
    def get(self,request):
        print("Entered here")
        return Response({"message":"Demo initialized"})