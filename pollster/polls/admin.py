from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Administrador da enquete"
admin.site.site_title = "Area de administração da enquete"
admin.site.index_title = "Bem vindo à àrea de administração da enquete"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': [
                  'pub_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
