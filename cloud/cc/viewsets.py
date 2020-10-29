# from rest_framework import viewsets
# from .import models
# from .import serializers
# from django.http import HttpResponse,HttpResponseRedirect

# class ProfileViewset(viewsets.ModelViewSet):
#     queryset = models.ProfileEvaluation.objects.all()
#     serializer_class = serializers.Profile

# def profileupdate(request):
#     p = models.ProfileEvaluation.objects.get(id = 1)
#     serializer = serializers.Profile(instance=p, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     #return Response(serializer.data)
