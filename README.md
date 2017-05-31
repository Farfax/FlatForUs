# FlatForUs


@Wytyczne:
- Utworzyć strukturę bazy danych - MySQL. Najistotniejsze jest byście przygotowali
strukturę bazy danych wraz z relacjami pomiędzy obiektami oraz migracje dla bazy danych.

Status:
        Zrealizowano


- Przygotować panel administratora – tak by najistotniejsze dane były pokazywane w
odpowiedni sposób (pogrupowane) oraz najczęściej wykonywane akcje były
zautomatyzowane (np. Administrator ma zmienić status kilku mieszkań na niedostępny,
zamiast wchodzić wkażde mieszkanie osobno, lepiej by mógł zaznaczyć pokoje i wybrać
odpowiednią akcję)

Status:
        Zrealizowano
       
       
- Możliwość dodawania miast, możliwość dodawania mieszkań oraz przypisywania mieszkań
do miast. W samych obiektach możliwość ustawiania od kiedy do kiedy są dostępne.

Status:
        Zrealizowano


- Powinna być również informacja (lista) o rezerwacjach danego obiektu (od kiedy do kiedy 
oraz nickname),

Status:
        Częściowa realizacja za pomocą filtrów.

- Wiadomo - nie może być więcej jak jednej rezerwacji w jednym terminie

Status:
        W trakcie.(Mysql nie obsługuje distinct(), brak możliwości użycia unique=True)
        
        
@Cele:
- Rozwinąć automatyzacje panelu użytkownika
    *możliwość przypisania jednej daty do wielu mieszkań
    *zmiana miasta wielu mieszkań
    
 - Poprawić validację rezerwacji
 
 - Automatyzacja rejestracji modeli
 
 - Obsługa wyjątków validatora rezerwacji
 
 @Instalacja/Wymagania/Technologie
    Aplikacja powstała w oparciu o Django 1.11 oraz Python3, w systemie Arch Linux(wersja jądra 4.10.13-1). 
    Z powodów technicznych w testach użyto Mariadb 4.10.13-1(która jest oparta na MySQL)
    Hasła/Loginy użyte w bazie danych zawarte w settings.py.
