from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_api.views import agendamentoviewset, hello_word

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=True)
router.register('agendamento',agendamentoviewset)
urlpatterns = [
    path('hello_word',hello_word,name='hello_word_api'),
]

urlpatterns += router.urls

