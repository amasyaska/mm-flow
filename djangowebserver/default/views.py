from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .functions import calculate_costs, calc_engineer
# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        # total
        print(request.POST)
        print(calculate_costs(model1=int(request.POST['model1'][0]), model2=int(request.POST['model2'][0]), model3=int(request.POST['model3'][0]), model4=int(request.POST['model4'][0]),
                                wl_pow=int(request.POST['wl_sites'][0]), rf_pow=int(request.POST['rf_sites'][0]), se_pow=int(request.POST['se_sites'][0]), months=int(request.POST['months'][0]),
                                survey_price=int(request.POST['survey_price'][0]), transportation_price=int(request.POST['transport_price'][0]),
                                antenna_price=int(request.POST['antenna_price'][0]),
                                equip_bbu_rru_3_price=int(request.POST['bbu_rru_price'][0]), equip_rru_3_price=int(request.POST['rru_3_price'][0]),
                                equip_rru_6_price=int(request.POST['rru_6_price'][0]),
                                dismantling_price=int(request.POST['dismantling_price'][0])
                                ))
        # print(calculate_costs(model1=300, model2=700, model3=700, model4=300,
        #                         wl_pow=40, rf_pow=30, se_pow=25, months=12,
        #                         survey_price=1.0, transportation_price=1.0, antenna_price=1.0,
        #                         equip_bbu_rru_3_price=2.0, equip_rru_3_price=1.7, equip_rru_6_price=2.5, dismantling_price=0.5
        #                         ))
        return render(request, 'summary.html')