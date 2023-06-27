from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .permissions import IsAdminReadOnly
from .serializers import UserSerializer


class UserViewSetList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()[:1]

    @action(methods=['get'], detail=False)
    def category(self, pk, request):
        userList = User.objects.get(pk=pk)
        return Response({'list': userList.username})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminReadOnly,)


class UserAPIUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminReadOnly,)


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminReadOnly,)
    lookup_field = 'username'

# class UserAPIView(APIView):
#     def get(self, request):
#         list = User.objects.all()
#         return Response({'list': UserSerializer(list, many=True).data})
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'list': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({"error": "Object does not exist"})
#
#         serializer = UserSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"list": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         instance = get_object_or_404(User, pk=pk)
#         instance.delete()
#         return Response({"message": "User deleted successfully"})
