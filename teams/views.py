from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team

# Create your views here.


class TeamView(APIView):
    def post(self, request):
        team_new = request.data
        firt_cup = int(team_new["first_cup"].split("-")[0])
        if team_new["titles"] < 0:
            return Response({"error": "titles cannot be negative"}, 400)
        if firt_cup < 1930:
            return Response({"error": "there was no world cup this year"}, 400)
        if (firt_cup - 1930) % 4 != 0:
            return Response({"error": "there was no world cup this year"}, 400)
        if firt_cup >= 2022:
            return Response(
                {"error": "impossible to have more titles than disputed cups"}, 400
            )
        new_team = Team.objects.create(**team_new)
        return Response(model_to_dict(new_team), 201)

    def get(self, request):
        all_teams = Team.objects.values()
        return Response(all_teams)


class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            unique_team = Team.objects.get(id=team_id)
            return Response(model_to_dict(unique_team), 200)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def patch(self, request, team_id):
        try:
            data = request.data.items()
            team = Team.objects.get(id=team_id)
            for key, value in data:
                setattr(team, key, value)
            team.save()
            return Response(model_to_dict(team), 200)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=204)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
