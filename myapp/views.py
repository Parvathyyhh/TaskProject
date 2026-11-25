from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class BMIView(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("height")
        w=data.get("weight")

        # Convert height from cm to m
        height=h/100

        #Calculate bmi
        bmi=w/(height**2)

        result={
            "Height":data.get("height"),
            "Weight":w,
            "BMI":round(bmi,2)
        }
        return JsonResponse(result)
@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data=json.loads(request.body)
        birth_year=data.get("birth_year")
        current_year=data.get("current_year")
        age=current_year-birth_year
        result={
            "Age":age
        }
        return JsonResponse(result)
@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        data=json.loads(request.body)
        obtained_mark=data.get("obtained_marks")
        total_mark=data.get("total_marks")
        percentage=obtained_mark/total_mark*100
        result={
            "Percentage":percentage
        }
        return JsonResponse(result)

#Simple Interest Calculator
@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        data=json.loads(request.body)
        principal=data.get("principal")
        rate=data.get("rate")
        time=data.get("time")
        simple_interest=(principal*rate*time)/100
        result={
            "Principal":principal,
            "Rate":rate,
            "Time":time,
            "Simple Interest":simple_interest
        }
        return JsonResponse(result)

# Electricity Bill Calculator
@method_decorator(csrf_exempt,name='dispatch')
class ElectricityBillView(View):
    def post(self,request):
        data=json.loads(request.body)
        units=data.get("units")
        rate=data.get("rate")
        bill=units*rate
        result={
            "Bill":bill
        }
        return JsonResponse(result)

#Discount Calculator
@method_decorator(csrf_exempt,name='dispatch')
class DiscountView(View):
    def post(self,request):
        data=json.loads(request.body)
        price=data.get("price")
        discount_percentage=data.get("discount_percentage")
        discount_amount = price * discount_percentage / 100
        final_price = price - discount_amount     
        result={
            "Price":price,
            "Discount_percentage":discount_percentage,
            "Discount_Amount":discount_amount,
            "Final_Price":final_price
        }
        return JsonResponse(result)

#  Profit Calculator
@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        cost_price=data.get("cost_price")
        selling_price=data.get("selling_price")
        profit=selling_price-cost_price
        result={
            "Cost_price":cost_price,
            "Selling_price":selling_price,
            "Profit":profit
        }
        return JsonResponse(result)

# Salary Calculator 
@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        data=json.loads(request.body)
        basic_salary=data.get("basic_salary")
        bonus=data.get("bonus")
        deduction=data.get("deduction")
        Net_Salary = basic_salary + bonus - deduction 
        result={
            "Basic_salary":basic_salary,
            "Bonus":bonus,
            "Deduction":deduction,
            "Net_salary":Net_Salary
        }
        return JsonResponse(result)
    
# Time Converter 
@method_decorator(csrf_exempt,name='dispatch')
class TimeView(View):
    def post(self,request):
        data=json.loads(request.body)
        hours=data.get("hours")
        minutes=hours*60
        seconds=hours*3600
        result={
            "Hours":hours,
            "Minutes":minutes,
            "Seconds":seconds
        }
        return JsonResponse(result)

#Fuel Cost Calculator 
@method_decorator(csrf_exempt,name='dispatch')
class FuelCostView(View):
    def post(self,request):
        data=json.loads(request.body)
        distance=data.get("distance")
        mileage=data.get("mileage")
        fuel_price=data.get("fuel_price")
        fuel_required = distance / mileage 
        Total_Cost = fuel_required * fuel_price   
        result={
            "Distance": distance, 
            "Mileage": mileage, 
            "Fuel_price": fuel_price, 
            "Fuel_required": fuel_required, 
            "Total_cost": Total_Cost
        }
        return JsonResponse(result)

# Product Profit Calculator 
@method_decorator(csrf_exempt,name='dispatch')
class ProductProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        cost_price= data.get("cost_price")
        selling_price= data.get("selling_price") 
        quantity = data.get("quantity")
        total_cost = cost_price * quantity 
        total_sales = selling_price * quantity 
        profit = total_sales - total_cost
        result={
            "cost_price": cost_price, 
            "selling_price": selling_price, 
            "quantity": quantity, 
            "total_cost": total_cost, 
            "total_sales": total_sales, 
            "profit": profit
        }
        return JsonResponse(result)

#Work Salary Calculator 
@method_decorator(csrf_exempt,name='dispatch')
class WorkSalaryView(View):
    def post(self,request):
        data=json.loads(request.body)
        hours_worked=data.get("hours_worked")
        regular_hours=data.get("regular_hours")
        hourly_rate=data.get("hourly_rate")
        overtime_rate=data.get("overtime_rate")
        regular_pay = regular_hours * hourly_rate 
        overtime_hours = hours_worked - regular_hours 
        overtime_pay = overtime_hours * overtime_rate 
        total_salary = regular_pay + overtime_pay   
        result={
            "Hours_worked":hours_worked,
            "Regular_hours":regular_hours,
            "Hourly_rate":hourly_rate,
            "Overtime_rate":overtime_rate,
            "Regular_pay":regular_pay,
            "Overtime_hours":overtime_hours,
            "Overtime_pay":overtime_pay,
            "Total_salary":total_salary
        }      
        return JsonResponse(result)

#Age in Days Calculator
@method_decorator(csrf_exempt,name='dispatch')
class AgeDetailsView(View):
    def post(self,request):
        data=json.loads(request.body)
        age=data.get("age")
        months=age*12
        weeks=age*52
        days=age*365
        result={
            "Age":age,
            "Months":months,
            "Weeks":weeks,
            "Days":days
        }
        return JsonResponse(result)