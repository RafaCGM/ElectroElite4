from django.urls import path
from usuarios.views import *

app_name = 'usuarios'

urlpatterns = [
    path('login/', view_login, name='login'),
    path('login/acess', view_acess_login, name='acess'),
    path('login/logout', view_logout, name= 'logout'),
    path('cadusuario/', view_cadusuario, name='cadastro'),
    path('cadusuario/<int:firstacess>', view_cadusuario, name='cadastro'),
    path('cadusuario/create_usuario/', view_create_usuario, name='createusuario'),
    path('area_usuario', view_area_usuario, name='area_usuario'),

]