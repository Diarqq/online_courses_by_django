from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("course_list")

    else:
        form = CustomUserCreationForm
        return render(request, "registration/register.html", {"form": form})


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                username=username, password=password
            )  # Проверяем учетные данные
            if user is not None:
                login(request, user)  # Выполняем вход
                return redirect("course_list")  # Перенаправляем на главную страницу
    return render(request, "login.html", {"form": form})


"""class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        role = form.cleaned_data.get('role')

        if role == 'student':
            group, created = Group.objects.get_or_create(name='Students')
        elif role == 'instructor':
            group, created = Group.objects.get_or_create(name='Instructors')
        else:
            group = None

        if group:
            user.groups.add(group)

        messages.success(self.request, 'Ypu registered successfully!')
        return super().form_valid(form)"""
