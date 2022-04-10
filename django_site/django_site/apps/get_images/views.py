from django.views.generic import CreateView

from .forms import PagesToScanForm
from .models import PagesToScan
from .tasks import get_images_from_links


# Create your views here.
class GetImages(CreateView):
    model = PagesToScan
    form_class = PagesToScanForm
    success_url = '/'
    template_name = 'get_images/get_images.html'

    def form_valid(self, form):
        form.save()
        get_images_from_links.delay(form.instance.url)

        return super().form_valid(form)
