from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("category")
    template_name = "index.html"

    def get_context_data(self):
        context = {
            "meals": ["Pizza", "Pasta"],
            "ingredients": ["Flour", "Eggs", "Ham", "Cheese", "Tomatoes"]
        }
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
