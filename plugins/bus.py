#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time, datetime
from BeautifulSoup import BeautifulSoup as BS
import urllib2
from dot3k.menu import MenuOption


class Kvadraturen(MenuOption):      # Replace the method name here with e.g. the direction the bus is heading
    """
    A Python script that scrapes AKT's real time bus departure list to get bus departure times (The next two buses)
    Could be rewritten to work with any bus company.
    """

    def redraw(self, menu):
        """
        Find your bus-stops ID by going to: http://rp.akt.no/scripts/TravelMagic/TravelMagicWE.dll/?lang=en&dep1=1&now=1
        Find your stop by clicking a stop-icon on the map, and click the stops' name (e.g. Kjevik Lufthavn Pl C(Kristiansand)
        Copy the URL that appears in your browser, and replace "url" below with that URL
        """

        # Stop Osterveien, towards Kvadraturen, ID 10012851

        url = "http://rp.akt.no/scripts/TravelMagic/TravelMagicWE.dll/avgangsinfo?lang=en&theme=&now=1&from=10012851"
        usock = urllib2.urlopen(url)
        data = usock.read()
        usock.close()
        source = BS(data)
        # Bus 1 value
        bus1 = ""
        # Bus 1 Query Value
        bQ1 = ""
        # Bus 1 Time Value
        time1 = ""
        # Bus 1 Time Query Value
        tQ1 = ""

        # Bus 2 value
        bus2 = ""
        # Bus 2 Query Value
        bQ2 = ""
        # Bus 2 Time Value
        time2 = ""
        # Bus 2 Time Query Value
        tQ2 = ""

        stop = "Til Byen"    # Replace this with where the bus is heading, e.g. "Til Kvadraturen"

        for b in source.findAll('span', {'class': ['tm-block-float tm-departurelist-colwrapper']}):
            if (bus1 != "") and (bQ2 == ""):
                bus2 = bQ1
                time2 = tQ1
            bQ1 = b.find('strong', {'class': 'tm-departurelist-linename'}).text
            bus1 = bQ1

            tQ1 = b.find('span', {'class': 'tm-block-float tm-departurelist-time'}).text
            time1 = tQ1

            # print "bus1 " + bus1 + " time1 " + time1 + "\n" + "bus2 " + bus2 + " time2 " + time2
            if (bus1 != "") and (bus2 != ""):
                break
        # print "Osterveien->byen\n" + bus1 + "        " + time1 + "\n" + bus2 + "        " + time2
        menu.write_row(0, stop)
        menu.write_row(1, bus2 + "        " + time2)
        menu.write_row(2, bus1 + "        " + time1)


class UiA(MenuOption):      # Replace the method name here with e.g. the direction the bus is heading, e.g. "class Kjevik(MenuOption):"
    """
    A Python script that scrapes AKT's real time bus departure list to get bus departure times (The next two buses)
    Could be rewritten to work with any bus company.
    """

    def redraw(self, menu):
        """
        Find your bus-stops ID by going to: http://rp.akt.no/scripts/TravelMagic/TravelMagicWE.dll/?lang=en&dep1=1&now=1
        Find your stop by clicking a stop-icon on the map, and click the stops' name (e.g. Kjevik Lufthavn Pl C(Kristiansand)
        Copy the URL that appears in your browser, and replace "url" below with that URL
        """

        # Stop Osterveien, towards UiA, ID 10012840
        url = "http://rp.akt.no/scripts/TravelMagic/TravelMagicWE.dll/avgangsinfo?lang=en&theme=&now=1&from=10012840"
        usock = urllib2.urlopen(url)
        data = usock.read()
        usock.close()
        source = BS(data)
        # Bus 1 value
        bus1 = ""
        # Bus 1 Query Value
        bQ1 = ""
        # Bus 1 Time Value
        time1 = ""
        # Bus 1 Time Query Value
        tQ1 = ""

        # Bus 2 value
        bus2 = ""
        # Bus 2 Query Value
        bQ2 = ""
        # Bus 2 Time Value
        time2 = ""
        # Bus 2 Time Query Value
        tQ2 = ""

        stop = "Til UiA"    # Replace this with where the bus is heading, e.g. "Til Kvadraturen"

        for b in source.findAll('span', {'class': ['tm-block-float tm-departurelist-colwrapper']}):
            if (bus1 != "") and (bQ2 == ""):
                bus2 = bQ1
                time2 = tQ1
            bQ1 = b.find('strong', {'class': 'tm-departurelist-linename'}).text
            bus1 = bQ1

            tQ1 = b.find('span', {'class': 'tm-block-float tm-departurelist-time'}).text
            time1 = tQ1

            # print "bus1 " + bus1 + " time1 " + time1 + "\n" + "bus2 " + bus2 + " time2 " + time2
            if (bus1 != "") and (bus2 != ""):
                break
        # print "Til UiA\n" + bus1 + "        " + time1 + "\n" + bus2 + "        " + time2
        menu.write_row(0, stop)
        menu.write_row(1, bus2 + "        " + time2)
        menu.write_row(2, bus1 + "        " + time1)