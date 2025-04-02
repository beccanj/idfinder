from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render

# Create your views here.
from datetime import date

from django.contrib import messages
from django.db.models.fields import return_None
from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import LostIDReportForm, RetrievalRequestForm, CitizenForm, RegistrationForm
from main.models import Citizen, LostIDReport, RetrievalRequest


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def get_started(request):
    citizens = Citizen.objects.all()
    return render(request, 'get_started.html', {'citizens': citizens})

def register(request):
    if request.method == "POST":
        form = CitizenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dear {form.cleaned_data['first_name']} , thank you for registering!")
            return redirect('reg_citizens')
    else:
        form = CitizenForm()
    return render(request, 'register.html', {"form": form})

@login_required
def donate(request):
    return render(request, 'donate.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def report(request):
    reports = LostIDReport.objects.all()
    return render(request, 'report.html', {'reports': reports})


#
@login_required
def retrieve(request):
    requests = RetrievalRequest.objects.all()
    return render(request, 'retrieve.html', {'requests': requests})


# def report_a_lost_id(request, id):
#     lostids = LostIDReport.objects.get(pk=id)
#     kenyans = Citizen.objects.all()
#     if request.method == "POST":
#         citizen_id = request.POST['citizen_id']
#         citizen = Citizen.objects.get(pk = citizen_id)
#         date_reported = date.today()
#         reports = LostIDReport.objects.create(citizen=citizen, date_reported=date_reported, status='Lost')
#         reports.save()
#         messages.success(request,
#                          f'The ID of citizen no {id} has successfully been reported as lost ! Thank you for being a patriotic kenyan !')
#         return redirect('get_started')
#     return render(request, 'report_a_lost_id.html', {'kenyans': kenyans, 'lostids': lostids})

# def report_a_lost_id(request, id):
#     # Fetch the citizen using the ID
#     citizen = Citizen.objects.get(id=id)
#     if request.method == 'POST':
#         # Retrieve POST data
#         location = request.POST.get('location')
#         description = request.POST.get('description')
#
#         # Create and save the lost ID report
#         lost_id_report = LostIDReport(
#             citizen=citizen,
#             description=description,
#             location=location,
#             status="pending"  # Set default status
#         )
#
#         # Validate input
#         if not location or not description:
#             return HttpResponse("All fields are required.", status=400)
#         # Create and save the lost ID report
#         lost_id_report = LostIDReport(
#                 citizen=citizen,
#                 description=description,
#                 location=location,
#                 status="pending"  # Set default status
#         )
#
#         lost_id_report.save()
#
#         messages.success(request,
#                          f'The ID has successfully been reported as lost ! Thank you for being a patriotic kenyan !')
#         return redirect('report')
#
#     else:
#
#         # Render the reporting form for the specific citizen
#
#         return render(request, 'report_a_lost_id.html', {'citizen': citizen})
#

@login_required
def reg_citizens(request):
    citizens = Citizen.objects.all()
    return render(request, 'reg_citizens.html', {'citizens': citizens})


# View to report a lost ID
@login_required
#SUBMIT VIEW WORKING WELL INC
# def submit_request(request):
#     citizens = Citizen.objects.all()
#     if request.method == "POST":
#         citizen_id = request.POST.get('citizen')
#         citizen = get_object_or_404(Citizen, id=citizen_id)
#
#         LostIDReport.objects.create(
#             status="Lost"
#         )
#         messages.success(request, f"Lost report submitted for {citizen.first_name} {citizen.last_name}.")
#         return redirect('report')
#
#     return render(request, 'submit_request.html', {'citizens': citizens})
# ------------------------------------------------------------------------------------------------
# ANOTHER ONE CURRENTLY WORKING VERY WELL
# def submit_request(request, citizen_id):
#     citizen = get_object_or_404(Citizen, id=citizen_id)
#     if request.method == "POST":
#         form = LostIDReportForm(request.POST, request.FILES, instance=citizen)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "The ID has been reported as Lost! ")
#             return redirect('report')
#     else:
#         form = LostIDReportForm(instance=citizen)
#     return render(request, 'submit_request.html', {"form": form})
# ----------------------------------------------------------------------------------------------

#THIS ONE DOWN HERE WORKS LIKE A CHARM!! --- UPDATES STATUS OF ID AS LOST OR FOUND
# def submit_request(request, citizen_id):
#     citizen = get_object_or_404(LostIDReport, id=citizen_id)
#     if request.method == "POST":
#         form = LostIDReportForm(request.POST, request.FILES, instance=citizen)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "The ID has been reported as Lost! ")
#             return redirect('report')
#     else:
#         form = LostIDReportForm(instance=citizen)
#     return render(request, 'submit_request.html', {"form": form})
# ------------------------------------------------------------------------------------------------------------------------
# ROUND TAKE 2 ---- ABSOLUTELY WORKS !! USE THIS AND THIS ALONE!! CITIZEN_ID SMH
def submit_request(request):
    if request.method == "POST":
        form = LostIDReportForm(request.POST)
        if form.is_valid():
            # Retrieve the citizen from the form
            citizen = form.cleaned_data['citizen']
            description = form.cleaned_data.get('description')
            location = form.cleaned_data.get('location')

            # Create a new LostIDReport instance
            lost_id_report = LostIDReport.objects.create(
                citizen=citizen,
                description=description,
                location=location,
                # date_reported=date.today(),
                # status="Lost"
            )
            # Save the new report
            lost_id_report.save()

            # Success message
            messages.success(request, f"Lost ID report for {form.cleaned_data['citizen']}  has been successfully submitted.")
            return redirect('report')  # Redirect to reports page or another appropriate page
    else:
        form = LostIDReportForm()

    # Render the form
    return render(request, 'submit_request.html', {'form': form})








@login_required
# def return_id(request, id):
#     retrievals = RetrievalRequest.objects.get(id=id)
#     retrievals.request_date = date.today()
#     retrievals.status = 'Pending'
#     retrievals.save()
#     messages.success(request,
#                      f'Your request for ID Number {retrievals.citizen.national_id} has been submitted successfully!')
#
#     return redirect('report')

#THIS ONE HERE WORKS WELL USE IT INC
# def return_id(request, report_id):
#     returned_borrow = get_object_or_404(LostIDReport, pk=report_id)
#     # returned_borrow.return_date = date.today()
#     returned_borrow.status = 'Pending'
#     returned_borrow.save()
#     messages.success(request,
#                      f'{returned_borrow.citizen.national_id} was requested successfully')
#     return redirect('retrieve')

# --------------------------------------------------------------------------
# TRYING TO COPY THE SUBMIT
# def retrieval_form(request, report_id):
#     report_logs = get_object_or_404(Citizen, id=report_id)
#     if request.method == "POST":
#         form = RetrievalRequestForm(request.POST, request.FILES, instance=report_logs)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Your request for {form.cleaned_data['citizen']} has been submitted successfully! ")
#             return redirect('retrieve')
#     else:
#         form = RetrievalRequestForm(instance=report_logs)
#     return render(request, 'retrieval_form.html', {"form": form})

# ----------------------------------------------------------------------------
# ROUND 2 TAKE 2 OF REQUEST ID
def retrieval_form(request):
    if request.method == "POST":
        form = RetrievalRequestForm(request.POST)
        if form.is_valid():
            # Retrieve user inputs or fallback to defaults
            report = form.cleaned_data['report']
            citizen = form.cleaned_data['citizen']


            # Create a new RetrievalRequest instance
            retrieval_request = RetrievalRequest.objects.create(
                report=report,
                citizen=citizen,
                # status= "Pending"
            )
            retrieval_request.save()

            # Success message
            messages.success(request, f"Retrieval request for {form.cleaned_data['citizen']} has been successfully submitted.")
            return redirect('retrieve')  # Redirect to retrieval requests page or another appropriate page
    else:
        form = RetrievalRequestForm()

    # Render the form
    return render(request, 'retrieval_form.html', {'form': form})

# def return_id(request, report_id):
#     reportss = get_object_or_404(LostIDReport, pk=report_id)
#     citizenss = Citizen.objects.all()
#     if request.method == 'GET':
#         return render(request, 'retrieve.html', {'reportss': reportss, 'citizenss': citizenss})
#     elif request.method == 'POST':
#         citizen_id = request.POST['citizen']
#         citizen = Citizen.objects.get(pk=int(citizen_id))
#         request_date = date.today()
#         retrieval = RetrievalRequest.objects.create(report=report, citizen=citizen, request_date=request_date,status='Lost')
#         retrieval.save()
#         return redirect('retrieve')
#     return render(request, 'retrieve.html', {'reportss': reportss, 'citizenss': citizenss})







def login_page(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'You are now logged in!')
            return redirect('home')
        messages.warning(request,'Invalid username or password.')
        return redirect('login')

# -----------------------sign up----------------------------------------
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user from the form data
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            # Log the user in after registration
            login(request, user)

            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')  # Redirect to home or any other page you choose
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})
# ======================================signup-------------
@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required
def lost_book(request, id):

    transactions = RetrievalRequest.objects.get(pk=id)
    transactions.status = 'Pending'
    transactions.save()
    messages.info(request, f'Your request for ID No {transactions.citizen.national_id} has been submitted successfully!')
    return redirect('retrieve')



