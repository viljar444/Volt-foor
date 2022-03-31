import pygame                                                       #mooduli pygame importimine

pygame.init()                                                       #pygame käivitamine
screen=pygame.display.set_mode([300,300])                           #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.Akna mõõt 300x300 px.
pygame.display.set_caption("Foor-Viljar Volt")                      #aknale nimetuse andmine
pygame.draw.line(screen, [255,255,255], [100, 10], [100,270], 2)    #joone joonistamine,värvus valge,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,255,255], [100, 270], [200,270], 2)   #joone joonistamine,värvus valge,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,255,255], [200, 270], [200,10], 2)    #joone joonistamine,värvus valge,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,255,255], [200, 10], [100,10], 2)     #joone joonistamine,värvus valge,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.circle(screen, [255, 0, 0], [150,55], 40, 0)            #joonistab ringi ekraanile,värvus punane,xy koordinaadid,raadius 40, 0 täidab kujundi värviga
pygame.draw.circle(screen, [255, 255, 0], [150,140], 40, 0)         #joonistab ringi ekraanile,värvus kollane,xy koordinaadid,raadius 40, 0 täidab kujundi värviga
pygame.draw.circle(screen, [0, 255, 0], [150,225], 40, 0)           #joonistab ringi ekraanile,värvus roheline,xy koordinaadid,raadius 40, 0 täidab kujundi värviga


pygame.display.flip()                                               #ekraani värskendamine






from sys import exit                         #mooduli importimine, et ekraan ei sulguks
while True:                                  #korduslause kui õige
        for event in pygame.event.get():     #event omistab mooduli parameetird
            if event.type == pygame.QUIT:    #tingimusel kui võrdne
                pygame.quit()                #lõpetab tegevuse kui, kasutaja aktiveerib
                exit()                       #väljub







