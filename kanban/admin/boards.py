from adminsortable.admin import SortableAdmin
from django.contrib import admin

from kanban.models import (Label, Board, Column, Comment, Task)


class LabelAdmin(admin.ModelAdmin):
    list_display = ["name", "board"]
    list_filter = ["board"]
    search_fields = ["name"]

    class Meta:
        model = Label


admin.site.register(Label, LabelAdmin)
admin.site.register(Board)
admin.site.register(Column, SortableAdmin)
admin.site.register(Task, SortableAdmin)
