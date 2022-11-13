#Execution process for a single middleware classes
class ExicutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        print('This line added at pre-processing request')
        response=self.get_response(request)
        print('This line added at post-processing of request')
        return response

# middleware application to show information saying application under maintenance

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        return HttpResponse('<h1> Currently Application Under Maintenance .....please try after 2 days !!!!</h1>')


# middleware application to show response if view function raises any error
# Configuration of how to raise the display exception information to end user


class ErrorMassageMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        response=self.get_response(request)
        return response

    def process_exception(self, request, exception):
        s1='<h1>Currently we are facing some technical problems ..... please try after some time !!!!</h1><hr><hr>'
        s2='<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        s3='<h2>Exception Description/Message:{}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)

# Configuration of multiple middleware classes.......

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        print('This line printed by first middleware at pre-processing request')
        response=self.get_response(request)
        print('This line printed by first middleware at post-processing of request')
        return response


class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        print('This line printed by Second middleware at pre-processing request')
        response=self.get_response(request)
        print('This line printed by Second middleware at post-processing of request')
        return response


class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        print('This line printed by Third middleware at pre-processing request')
        response=self.get_response(request)
        print('This line printed by Third  middleware at post-processing of request')
        return response