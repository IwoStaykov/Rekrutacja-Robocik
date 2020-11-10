# Rekrutacja-Robocik
Jako, że zrobiłem tylko pierwsze zadanie to wszystkie pliki są umieszczone w głównym folderze. 
Program składa się z 4 podprogramów :
1) submarine imitujący łódź podwodną
2) speedometer obliczający prędkość na podstawie otrzymanych danych
3) server udostępniający (w formie serwera localhost http) folder Rekrutacja, w którym znajdują się wszystkie podprogramy i pliki typu txt, z których korzystają programy w trakcie pracy
4) receiver(module), w którym zdefiniowane są funkcje potrzebne programowi speedometer do odczytu z serwera localhost

Program submarine miał mieć kontrolę nad serverem i speedometer, a receiver miał pełnić rolę modułu dla speedometer. Niestety nie udało mi się poprawnie wszystkiego wykonać. Nie potrafiłem załączyć serwera poprzez submarine. Dodatkowo sam program ogółem niestety nie działa poprawnie, ponieważ występuje problem z konwertowaniem stringa na flout danych pobranych z serwera http. Gdyby nie to, myślę, że cały program działałby poprawnie. 
W założeniu przy włączeniu submarine mieliśmy wprowadzić liczbę sygnałów, a także odstęp czasowy między kolejnymi sygnałami oraz początkową lokalizację łodzi (3 wartości współrzędnych przestrzeni (x,y,z)). Założyłem, że przestrzenią będzie sześcian 2000x2000x2000 i wartości współrzędnych będą losowane z przedziału [-1000,1000]. Następnie program submarine miał zapisać w plikach tekstowych odpowiednie dane i przejść do pętli, w której losowane są następne współrzędne położenia łodzi, zapisywane w odpowiednim pliku i włączany jest program speedometer. 
Speedometer za pomocą receiver odbiera dane, odpowiednio przypisuje i oblicza prędkość w danym odstępie czasowym, wypisuje prędkość i kończy pracę. Wtedy pętla dobiega końca odczekując wyznaczony czas (symulujemy że submarine płynie w tym czasie), a wszystko powtarza się tyle razy ile sygnałów ma być nadanych.

Kod i komentarze w programach są pisane po angielsku. Mam nadzieję, że są czytelne.

Iwo Staykov
