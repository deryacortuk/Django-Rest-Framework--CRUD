***Django REST Framework***


Some reasons you might want to use REST framework:

-   The  [Web browsable API](https://restframework.herokuapp.com/)  is a huge usability win for your developers.

-   [Authentication policies](https://www.django-rest-framework.org/api-guide/authentication/)  including packages for  [OAuth1a](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth)  and  [OAuth2](https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit).

-   [Serialization](https://www.django-rest-framework.org/api-guide/serializers/)  that supports both  [ORM](https://www.django-rest-framework.org/api-guide/serializers#modelserializer)  and  [non-ORM](https://www.django-rest-framework.org/api-guide/serializers#serializers)  data sources.

-   Customizable all the way down - just use  [regular function-based views](https://www.django-rest-framework.org/api-guide/views#function-based-views)  if you don't need the  [more](https://www.django-rest-framework.org/api-guide/generic-views/)  [powerful](https://www.django-rest-framework.org/api-guide/viewsets/)  [features](https://www.django-rest-framework.org/api-guide/routers/).

-   Extensive documentation, and  [great community support](https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework).

-   Used and trusted by internationally recognised companies including  [Mozilla](https://www.mozilla.org/en-US/about/),  [Red Hat](https://www.redhat.com/),  [Heroku](https://www.heroku.com/), and  [Eventbrite](https://www.eventbrite.co.uk/about/).

An API allows developers to automate actions on your platform and integrate your service with other applications or online services.

When building an API, there are several ways you can structure its endpoints and actions, but following REST principles is encouraged. The REST architecture comes from Representational State Transfer. RESTful APIs are resource-based; your models represent resources and HTTP methods such as GET, POST, PUT, or DELETE are used to retrieve, create, update, or delete objects. HTTP response codes are also used in this context. Different HTTP response codes are returned to indicate the result of the HTTP request, for example, 2XX response codes for success, 4XX for errors, and so on.

Django REST framework allows you to easily build RESTful APIs for your project.
Install the framework with the following command: 

    pip install djangorestframework

Edit the settings.py file of the your project and add rest_framework to the INSTALLED_APPS setting to activate the application, as follows:

    INSTALLED_APPS = [ # ... 'rest_framework', ]
     

      REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [    
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly']}


***Serializers***

 The framework provides the following classes to build serializers for single objects:
 
  • Serializer: Provides serialization for normal Python class instances 
  
  • ModelSerializer: Provides serialization for model instances 
  
  • HyperlinkedModelSerializer: The same as ModelSerializer, but it represents object relationships with links rather than primary keys. 
 
 ***Parsers and Renderers***
 
 When you get an HTTP request, you have to parse the incoming data and deserialize it before you can operate with it. REST framework includes renderers and parsers to handle that.

     from io import BytesIO
     from rest_framework.parsers import JSONParser
     JSONParser().parse(BytesIO(data))

Given a JSON string input, you can use the JSONParser class provided by REST framework to convert it to a Python object. REST framework also includes Renderer classes that allow you to format API responses. The framework determines which renderer to use through content negotiation by inspecting the request's Accept header to determine the expected content type for the response. Optionally, the renderer is determined by the format suffix of the URL. For example, the URL http://127.0.0.1:8000/api/data.json might be an endpoint that triggers the JSONRenderer in order to return a JSON response.

    from rest_framework.renderers import JSONRenderer 
    JSONRenderer().render(serializer.data)

You use the JSONRenderer to render the serialized data into JSON. By default, REST framework uses two different renderers: 
`JSONRenderer` and `BrowsableAPIRenderer`.

**Django REST Framework Views Series:**

-   ## APIView
`APIView` provides the least amount of abstraction out of the three view classes. There are a total of six policy attributes in APIView,

-   renderer_classes: Used to pass the set of renderer classes that can be used to render the endpoint.

-   parser_classes: Determines which data parsers for different media types are allowed.

-   authentication_classes: To set the authentication schemas we want the view to use.

-   throttle_classes: Determines if a request should be authorized based on the rate of requests

-   permission_classes: Which permission class to use to determine if the user is authorized to access the view.

-   content_negotiation_class: Selects one of the multiple possible representations of the resource to return to a client.

-   ## Generic Views
 It consists of GenericAPIView, Mixins, and Concrete Views:
 1.  `GenericAPIView`  is a more loaded version of  `APIView`. It isn't really useful on its own but can be used to create reusable actions.

2.  Mixins have common behaviors, such as list, create, etc. These are generally not used without  `GenericAPIView`  .

3.  Concrete views combine  `GenericAPIView`, with the appropriate mixins. This is what we mostly deal with if we are using Generic Views. It provides the appropriate level of abstraction, but if you want more flexibility then you can use  `GenericAPIView`  , Mixin classes of your choice.

## Attributes:

1.  `queryset`: This should be used for returning objects from this view. Typically, you must either set this attribute or override the  `get_queryset()`  method. If you are overriding a view method, it is important that you call  `get_queryset()`  instead of accessing this property directly, as  `queryset`  will get evaluated once, and those results will be cached for all subsequent requests.

2.  `serializer_class`: The serializer class that should be used for validating and deserializing input, and for serializing output. Typically, you must either set this attribute or override the  `get_serializer_class()`  method.

3.  `lookup_field`: The model field that should be used for performing object lookup of individual model instances. Defaults to  `'pk'`. Note that when using hyperlinked APIs you'll need to ensure that  _both_  the API views  _and_  the serializer classes set the lookup fields if you need to use a custom value.

## Methods:

`get_queryset(self)`  : This method returns the queryset that will be used for list and detail views. This method should always be used rather than accessing  `self.queryset`  directly, as  `self.queryset`  gets evaluated only once, and those results are cached for all subsequent requests.

-   ## ViewSets
[ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#viewsets) is a type of class-based view.

Instead of method handlers, like `.get()` and `.post()`, it provides actions, like `.list()` and `.create()`.

There are four types of ViewSets, from the most basic to the most powerful:

    1.  ViewSet
    2.  GenericViewSet
    3.  ReadOnlyModelViewSet
    4.  ModelViewSet


Instead of using Django's  [urlpatterns](https://docs.djangoproject.com/en/3.2/topics/http/urls/#syntax-of-the-urlpatterns-variable), ViewSets come with a router 
class that automatically generates the URL configurations.

DRF comes with two routers out-of-the-box:

1.  [SimpleRouter](https://www.django-rest-framework.org/api-guide/routers/#simplerouter)
2.  [DefaultRouter](https://www.django-rest-framework.org/api-guide/routers/#defaultrouter)

While  `ViewSet`  extends  `APIView`,  `GenericViewSet`  extends  `GenericAPIView`.

The  [GenericViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset)  class provides the base set of generic view behavior along 
with the  `get_object`  and  `get_queryset`  methods.

When using mixins, you only need to provide the `serializer_class` and `queryset` attributes; otherwise, you will need to implement the actions yourself.

## Permissions

In DRF,  [permissions](https://www.django-rest-framework.org/api-guide/permissions/), along with
[authentication](https://www.django-rest-framework.org/api-guide/authentication/)  and  [throttling](https://www.django-rest-framework.org/api-guide/throttling/), 
are used to grant or deny access for different classes of users to different parts of an API.

Authentication and authorization work hand in hand. Authentication is always executed before authorization.

While authentication is the process of checking a user's identity (the user the request came from, the token that it was signed with), authorization is 
a process of checking if the request user has the necessary permissions for executing the request (are they a super user, are they the creators of the object).


***Handling Authentication***

REST framework provides authentication classes to identify the user performing the request. If authentication is successful, the framework sets the authenticated 
User object in request.user. If no user is authenticated, an instance of Django's AnonymousUser is set instead. 

REST framework provides the following authentication backends:

• BasicAuthentication: This is HTTP basic authentication. The user and password are sent by the client in the Authorization HTTP header encoded with Base64. 
You can learn more about it at https://en.wikipedia.org/ wiki/Basic_access_authentication.

 • TokenAuthentication: This is token-based authentication. A Token model is used to store user tokens. Users include the token in the Authorization HTTP header 
 for authentication.
 
•SessionAuthentication: This uses Django's session backend for authentication. This backend is useful for performing authenticated AJAX requests to the API 
from your website's frontend. 

• RemoteUserAuthentication: This allows you to delegate authentication to your web server, which sets a REMOTE_USER environment variable. You can build
a custom authentication backend by subclassing the BaseAuthentication class provided by REST framework and overriding the authenticate() method.
