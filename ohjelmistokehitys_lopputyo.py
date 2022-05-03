import pygame
import time
import random

pygame.init()
pygame.display.set_caption('Ohjelmistokehitys lopputyo')

musta = (0, 0, 0)
keltainen = (255, 255, 0)
punainen = (255, 0, 0)
sininen = (0, 255, 255)

naytonLeveys = 1000
naytonKorkeus = 800

naytto = pygame.display.set_mode((naytonLeveys, naytonKorkeus))

aika = pygame.time.Clock()

koko = 10

fontti = pygame.font.SysFont(None, 100)

pelinHaviaja = str


def punainenMato(koko, punainenSijanti):
    for x in punainenSijanti:
        pygame.draw.rect(naytto, punainen, [x[0], x[1], koko, koko])


def keltainenMato(koko, keltainenSijanti):
    for y in keltainenSijanti:
        pygame.draw.rect(naytto, keltainen, [y[0], y[1], koko, koko])


def viesti(v, vari):
    loppuViesti = fontti.render(v, True, vari)
    naytto.blit(loppuViesti, [100, 400])


def uusiPeli():
    peliOhi = False
    sammutaPeli = False

    leveysPunainen = 100
    korkeusPunainen = 100

    leveysMuutosPunainen = 0
    korkeusMuutosPunainen = 0

    leveysKeltainen = 100
    korkeusKeltainen = 700

    leveysMuutosKeltainen = 0
    korkeusMuutosKeltainen = 0

    punainenSijainti = []
    punainenPituus = 1

    keltainenSijainti = []
    keltainenPituus = 1

    ruokaLeveys = round(random.randrange(
        0, naytonLeveys - koko) / 10.0) * 10.0
    ruokaKorkeus = round(random.randrange(
        0, naytonKorkeus - koko) / 10.0) * 10.0

    while not peliOhi:

        while sammutaPeli == True:
            naytto.fill(musta)
            viesti("Hävisit pelin", pelinHaviaja)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        peliOhi = True
                        sammutaPeli = False
                    if event.key == pygame.K_SPACE:
                        uusiPeli()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                peliOhi = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leveysMuutosPunainen = -koko
                    korkeusMuutosPunainen = 0
                elif event.key == pygame.K_RIGHT:
                    leveysMuutosPunainen = koko
                    korkeusMuutosPunainen = 0
                elif event.key == pygame.K_UP:
                    korkeusMuutosPunainen = -koko
                    leveysMuutosPunainen = 0
                elif event.key == pygame.K_DOWN:
                    korkeusMuutosPunainen = koko
                    leveysMuutosPunainen = 0

                elif event.key == pygame.K_a:
                    leveysMuutosKeltainen = -koko
                    korkeusMuutosKeltainen = 0
                elif event.key == pygame.K_d:
                    leveysMuutosKeltainen = koko
                    korkeusMuutosKeltainen = 0
                elif event.key == pygame.K_w:
                    leveysMuutosKeltainen = 0
                    korkeusMuutosKeltainen = -koko
                elif event.key == pygame.K_s:
                    leveysMuutosKeltainen = 0
                    korkeusMuutosKeltainen = koko

        if leveysPunainen >= naytonLeveys or leveysPunainen < 0 or korkeusPunainen >= naytonKorkeus or korkeusPunainen < 0:
            sammutaPeli = True
            pelinHaviaja = punainen

        leveysPunainen += leveysMuutosPunainen
        korkeusPunainen += korkeusMuutosPunainen

        if leveysKeltainen >= naytonLeveys or leveysKeltainen < 0 or korkeusKeltainen >= naytonKorkeus or korkeusKeltainen < 0:
            sammutaPeli = True
            pelinHaviaja = keltainen

        leveysKeltainen += leveysMuutosKeltainen
        korkeusKeltainen += korkeusMuutosKeltainen

        naytto.fill(musta)
        pygame.draw.rect(
            naytto, sininen, [ruokaLeveys, ruokaKorkeus, koko, koko])

        punainenPaa = []
        punainenPaa.append(leveysPunainen)
        punainenPaa.append(korkeusPunainen)
        punainenSijainti.append(punainenPaa)
        if len(punainenSijainti) > punainenPituus:
            del punainenSijainti[0]

        for x in punainenSijainti[:-1]:
            if x == punainenPaa:
                sammutaPeli = True
                pelinHaviaja = punainen

        for q in punainenSijainti[:-1]:
            if q == keltainenPaa:
                sammutaPeli = True
                pelinHaviaja = keltainen

        keltainenPaa = []
        keltainenPaa.append(leveysKeltainen)
        keltainenPaa.append(korkeusKeltainen)
        keltainenSijainti.append(keltainenPaa)
        if len(keltainenSijainti) > keltainenPituus:
            del keltainenSijainti[0]

        for y in keltainenSijainti[:-1]:
            if y == keltainenPaa:
                sammutaPeli = True
                pelinHaviaja = keltainen

        for w in keltainenSijainti[:-1]:
            if w == punainenPaa:
                sammutaPeli = True
                pelinHaviaja = punainen

        punainenMato(koko, punainenSijainti)
        keltainenMato(koko, keltainenSijainti)

        pygame.display.update()

        if leveysPunainen == ruokaLeveys and korkeusPunainen == ruokaKorkeus:
            ruokaLeveys = round(random.randrange(
                0, naytonLeveys - koko) / 10.0) * 10.0
            ruokaKorkeus = round(random.randrange(
                0, naytonKorkeus - koko) / 10.0) * 10.0
            punainenPituus += 10

        if leveysKeltainen == ruokaLeveys and korkeusKeltainen == ruokaKorkeus:
            ruokaLeveys = round(random.randrange(
                0, naytonLeveys - koko) / 10.0) * 10.0
            ruokaKorkeus = round(random.randrange(
                0, naytonKorkeus - koko) / 10.0) * 10.0
            keltainenPituus += 10

        aika.tick(20)

    pygame.quit()
    quit()


uusiPeli()
