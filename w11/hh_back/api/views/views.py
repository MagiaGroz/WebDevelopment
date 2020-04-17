
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CompanySerializer

def companies(request):
    companies_arr = Company.objects.all()
    companies_json = [company.to_json() for company in companies_arr]
    return JsonResponse(companies_json, safe=False)
def companies_id(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.to_json(),safe=False)
def vacancies(request):
    vacancies_arr = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies_arr]
    return JsonResponse(vacancies_json,safe=False)
def vacancies_id(request,id):
    try:
        vacancy= Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json(), safe=False)
def comp_vacancies(request,id):
    vacancies_arr = Vacancy.objects.filter(company=id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies_arr]
    return JsonResponse(vacancies_json,safe=False)
def top_ten(request):
    vacancies_arr = Vacancy.objects.all().order_by("-salary")[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies_arr]
    return JsonResponse(vacancies_json,safe=False)

class CategoryDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()

        return Response({'deleted': True})