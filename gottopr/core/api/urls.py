from django.urls import path
from core.api.views import (
    # Setting Views
    SettingCreateView, SettingListView, SettingUpdateView, SettingRetrieveView,
    SettingDestroyView, SettingRetrieveUpdateView, SettingRetrieveDestroyView,

    # Job Views
    JobCreateView, JobListView, JobUpdateView, JobRetrieveView,
    JobDestroyView, JobRetrieveUpdateView, JobRetrieveDestroyView,

    # Customer Views
    CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerRetrieveView,
    CustomerDestroyView, CustomerRetrieveUpdateView, CustomerRetrieveDestroyView,

    # Service Views
    ServiceCreateView, ServiceListView, ServiceUpdateView, ServiceRetrieveView,
    ServiceDestroyView, ServiceRetrieveUpdateView, ServiceRetrieveDestroyView,

    # Contact Views
    ContactCreateView, ContactListView, ContactUpdateView, ContactRetrieveView,
    ContactDestroyView, ContactRetrieveUpdateView, ContactRetrieveDestroyView,

    # Recent Jobs Views
    RecentJobsCreateView, RecentJobsListView, RecentJobsUpdateView, RecentJobsRetrieveView,
    RecentJobsDestroyView, RecentJobsRetrieveUpdateView, RecentJobsRetrieveDestroyView,
    )

urlpatterns = [
    # ------- Setting -------
    path('settings/create/', SettingCreateView.as_view()),
    path('settings/', SettingListView.as_view()),
    path('settings/<pk>/update/', SettingUpdateView.as_view()),
    path('settings/<pk>/', SettingRetrieveView.as_view()),
    path('settings/<pk>/delete/', SettingDestroyView.as_view()),
    path('settings/<pk>/edit/', SettingRetrieveUpdateView.as_view()),
    path('settings/<pk>/view-delete/', SettingRetrieveDestroyView.as_view()),

    # ------- Job -------
    path('jobs/create/', JobCreateView.as_view()),
    path('jobs/', JobListView.as_view()),
    path('jobs/<pk>/update/', JobUpdateView.as_view()),
    path('jobs/<pk>/', JobRetrieveView.as_view()),
    path('jobs/<pk>/delete/', JobDestroyView.as_view()),
    path('jobs/<pk>/edit/', JobRetrieveUpdateView.as_view()),
    path('jobs/<pk>/view-delete/', JobRetrieveDestroyView.as_view()),

    # ------- Customer -------
    path('customers/create/', CustomerCreateView.as_view()),
    path('customers/', CustomerListView.as_view()),
    path('customers/<pk>/update/', CustomerUpdateView.as_view()),
    path('customers/<pk>/', CustomerRetrieveView.as_view()),
    path('customers/<pk>/delete/', CustomerDestroyView.as_view()),
    path('customers/<pk>/edit/', CustomerRetrieveUpdateView.as_view()),
    path('customers/<pk>/view-delete/', CustomerRetrieveDestroyView.as_view()),

    # ------- Service -------
    path('services/create/', ServiceCreateView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('services/<pk>/update/', ServiceUpdateView.as_view()),
    path('services-retrieve/', ServiceRetrieveView.as_view()),
    path('services/delete/', ServiceDestroyView.as_view()),
    path('services/edit/', ServiceRetrieveUpdateView.as_view()),
    path('services/view-delete/', ServiceRetrieveDestroyView.as_view()),

    # ------- Contact -------
    path('contacts/create/', ContactCreateView.as_view()),
    path('contacts-list/', ContactListView.as_view()),
    path('contacts/update/', ContactUpdateView.as_view()),
    path('contacts/', ContactRetrieveView.as_view()),
    path('contacts/delete/', ContactDestroyView.as_view()),
    path('contacts/edit/', ContactRetrieveUpdateView.as_view()),
    path('contacts/view-delete/', ContactRetrieveDestroyView.as_view()),

    # ------- Recent Jobs -------
    path('recent-jobs/create/', RecentJobsCreateView.as_view()),
    path('recent-jobs-list/', RecentJobsListView.as_view()),
    path('recent-jobs/update/', RecentJobsUpdateView.as_view()),
    path('recent-jobs/', RecentJobsRetrieveView.as_view()),
    path('recent-jobs/delete/', RecentJobsDestroyView.as_view()),
    path('recent-jobs/edit/', RecentJobsRetrieveUpdateView.as_view()),
    path('recent-jobs/view-delete/', RecentJobsRetrieveDestroyView.as_view()),
]