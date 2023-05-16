# Gliederung Lasten- und Pflichten-Heft

## *Mögliche Gliederung:*

## Struktur des Lastenheftes

1. Allgemeines *-> Qusay: "Allgemeines" finde ich besser. Und ich würde folgende Abschnitte vorschlagen:*
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
2. Anforderungen *-> Qusay: Ich würde diesen Abschnitt in funktionale und nicht-funktionale Anforderungen etc. aufteilen. Vllt. noch Umsetzungsanforderungen: Data Selection,Vorverarbeitung, etc.*
   - 2.1 Funktionsumfang
     - 2.1.1 Textzusammenfassung
     - 2.1.2 Textklassifikation
       - Welche Klassen? ggf.Grob formulieren
   - 2.2 Performance-Anforderungen
     - 2.2.1 Schnelligkeit und Reaktionszeit
     - 2.2.2 Speicherplatzbedarf
   - 2.3 Bedienbarkeit
     - 2.3.1 Benutzerfreundlichkeit
     - 2.3.2 Einfache Integration
     - *-> Qusay (mögliche Anforderungen/Eigenschaften): + Hohe Genauigkeit, + Eigenständige Anwendung, + modulare Architektur: Zusammenfassung getrennt von der Klassifikation, grafische Benutzeroberfläche, Qualitätssicherung: z.B. durch Tests*
   - 2.4 Sicherheitsanforderungen *-> Felix: würde ich ggf. weglassen, aber guter Gedanke; Qusay: könnten die Umsetzung zu kompliziert machen*
     - 2.4.1 Datenverschlüsselung (?)
     - 2.4.2 Zugriffsrechte-Management 
   - 2.5 Erweiterbarkeit
     - 2.5.1 Möglichkeit zur Erweiterung der Sprachen und Textarten
     - 2.5.2 Möglichkeit zur Integration von neuen Funktionen
   - 2.6 Projektmanagement
     - 2.6.1 Projektplan (Entwicklungsmodell, Projektphasen, Meilensteine, Zeitplan)
     - 2.6.2 Ressourcenplanung (Hardware-, Software-Ressourcen, Datenquellen, Experten/Erfahrung)
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
3. Anforderungen an die Umsetzung
   - 3.1 Technische Anforderungen
     - 3.1.1 Hardware-Anforderungen
     - 3.1.2 Software-Anforderungen
   - 3.2 Design-Anforderungen
     - 3.2.1 Benutzeroberfläche
     - 3.2.2 Funktionsweise
   - 3.3 Performance-Anforderungen
     - 3.3.1 Schnelligkeit und Reaktionszeit
     - 3.3.2 Speicherplatzbedarf
   - 3.4 Sicherheitsanforderungen
     - 3.4.1 Datenverschlüsselung
     - 3.4.2 Zugriffsrechte-Management
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

