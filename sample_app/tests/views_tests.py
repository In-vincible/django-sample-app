import mock

from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase as DjangoTestCase

class DiaryRedirectViewTestCase(DjangoTestCase):
    def test_redirects_when_diary_empty(self):
        response = self.client.get(reverse('diary'))
        self.assert_(response.status_code == 302)
        response = self.client.get(reverse('diary'), follow=True)
        self.assert_(response.content == render_to_string("home.html"))

class DiaryRedirectViewTestCase2(DjangoTestCase):
    def test_redirect_to_url_name_is_none(self):
        with mock.patch.object('sample_app.views', 
                               'REDIRECT_TO_URL_NAME',
                               None):
            response = self.client.get(reverse('diary'), follow=True)
            self.assert_(response.content == render_to_string("index.html"))
