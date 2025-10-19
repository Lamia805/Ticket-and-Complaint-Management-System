from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Complaint, Comment
from .forms import ComplaintForm, CommentForm, ComplaintSatisfactionForm

# Helper function to check if a user belongs to a specific group
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

# Decorator to protect views based on group membership
def group_required(group_name):
    return user_passes_test(lambda u: is_in_group(u, group_name))

@login_required
def view_complaints(request):
    """Displays a full list of the user's complaints."""
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'view_complaints.html', {'complaints': complaints})

@login_required
def complaint_detail(request, complaint_id):
    """Displays a single complaint and handles comment submission."""
    # This logic allows a user to see their own complaints, 
    # but also allows staff to see any complaint.
    if request.user.is_staff:
        complaint = get_object_or_404(Complaint, id=complaint_id)
    else:
        complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.complaint = complaint
            new_comment.user = request.user
            new_comment.save()
            return redirect('complaint_detail', complaint_id=complaint.id)
    else:
        comment_form = CommentForm()
    
    context = {
        'complaint': complaint,
        'comment_form': comment_form,
    }
    return render(request, 'complaint_detail.html', context)

@login_required
def create_complaint(request):
    """Handles the creation of a new complaint."""
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('view_complaints')
    else:
        form = ComplaintForm()
    return render(request, 'create_complaint.html', {'form': form})

@login_required
def update_complaint(request, complaint_id):
    """Handles updating an existing complaint."""
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_detail', complaint_id=complaint.id)
    else:
        form = ComplaintForm(instance=complaint)
    return render(request, 'update_complaint.html', {'form': form})

@login_required
def delete_complaint(request, complaint_id):
    """Handles the deletion of a complaint after confirmation."""
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    if request.method == 'POST':
        complaint.delete()
        return redirect('view_complaints')
    return render(request, 'complaint_confirm_delete.html', {'complaint': complaint})

@login_required
def update_complaint_satisfaction(request, complaint_id):
    """Handles the user's satisfaction feedback for a solved complaint."""
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    if request.method == 'POST':
        form = ComplaintSatisfactionForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_detail', complaint_id=complaint.id)
    else:
        form = ComplaintSatisfactionForm(instance=complaint)
    return render(request, 'update_complaint_satisfaction.html', {'form': form, 'complaint': complaint})

# New view for the Manager Dashboard, protected by our role decorator
@login_required
@group_required('Helpdesk Manager')
def manager_dashboard(request):
    """
    A special dashboard for managers to get an overview of the system.
    """
    unassigned_complaints = Complaint.objects.filter(assigned_to__isnull=True).order_by('-created_at')
    context = {
        'unassigned_complaints': unassigned_complaints,
    }
    return render(request, 'manager_dashboard.html', context)

