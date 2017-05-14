from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from .models import Alert, Station
from django.core.urlresolvers import reverse


class RssLatestEntriesFeed(Feed):
    link = "/alerts/"
    description = "Updates on air quality alerts"

    def title(self, object):
        return '%s %s | Latest Alerts' % (object.name, object.id)

    def get_object(self, request, station_id):
        return Station.objects.get(pk=station_id)

    def items(self, obj):
        return Alert.objects.filter(station=obj).order_by('-report__date')[:5]

    def item_title(self, alert):
        return '%s: %d µg/m³ the %s' % (alert.report.get_kind_display(), alert.value, alert.report.date)

    def item_description(self, item):
        return 'station: %s' % item.station

    def item_link(self, item):
        return reverse('station', args=[item.station.id])


class AtomLatestEntriesFeed(RssLatestEntriesFeed):
    feed_type = Atom1Feed
    subtitle = RssLatestEntriesFeed.description
