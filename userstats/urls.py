from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats
from django.urls import path


urlpatterns = [
    path('expense_category_data/', ExpenseSummaryStats.as_view(), 
        name='expense_category_summary'),
    path('income_summary_data/', IncomeSourcesSummaryStats.as_view(), 
        name='income_summary_data'),






        
]