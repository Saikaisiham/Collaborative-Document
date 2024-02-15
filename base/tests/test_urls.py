from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import base, document_detail

class TestUrls(SimpleTestCase):

    def test_base_url_is_resolved(self):
        url = reverse('base')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, base)


    def test_doc_url_is_resolved(self):
        doc_id = 1
        url = reverse('doc', args=[doc_id])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, document_detail)

