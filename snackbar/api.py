from tastypie.resources import Resource

class Ingredient():
    def __init__(self, name, value):
        self.name = name
        self.value = value



class snackbarResource(Resource):
    class Meta:
        allowed_methods = ['get','post','put','patch','delete']
        object_class = Ingredient
        resource_name = 'snackbar/api'


    def prepend_urls(self):
        return [
            path('teste/', self.wrap_view('api_teste'), name='api_teste'),
        ]
    
    def api_teste(self, request, **kwargs):
        return self.create_response(request, {'status': True})
   



