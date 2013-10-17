from django.conf.urls import patterns, include, url

from pombola.south_africa.views import LatLonDetailView, SAPlaceDetailSub, \
    SAOrganisationDetailView, SAPersonDetail, SASearchView
from pombola.core.urls import organisation_patterns, person_patterns
from pombola.search.urls import urlpatterns as search_urlpatterns

# Override the organisation url so we can vary it depending on the organisation type.
for index, pattern in enumerate(organisation_patterns):
    if pattern.name == 'organisation':
        organisation_patterns[index] = url(r'^(?P<slug>[-\w]+)/$', SAOrganisationDetailView.as_view(), name='organisation')

# Override the person url so we can add some extra data
for index, pattern in enumerate(person_patterns):
    if pattern.name == 'person':
        person_patterns[index] = url(r'^(?P<slug>[-\w]+)/$', SAPersonDetail.as_view(), name='person')

for index, pattern in enumerate(search_urlpatterns):
    if pattern.name == 'core_search':
        search_urlpatterns[index] = url(r'^$', SASearchView(), name='core_search')

urlpatterns = patterns('pombola.south_africa.views',
    url(r'^place/latlon/(?P<lat>[0-9\.-]+),(?P<lon>[0-9\.-]+)/', LatLonDetailView.as_view(), name='latlon'),
    url(r'^place/(?P<slug>[-\w]+)/places/', SAPlaceDetailSub.as_view(), {'sub_page': 'places'}, name='place_places'),
)
