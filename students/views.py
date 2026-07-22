from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            rollno=request.POST['rollno'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            branch=request.POST['branch']
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.rollno = request.POST['rollno']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.branch = request.POST['branch']
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')