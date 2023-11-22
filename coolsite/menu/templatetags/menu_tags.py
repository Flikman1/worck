# menu/templatetags/menu_tags.py
# menu/templatetags/menu_tags.py
from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items, 'menu_name': menu_name, 'current_url': current_url}
