from django.contrib.auth.decorators import login_required
from django.urls import path

from rcrm_dynamic.views import DynamicTabCreateView, DynamicCreateView,\
    CharfieldCreateView, TextBoxCreateView,\
    ImageCreateView, FileCreateView, DateCreateView,\
    TimeCreateView, DateTimeCreateView

app_name = 'Dynamic'


urlpatterns = [
    # Dynamic Tab
    path('<int:pk>/dynamic/tab/add/', login_required(DynamicTabCreateView.as_view()), name='Dynamic_Tab_Create'),

    # Dynamic
    path('<int:pk>/dynamic/add/', login_required(DynamicCreateView.as_view()), name='Dynamic_Create'),

    # Charfield
    path('<int:pk>/charfield/add/', login_required(CharfieldCreateView.as_view()), name='Dynamic_Charfield_Create'),

    # Text Box
    path('<int:pk>/textbox/add/', login_required(TextBoxCreateView.as_view()), name='Dynamic_Textbox_Create'),

    # Image
    path('<int:pk>/image/add/', login_required(ImageCreateView.as_view()), name='Dynamic_Image_Create'),

    # File
    path('<int:pk>/file/add/', login_required(FileCreateView.as_view()), name='Dynamic_File_Create'),

    # File
    path('<int:pk>/date/add/', login_required(DateCreateView.as_view()), name='Dynamic_Date_Create'),

    # Time
    path('<int:pk>/time/add/', login_required(TimeCreateView.as_view()), name='Dynamic_Time_Create'),

    # Date Time
    path('<int:pk>/datetime/add/', login_required(DateTimeCreateView.as_view()), name='Dynamic_Date_Time_Create'),
]