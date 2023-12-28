from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import team_serializer
from rest_framework.response import Response
from .models import *



class team_viewset(viewsets.ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=team_serializer
    










class TeamApiView(APIView):
    def get(self,request):
        allTeams=Team.objects.all().values()
        return Response({"Message":"List of Teams","Team List":allTeams})
    
    def post(self,request):
        Team.objects.create(id=request.data["id"],
                            branch=request.data["branch"],
                            leadname=request.data["leadname"],
                            prn=request.data["prn"],
                            email=request.data["email"],
                            contact=request.data["contact"],
                            mem=request.data["mem"],
                            prn1=request.data["prn1"],
                            email1=request.data["email1"],
                            contact1=request.data["contact1"],
                            mem2=request.data["mem2"],
                            prn2=request.data["prn2"],
                            email2=request.data["email2"],
                            contact2=request.data["contact2"],
                            mem3=request.data["mem3"],
                            prn3=request.data["prn3"],
                            email3=request.data["email3"],
                            contact3=request.data["contact3"],
                            )
        
        team=Team.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Team Added!","Team List":team})