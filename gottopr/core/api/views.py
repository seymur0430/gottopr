from rest_framework.generics import (
    CreateAPIView,ListAPIView,UpdateAPIView,
    RetrieveAPIView,DestroyAPIView,ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveDestroyAPIView,
                                     
)


from django.contrib.auth.models import User
from core.api.serializers import SettingSerializer,JobSerializer,CustomerSerializer,ServiceSerializer,ContactSerializer,Recent_jobsSerializer
from core.models import Setting,Job,Customer,Service,Recent_jobs,Contact

#Setting Views
class SettingCreateView(CreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingListView(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingUpdateView(UpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingRetrieveView(RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingDestroyView(DestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

# Job Views
class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDestroyView(DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



# Customer Views
class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDestroyView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Service Views
class ServiceCreateView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDestroyView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Contact Views
class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDestroyView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Recent Jobs Views
class RecentJobsCreateView(CreateAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsListView(ListAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsUpdateView(UpdateAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsRetrieveView(RetrieveAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsDestroyView(DestroyAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer

class RecentJobsRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Recent_jobs.objects.all()
    serializer_class = Recent_jobsSerializer


class CategoryJobListAPIView(ListAPIView):
    def get_queryset(self):
        category_id=self.kwargs.get('id')
        category=Job.objects.get(id=category_id)
        return Job.objects.filter(
            category=category
        )
    
    serializer_class=JobSerializer
