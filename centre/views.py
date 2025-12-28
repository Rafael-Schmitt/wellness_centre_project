from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import ContactSubmission
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the main homepage"""
    return render(request, 'centre/index.html')

def about(request):
    """Render about page"""
    return render(request, 'centre/about.html')

def services(request):
    """Render services page"""
    return render(request, 'centre/services.html')

@csrf_exempt
def submit_contact(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            # Handle JSON or form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            # Create and save contact submission
            submission = ContactSubmission(
                name=data.get('name', ''),
                email=data.get('email', ''),
                interest=data.get('interest', 'custom'),
                message=data.get('message', '')
            )
            submission.save()
            
            # Return success response
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you for your message! We will contact you soon.'
                })
            else:
                messages.success(request, 'Thank you for your message! We will contact you soon.')
                return redirect('home')
                
        except Exception as e:
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': False,
                    'message': 'An error occurred. Please try again.'
                }, status=500)
            else:
                messages.error(request, 'An error occurred. Please try again.')
                return redirect('home')
    
    # If not POST request, redirect to home
    return redirect('home')