from django.urls import path, re_path
from api.views.views import companies,companies_id, comp_vacancies, vacancies, vacancies_id,top_ten,CategoryDetailAPIView

urlpatterns = [
    path('companies',companies),
    path(r'companies/<int:id>/',CategoryDetailAPIView.as_view()),
    path('vacancies',vacancies),
    path(r'vacancies/<int:id>/',vacancies_id),
    path(r'companies/<int:id>/vacancies/',comp_vacancies),
    path(r'vacancies/top_ten/',top_ten)
]