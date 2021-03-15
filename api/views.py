from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from api.serializers import Api1Serializer, Api2Serializer
from rest_framework.decorators import api_view
from rest_framework import status
from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]
import logging


logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("Test your post api using postman")

def validate_finite_values_entity_util(request):
    if request.method == 'POST':
            api_data = JSONParser().parse(request)
            api_serializer = Api1Serializer(data=api_data)
            if api_serializer.is_valid():
                data = api_data
                result = validate_finite_values_entity(data['values'],data['supported_values'],data['invalid_trigger'],data['key'],data['support_multiple']
                ,data['pick_first'],type=data['type'][0])
                response_dict = {}
                response_dict['filled'] = result[0]
                response_dict['partially_filled'] = result[1]
                response_dict['trigger'] = result[2]
                response_dict['parameters'] = result[3]
                return JsonResponse(response_dict, status=status.HTTP_201_CREATED) 
            return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def validate_numeric_entity_util(request):
    if request.method == 'POST':
            api_data = JSONParser().parse(request)
            api_serializer = Api2Serializer(data=api_data)
            if api_serializer.is_valid():
                data = api_data
                result = validate_numeric_entity(data['values'],data['invalid_trigger'],data['key']
                ,data['pick_first'],data['constraint'],data['var_name'],type=data['type'][0])
                response_dict = {}
                response_dict['filled'] = result[0]
                response_dict['partially_filled'] = result[1]
                response_dict['trigger'] = result[2]
                response_dict['parameters'] = result[3]
                return JsonResponse(response_dict, status=status.HTTP_201_CREATED) 
            return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
                                if not(pick_first) :
                                    pick_first = not(support_multiple)
                                filled = True
                                ids = []
                                ids_stated_dict = {}
                                if len(values) == 0:
                                    return (False,False,invalid_trigger,ids_stated_dict)
                                for i in range(len(values)):
                                    try:
                                        print(values[i]['value'])
                                        index = supported_values.index(values[i]['value'])
                                        if (not(pick_first)) or (pick_first and i==0) :
                                            ids.append(values[i]['value'].upper())
                                    except ValueError:
                                        filled = False
                                if not(filled):
                                    return (filled,not(filled),invalid_trigger,ids_stated_dict)
                                ids_stated_dict[key] = ids
                                return (filled,not(filled),"",ids_stated_dict)

def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:
                                filled = True
                                ids = []
                                ids_stated_dict = {}
                                if len(values) == 0:
                                    return (False,False,invalid_trigger,ids_stated_dict)
                                for i in range(len(values)):
                                    try:
                                        evalstring = var_name + "=" + str(values[i]['value'])
                                        exec(evalstring)
                                        constraint_ans = eval(constraint)
                                    except ValueError:
                                        return (filled,not(filled),"Caught NameError",ids_stated_dict)
                                    if not(constraint_ans) :
                                        filled = False
                                        break
                                    if (not(pick_first)) or (pick_first and i==0) :
                                        ids.append(values[i]['value'])
                                if not(filled):
                                    return (filled,not(filled),invalid_trigger,ids_stated_dict)
                                ids_stated_dict[key] = ids
                                return (filled,not(filled),"",ids_stated_dict)
