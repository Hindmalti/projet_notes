# Parser notes
A mon école (Polytech'Lille), nous avons une interface pour visualiser nos notes et résultats d'examens. Mais nous ne recevons aucune notification pour nous prévenir de l'arrivée d'une nouvelle note. Je trouvais ça barbant de devoir checker régulièrement et rafraichir la page dans l'espoir de voir une nouvelle note.
L'idée de ce projet m'est alors venue ! Pourquoi pas créer un bot qui parse régulièrement la page pour moi, stocke les données existantes sur une DynamoDB sur AWS et il compare régulièrement, s'il y a un changement (ajout d'une note) il me prévient avec un mail ! 



## Auteurs 
Durot Anthony- Hind MALTI Juin 2020