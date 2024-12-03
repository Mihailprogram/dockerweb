from django.shortcuts import render, redirect
from .bot import chats
# Create your views here.
text = ''
def index(request):
    global text
    if request.method == 'POST':
        text = chats(request.POST.get('text'))
        
        request.session['bot_response'] = text
        return redirect('viewapp:bot')
    response = request.session.get('bot_response', '')

    context = {
        'text': response
    }
    return render(request, 'index.html', context=context)
