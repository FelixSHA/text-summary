# Gliederung Lasten- und Pflichten-Heft

## *Mögliche Gliederung:*

## Struktur des Lastenheftes

1. Allgemeines
   - 1.1 Ziel und Zweck des Dokumentes
   - 1.2 Ausgangssituation
     - Keine Datensätze vorhanden
   - 1.3 Projektbezug
   - 1.4 Abkürzungen
   - 1.5 Verteiler und Freigabe
   *-> Qusay: bis hier*
   - 1.1 Hintergrund
     - ggf. inkl Motivation
   - 1.2 Zielsetzung
     - Aufgabenstellung von Dozenten
     - (nicht vorhandenen) Istzustand erläutern
   - 1.3 Umfang
2. Anforderungen
   - 2.1 Funktionale Anforderungen
      - 2.2.1 Funktionsumfang
         - Textzusammenfassung
         - Textklassifikation
            - Welche Klassen? ggf.Grob formulieren
   - 2.2 Nicht-funktionale Anforderungen
      - 2.2.1 Performance-Anforderungen
        - Schnelligkeit und Reaktionszeit
        - Speicherplatzbedarf
      - 2.2.2 Bedienbarkeit
        - Benutzerfreundlichkeit
        - Einfache Integration
     - *-> Qusay (mögliche Anforderungen/Eigenschaften): + Hohe Genauigkeit, + Eigenständige Anwendung, + modulare Architektur: Zusammenfassung getrennt von der Klassifikation, grafische Benutzeroberfläche, Qualitätssicherung: z.B. durch Tests*
      - 2.2.3 Sicherheitsanforderungen *-> Felix: würde ich ggf. weglassen, aber guter Gedanke; Qusay: könnten die Umsetzung zu kompliziert machen*
        - Datenverschlüsselung (?)
        - Zugriffsrechte-Management 
      - 2.2.4 Erweiterbarkeit
        - Möglichkeit zur Erweiterung der Sprachen und Textarten
        - Möglichkeit zur Integration von neuen Funktionen
      - 2.2.5 Projektmanagement
        - Projektplan (Entwicklungsmodell, Projektphasen, Meilensteine, Zeitplan)
        - Ressourcenplanung (Hardware-, Software-Ressourcen, Datenquellen, Experten/Erfahrung)
3. Annahmen und Einschränkungen
   - 3.1 Annahmen
     - 3.1.1 Verwendung von( Open-Source-Tools und) geeigneten Algorithmen
     - 3.1.2 (Vorhandensein ausreichend großer Textdatenbanken) Datensätze geeignet
   - 3.2 Einschränkungen
     - 3.2.1 Beschränkung auf bestimmte Textarten
     -  3.2.2 Beschränkung auf bestimmte Sprachen
4. Abnahmekriterien (Kundensicht)
   - 4.1 Abnahmekriterien für die Textzusammenfassung
      - 4.1.1 Performance
        - inkl. Güte
      - 4.1.2 Bedienbarkeit
      - 4.1.3. Sicherheit
      - 4.1.4. Erweiterbarkeit
   - 4.2 Abnahmekriterien für die Textklassifikation
      - 4.2.1 Performance
        - inkl. Güte
      - 4.2.2 Bedienbarkeit
      - 4.2.3. Sicherheit
      - 4.2.4. Erweiterbarkeit
5. Glossar
   - 5.1 Definitionen von Begriffen, die im Lastenheft verwendet werden.


## Struktur Pflichtenheft

1. Einleitung
    
2. Beschreibung des Tools
   - 2.1 Übersicht
   - 2.2 Funktionen (Beschreibung)
     - 2.2.1 Textzusammenfassung
     - 2.2.2 Textklassifikation
   - 2.3 Schnittstellen
     - Integration in bestehende Systeme
     - bestehende Seite des Auftragsgebers
     - (Schnittstellen)
3. Anforderungen an das Tool
   - 2.1 Funktionale Anforderungen
      - 2.2.1 Funktionsumfang
         - Textzusammenfassung
         - Textklassifikation
            - Welche Klassen? ggf.Grob formulieren
   - 2.2 Nicht-funktionale Anforderungen
      - 2.2.1 Performance-Anforderungen
        - Schnelligkeit und Reaktionszeit
        - Speicherplatzbedarf
      - 2.2.2 Bedienbarkeit
        - Benutzerfreundlichkeit
        - Einfache Integration
      - 2.2.3 Sicherheitsanforderungen 
        - Datenverschlüsselung
        - Zugriffsrechte-Management 
      - 2.2.4 Erweiterbarkeit
        - Möglichkeit zur Erweiterung der Sprachen und Textarten
        - Möglichkeit zur Integration von neuen Funktionen
      - 2.2.5 Projektmanagement
        - Projektplan (Entwicklungsmodell, Projektphasen, Meilensteine, Zeitplan)
        - Ressourcenplanung (Hardware-, Software-Ressourcen, Datenquellen, Experten/Erfahrung)

4. Test- und Qualitätsanforderungen
   - 4.1 Evaluierung
     - Metriken (BLEU, ROUGE, Human Evaluation)
   - 4.2 Benutzerfreundlichkeit (externe Prüfung, z.B. Pilotenphase)

5. Dokumentationsanforderungen
   - 5.1 Anforderungen an die technische Dokumentation
     - Kommentare
     - Readme
     - Beschreibung von Tools, Caveats, etc.
     - Anleitung für weiteres Training der Modelle 
   - 5.2 Anforderungen an die Benutzerdokumentation
     - Anleitung für UI
     - Einschränkungen
6. Projektmanagement (generelle Information)
   - 1.1 Ablaufbeschreibung (Implementation)
   - 1.2 Verwendete Techniken
      - ... (*Die eizelnen Schritte im Ablauf (Modellierung Summerizer, Modellierung Klassifier, Datenaufbereitung, Frontend, ...)*)
   - 6.1 Zeitplan
   - grober Strukturplan
   - 6.2 Ressourcenplan
     - Personal
     - Software
     - Hardware
   - 6.3 Mögliche Risiken
     - Mögliche Probleme (fehlende Daten, Systemausfall, etc.)
     - keine Haftung bei Verzögerungen, falscher Modellaussagen
7. Abnahmekriterien (Entwicklersicht)
   - 7.1 Abnahmekriterien für die Textzusammenfassung
      - 7.1.1 Performance
      - 7.1.2 Bedienbarkeit
      - 7.1.3. Sicherheit
      - 7.1.4. Erweiterbarkeit
   - 7.2 Abnahmekriterien für die Textklassifikation
      - 7.2.1 Performance
      - 7.2.2 Bedienbarkeit
      - 7.2.3. Sicherheit
      - 7.2.4. Erweiterbarkeit
8. Glossar
   - 8.1 Definitionen von Begriffen, die im Pflichtenheft verwendet werden.

![](https://images.acquisa.de/media/pages/magazin/lastenheft-pflichtenheft/ddec44d260-1673887926/lastenheft-pflichtenheft-infografik.png?width=762&fit=1&enlarge=0&v=ddec44d260-1673887926)

