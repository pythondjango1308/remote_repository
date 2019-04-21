from django.shortcuts import render
from django.http import HttpResponse
def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("cookie is set in the server")
def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response =HttpResponse("session deleted")
    else:
        response=HttpResponse("session not available")
    return response
def save_session_data(request):
    request.session['eno']=1001
    request.session['ename']='narayana'
    request.session['language']='python'
    request.session['framework']='django'
    return HttpResponse("session data saved")
def access_session_data(request):
    response=" "
    if request.session.get('Eno'):
        response+="Eno:{0}<br>".format(request.session.get('Eno'))
    if request.session.get('Ename'):
        response+="Empname:{0}<br>".format(request.session.get('Ename'))
    if request.session.get('language'):
        response+="language:{0}<br>".format(request.session.get('language'))
    if request.session.get('framework'):
       response+="framework:{0}<br>".format(request.session.get('framework'))
    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)
def delete_session_data(request):
 try:
   del request.session['Eno']
   del request.session['Ename']
   del request.session['language']
   del request.session['framework']
 except KeyError:
     pass
 return HttpResponse("session data is cleared")





