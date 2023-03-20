from rest_framework.generics import *

from .serializers import *


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserGetView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "tg_id"


class SectorListView(ListAPIView):
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()


class RowListView(ListAPIView):
    serializer_class = RowSerializer

    def get_queryset(self):
        option = self.request.query_params.get('option')
        return Row.objects.filter(sector_id=option)


class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        option = self.request.query_params.get('option')
        return Place.objects.filter(row_id=option)


class PlaceGetView(RetrieveAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    lookup_field = "id"


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderGetView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        tg_id = self.request.query_params.get("tg_id")
        try:
            user = User.objects.get(tg_id=tg_id)
        except:
            return []
        return Order.objects.filter(user=user)


class CallsGetView(ListAPIView):
    serializer_class = CallsSerializer
    queryset = Calls.objects.all()


class AboutUsGetView(ListAPIView):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()
