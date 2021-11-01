from django.shortcuts import  render, redirect
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Resume
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("profile")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("profile")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("register")

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if profile:
        return redirect("profile_view")
    else:
        return redirect("create_profile")

def create_profile(request):
    context ={}
 
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        a= Profile.objects.filter(user=request.user)
        for profile in a:
            profile.delete()
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("profile")
    context['form']= form
    return render(request, "create_profile.html", context)

def pdfview(request, filename):
    return FileResponse(open('media/'+ filename, 'rb'), content_type='application/pdf')

def profile_view(request):
    context ={}
    profile = Profile.objects.get(user=request.user)
    if profile:
        context["profile"] = profile
    resume = Resume.objects.filter(user=request.user).order_by('uploaded__minute')
    if resume:
        context["resume"] = str(resume[0].path).split('/')[-1]
    return render(request, "profile_view.html", context)  

def resume(request):
    context ={}
    resumes = Resume.objects.filter(user = request.user).order_by('uploaded__minute')
    res = []
    for resume in resumes:
        ls=(str(resume.path).split('/')[-1],resume.uploaded)
        res.append(ls)
    context["resumes"] = res
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        r = Resume.objects.create(user=request.user, path=uploaded_file_url)
        r.save()
        context["uploaded_file_url"]= uploaded_file_url,
        context["filename"] = filename
        
    return render(request, 'resume.html', context)

def delete_profile(request):
    temp = Profile.objects.get(user=request.user)
    temp.delete()
    return redirect("create_profile")