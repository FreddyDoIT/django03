from django.http import HttpResponse

def index(request):
    html = '''
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>论坛首页</title>
        </head>
        <body>
            <h2>Python部落论坛</h2>
            <div>运维专区</div>
            <div>Django专区</div>
            <div>部落建设</div>
        </body>
    </html>
    '''
    return HttpResponse(html)

