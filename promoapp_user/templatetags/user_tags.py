from django import template
from .. import models

register = template.Library()

@register.simple_tag
def get_user_type(obj):
    """ Get the type of user """
    if models.StoreManager.objects.filter(user_id=obj.pk):
        user_type = 'Store Manager'
    elif models.PromotionManager.objects.filter(user_id=obj.pk):
        user_type = 'Promotion Manager'
    elif models.Admin.objects.filter(user_id=obj.pk):
        user_type = 'Admin'
    else:
        return 'None'
    return user_type

@register.simple_tag
def get_user(obj, user_type):
    """ Get the type of user """
    if user_type == 'Store Manager':
        return models.StoreManager.objects.filter(user_id=obj.pk)[0]
    elif user_type == 'Promotion Manager':
        return models.PromotionManager.objects.filter(user_id=obj.pk)[0]
    elif user_type == 'Admin':
        return models.Admin.objects.filter(user_id=obj.pk)[0]
    else:
        return None

@register.filter(name='format_date')
def format_date(obj):
    month = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dic'
    }[obj.month]

    return month + '. ' + str(obj.year)