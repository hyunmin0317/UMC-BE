import requests
from rest_framework import views, status
from rest_framework.response import Response


def covid19_API(n):
    URL = f'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/{n}/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data


class CovidViewSet(views.APIView):
    def get(self, request):
        return Response(covid19_API(365), status=status.HTTP_200_OK)


class CovidDateViewSet(views.APIView):
    def get(self, request, date):
        data = covid19_API(365)
        for d in data:
            if date == d['T_DT'][2:10]:
                return Response(d, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
