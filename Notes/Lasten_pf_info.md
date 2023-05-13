# Informationen über Last- und Pflichtenheft

Das Lastenheft beschreibt die Anforderungen an ein Produkt oder System aus der Sicht des Kunden oder Benutzers, während das Pflichtenheft die Anforderungen aus der Sicht des Entwicklers oder Herstellers beschreibt und spezifiziert, wie diese Anforderungen umgesetzt werden sollen.
Das Lastenheft beschreibt die Anforderungen und Erwartungen des Kunden oder Benutzers an das zu entwickelnde Produkt. Es legt fest, welche Funktionen und Leistungen das Produkt haben soll, welche Bedienung es ermöglichen muss, welche Schnittstellen zu anderen Systemen vorhanden sein müssen und welche Leistungsmerkmale es erfüllen muss. Das Pflichtenheft geht einen Schritt weiter und beschreibt, wie diese Anforderungen umgesetzt werden sollen. Es legt fest, welche technischen Spezifikationen erfüllt werden müssen, welche Programmiersprachen, Datenbanken oder Betriebssysteme verwendet werden sollen und wie das Produkt getestet werden muss, um sicherzustellen, dass es alle Anforderungen erfüllt.

Generell ist es ein Synonym für Requiremnet document. Das Requirements Document umfasst normalerweise beide Perspektiven, indem es die Anforderungen aus der Sicht des Kunden und des Entwicklers beschreibt und spezifiziert, wie diese Anforderungen erfüllt werden sollen. Es ist ein umfassendes Dokument, das als Grundlage für die weitere Entwicklung, Umsetzung und Überprüfung des Produkts oder Systems dient.

Also tendentiell können wir die generelle Anforderung nach Last- und Pflichtenheft führen (Aufteilung in unterschiedlichen Perspektiven) und im Anschluss mit Requirement tracability matrix, Requirement vaidation matrix und feasibility matrix zu documentieren, zu "verfolgen". 

Im Folgenden sind paar Gedanken aufgeführt (muss natürlich erweitert und spezifiziert werden):

## 1. Ziel

Das Ziel dieses Projekts ist die Entwicklung eines Tools zur Textzusammenfassung und -klassifikation in Kleingruppen, das in der Lage ist, lange Texte automatisch zu analysieren und eine zusammenfassende Zusammenfassung des Inhalts zu generieren, die leicht verständlich ist. Das Tool sollte auch in der Lage sein, den Inhalt von Texten zu analysieren und sie in vordefinierten Kategorien zu klassifizieren.

## 2. Lastenheft

### 2.1 Zielsetzung

- Entwicklung eines Tools zur Textzusammenfassung und -klassifikation
- Einfache Bedienung für die Zielgruppe
- Kompressionsrate für die Zusammenfassung soll frei wählbar sein (aber eine Möglichkeit muss exisiteren: 100% Text auf 20% runterbrechen)
- Klassifizierung der Texte in unterschiedliche Oberkategorien
- Ein mehrstufiger Ansatz soll verwendet werden
- Evaluation des Tools anhand geeigneter Metriken

### 2.2 In Anforderungen an die Funktionalität formuliert

- Das Tool soll in der Lage sein, einen gegebenen Text zusammenzufassen und eine gewünschte Kompressionsrate anzugeben
- Die Klassifizierung des Textes soll automatisch in Oberkategorien wie Nachrichtenartikel, literarischer Text, Blogbeitrag usw. erfolgen
- Das Tool soll einen mehrstufigen Ansatz verwenden, einschließlich Data Selection, Preprocessing und Training des Modells
- Der Algorithmus zur Zusammenfassung und Klassifikation soll ausgewählt und angepasst werden können
- Das Tool soll mit einer Benutzeroberfläche ausgestattet sein, die einfach zu bedienen ist
- Das Tool soll auf einer zuverlässigen und skalierbaren Infrastruktur laufen
- Das Tool soll die Möglichkeit bieten, die erstellten Zusammenfassungen und Klassifizierungen in verschiedenen Formaten zu exportieren (maybe?)


