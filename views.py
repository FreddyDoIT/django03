from django.http import HttpResponse

def index(request):
    html = '''
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>��̳��ҳ</title>
        </head>
        <body>
            <h2>Python������̳</h2>
            <div>��άר��</div>
            <div>Djangoר��</div>
            <div>���佨��</div>
        </body>
    </html>
    '''
    return HttpResponse(html)

