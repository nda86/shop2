import logging

from django.views import generic
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shop2.settings import PAGINATE_PER_PAGE
from .models import Item, Cart
from .serializers import CartSerializer


# получаем объект логгера
log = logging.getLogger('main_debug_log')


class HomeView(generic.TemplateView):
	"""вьюха для главной страницы сайта"""
	template_name = "main/index.html"


class ItemsList(generic.ListView):
	"""вьюха для страницы со списком товара"""
	context_object_name = "items"
	template_name = "main/items_list.html"
	paginate_by = PAGINATE_PER_PAGE
	queryset = Item.objects.all()


@api_view(["GET"])
def cart_api_list(request):
	qs = Cart.objects.all()
	serializer = CartSerializer(qs, many=True)
	return Response(serializer.data)
