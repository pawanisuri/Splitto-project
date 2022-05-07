from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls import include

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$',views.home),
    re_path(r'^user/(?P<username>[\w-]+)/$',views.user_detail),
    re_path(r'^account/',include('accounts.urls')),
    re_path(r'^friends/(?P<username>[\w-]+)/$',views.getfriendlist),
    re_path(r'^groups/(?P<username>[\w-]+)/$',views.getallgroups),
    re_path(r'^newgroup/(?P<username>[\w-]+)/$',views.new_group.as_view()),
    re_path(r'^addfriend/(?P<username>[\w-]+)/(?P<friend_user_name>[\w-]+)/$',views.add_friend),
    re_path(r'^payfriend/(?P<username>[\w-]+)/(?P<friendname>[\w-]+)/(?P<amount>[\w-]+)/$',views.pay_friend),
    re_path(r'^uploadimg/(?P<username>[\w-]+)/$',views.upload_img.as_view(),name='upload'),
    re_path(r'^addmember/(?P<username>[\w-]+)/$',views.add_friend_in_group.as_view()),
    re_path(r'^members/(?P<username>[\w-]+)/$',views.get_group_members.as_view()),
    re_path(r'^insight/(?P<username>[\w-]+)/$',views.getTransactions.as_view()),
    re_path(r'^bargraph1/(?P<username>[\w-]+)/$',views.getTransactions.as_view()),
    re_path(r'^bargraph2/(?P<username>[\w-]+)/$',views.bargraph2.as_view()),
    re_path(r'^timeseriesplot/(?P<username>[\w-]+)/$',views.timeSeriesPlot.as_view()),
    re_path(r'^pieChartTags/(?P<username>[\w-]+)/$',views.tagsPieChart.as_view()),
    re_path(r'^friendspiechart/(?P<username>[\w-]+)/$',views.friendsPieChart.as_view()),
    re_path(r'^friendshipchart/(?P<username>[\w-]+)/$',views.friendshipChart.as_view()),
    re_path(r'^frienddetails/(?P<username>[\w-]+)/$',views.get_friend_details.as_view()),
    re_path(r'^settleupall/(?P<username>[\w-]+)/$',views.settle_up_all.as_view()),
    re_path(r'^addtrans/(?P<username>[\w-]+)/$',views.add_transaction.as_view()),
    re_path(r'^balances/(?P<username>[\w-]+)/$',views.balances.as_view()),
    re_path(r'^balances2/(?P<username>[\w-]+)/$',views.balances2.as_view()),
    re_path(r'^leave/(?P<username>[\w-]+)/$',views.leave_group.as_view()),
    re_path(r'^settleup/(?P<username>[\w-]+)/$',views.settle_up.as_view()),
    re_path(r'^grouptrans/(?P<username>[\w-]+)/$',views.get_group_transactions.as_view()),
    re_path(r'^activity/(?P<username>[\w-]+)/$',views.getactivity.as_view()),
    re_path(r'^name/(?P<username>[\w-]+)/$',views.updatename.as_view()),
    re_path(r'^passwd/(?P<username>[\w-]+)/$',views.updatepasswd.as_view()),


]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


