from rest_framework.response import Response
from rest_framework.views import APIView
import xlrd
from .models import Ohio
from .serializer import OhiolSerializer

# Create your views here.


def setData():
    loc = ("Taskexel.xls")   
    wb = xlrd.open_workbook(loc)     
    sheet = wb.sheet_by_index(0) 
    num_rows = sheet.nrows - 1
    curr_row = 1
    while curr_row < num_rows:
        api_well_number = sheet.cell_value(curr_row, 0)
        oil = sheet.cell_value(curr_row, 8)
        gas = sheet.cell_value(curr_row, 9)
        brine = sheet.cell_value(curr_row, 10)
        quater= 'q'+str(int(sheet.cell_value(curr_row, 2)))
        if Ohio.objects.filter(api_well_number=str(api_well_number),quater=quater).exists():
            well=Ohio.objects.get(api_well_number=str(api_well_number))  
            well.oil+=oil
            well.gas+=gas
            well.brine+=brine
        else:
            Ohio.objects.create(api_well_number=api_well_number,oil=oil,gas=gas,brine=brine,quater=quater)
        curr_row+=1


class GetWell(APIView):
    def get(self,request):
        well=self.request.GET.get('well')
        quater=self.request.GET.get('quater')
        if Ohio.objects.all().count()==0:
            setData()
        if quater:
            if Ohio.objects.filter(api_well_number=str(well),quater=str(quater)).exists():
                return Response((OhiolSerializer(Ohio.objects.get(api_well_number=str(well),quater=str(quater)),many=False)).data)
            else:
                return Response({'msg':'Data not Found'})
        if Ohio.objects.filter(api_well_number=str(well)).exists():
            res={'oil':0,'gas':0,'brine':0}
            for i in Ohio.objects.filter(api_well_number=str(well)):
                res['oil']+=i.oil
                res['gas']+=i.gas
                res['brine']+=i.brine
            return Response(res)            
        else:
            return Response({'msg':'Data not Found'})
        