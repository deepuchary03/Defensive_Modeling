"""fakedetector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from defensive_modeling import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^Search_News_DataSets/$', remoteuser.Search_News_DataSets, name="Search_News_DataSets"),
    re_path(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    re_path(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    re_path(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    re_path(r'^Search_News/$', serviceprovider.Search_News, name="Search_News"),
    re_path(r'^View_Positive_News/$', serviceprovider.View_Positive_News, name="View_Positive_News"),
    re_path(r'^Negative_News/$', serviceprovider.Negative_News, name="Negative_News"),
    re_path(r'^Fake_News/$', serviceprovider.Fake_News, name="Fake_News"),
    re_path(r'^View_News_Details/$', serviceprovider.View_News_Details, name="View_News_Details"),
    re_path(r'^View_News_Accuracy/$', serviceprovider.View_News_Accuracy, name="View_News_Accuracy"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