## 3. Pflichtenheft

- Das Pflichtenheft enthält die vom "Auftragnehmer erarbeiteten Realisierungsvorgaben" und es beschreibt die "Umsetzung des vom Auftraggeber vorgegebenen

### Funktionale Anforderungen

- Entwicklung eines Algorithmus zur Zusammenfassung von Texten basierend auf der gewünschten Kompressionsrate
- Entwicklung eines Algorithmus zur automatischen Klassifizierung von Texten in verschiedene Oberkategorien
- Implementierung eines mehrstufigen Ansatzes, einschließlich Data Selection, Preprocessing und Training des Modells
- Entwicklung einer Benutzeroberfläche, die einfach zu bedienen ist
- Entwicklung einer skalierbaren Infrastruktur zur Ausführung des Tools
- Möglichkeit zum Exportieren der Zusammenfassungen und Klassifizierungen in verschiedenen Formaten

### Nicht funktionale Anforderungen

- Das Tool muss sicher und zuverlässig sein
- Die Antwortzeiten müssen akzeptabel sein
- Das Tool muss einfach zu warten und zu aktualisieren sein
- Das Tool muss auf verschiedenen Betriebssystemen lauffähig sein
- Das Tool muss auf verschiedenen Plattformen, wie z.B. Desktop und Mobilgeräten, nutzbar sein (Müssen wir noch diskutieren)

### Technische Anforderungen

- Das Tool soll in Python entwickelt werden (?)
- Die Daten sollen in einer Datenbank gespeichert werden (?)
- Das Tool soll auf einer Cloud-Infrastruktur ausgeführt werden (?)

### Qualitätsanforderungen

- Das Tool soll auf eine hohe Genauigkeit bei der Zusammenfassung und Klassifizierung von Texten optimiert sein, dazu sollte man passende Metriken überlegen
- Das Tool soll mit einer ausreichenden Anzahl von Testfällen validiert werden
- Das Tool soll mit einer entsprechenden Dokumentation versehen

## Schematische Darstellung
![image](https://github.com/FelixSHA/text-summary/assets/105482809/05739e03-1ae0-4d53-b0ce-6505fba58147)

## Mögliche Gliederung
### Struktur des Lastenheftes
1. Einleitung
   - 1.1 Hintergrund
   - 1.2 Zielsetzung
   - 1.3 Umfang
2. Anforderungen
  2.1 Funktionsumfang
    2.1.1 Textzusammenfassung
    2.1.2 Textklassifikation
  2.2 Performance-Anforderungen
    2.2.1 Schnelligkeit und Reaktionszeit
    2.2.2 Speicherplatzbedarf
  2.3 Bedienbarkeit
    2.3.1 Benutzerfreundlichkeit
    2.3.2 Einfache Integration
  2.4 Sicherheitsanforderungen
    2.4.1 Datenverschlüsselung (?)
    2.4.2 Zugriffsrechte-Management 
  2.5 Erweiterbarkeit
    2.5.1 Möglichkeit zur Erweiterung der Sprachen und Textarten
    2.5.2 Möglichkeit zur Integration von neuen Funktionen
3. Annahmen und Einschränkungen
  3.1 Annahmen
    3.1.1 Verwendung von Open-Source-Tools und Algorithmen
    3.1.2 Vorhandensein ausreichend großer Textdatenbanken
  3.2 Einschränkungen
    3.2.1 Beschränkung auf bestimmte Textarten
    3.2.2 Beschränkung auf bestimmte Sprachen
4. Abnahmekriterien
  4.1 Abnahmekriterien für die Textzusammenfassung
  4.2 Abnahmekriterien für die Textklassifikation
  4.3 Abnahmekriterien für die Performance
  4.4 Abnahmekriterien für die Bedienbarkeit
  4.5 Abnahmekriterien für die Sicherheit
  4.6 Abnahmekriterien für die Erweiterbarkeit
5. Glossar
  5.1 Definitionen von Begriffen, die im Lastenheft verwendet werden.

