from django_site.celery import app

from .getimages import ImagesFromLinks


@app.task
def get_images_from_links(url):
    links = ImagesFromLinks(url)
    links.save_images_from_link()
