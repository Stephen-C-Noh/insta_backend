from django import template
import re

# register is a module-level instance object to make valid tag library
register = template.Library()

@register.filter
def add_link(value):
    content = value.content #get 'content' member variable from the value object called with the add link
    tags = value.tag_set.all() # return a queryset that take tag_set from value object. model.py > tag_set(holding value object) > queryset 
    
    for tag in tags:
        content = re.sub('r\#'+tag.name+r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content) # re.sub(pattern, repl, string)
        # in string, find pattern, and replace them to repl.
        return content