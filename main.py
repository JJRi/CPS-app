import kivy
from kivy.clock import Clock
from kivy.app import App
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.properties import ObjectProperty


# Sivupalkki / Navigaatio
class Drawer(NavigationDrawer):

# yhdistää numerot KV:sta
    breath = ObjectProperty(None)

# päämetodi, yhdistetty aloitusnappiin
    def hengitys(self):
        global counter
        counter = 1
# ajastettu metodi
        self.rauhoitu = Clock.schedule_interval(self.show_numbers, 1)


#lopetusnapin metodi, pysäyttää harjoituksen
    def hengitys_seis(self):
        self.rauhoitu.cancel()

#Ajastimen numeroiden ja ohjeistuksen vaihdon metodi
    def show_numbers(self, *args):
        global counter
        self.breath.text = str(int(self.breath.text) + 1)
        counter += 1
        if self.breath.text == '6':
            self.breath.text = '1'

        #Ohjeistavan tekstin vaihtaminen
        #pyörii yllä olevan iteroijan kautta
        #TODO: kun teet asetukset lehden, näihin pitää tehdä muuttujat jotta niitä voi itse määritellä
        if counter <= 5:
            self.suunta.text = 'Hengitä sisään.'
        if counter >= 6:
            self.suunta.text = 'Hengitä ulos.'
        #Ohjeistustekstin nollaus
        if counter == 10:
            counter = counter - 10



#Ohjelman pääluokat
#Varsinainen laukaisu on alla
class MainMenuApp(App):
    #Sovellutuksen pääluokka

    def show_drawer(self):
        #Navigaatiopalkin laukaisija
        d = Drawer()
        d.toggle_state()

    def build(self):
        return Drawer()

if __name__ == "__main__":
    MainMenuApp().run()