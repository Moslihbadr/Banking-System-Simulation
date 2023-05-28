# Simulation de Système Bancaire

Il s'agit d'une implémentation en Python d'une simulation de système bancaire. Elle comprend des classes pour gérer les comptes bancaires, effectuer des opérations telles que les dépôts et les retraits, appliquer des intérêts et générer des relevés de compte.

## Fonctionnalités

- Créer un compte bancaire avec un numéro de compte unique et le nom du titulaire du compte.
- Effectuer diverses opérations sur le compte, y compris les dépôts et les retraits.
- Appliquer des intérêts au solde du compte.
- Clôturer le compte et générer un relevé de compte.

## Pour commencer

### Prérequis

- Python 3.x

### Exécution de la Simulation

1. Clonez le dépôt ou téléchargez le code source.
2. Ouvrez le terminal et accédez au répertoire du projet.
3. Exécutez la commande suivante pour lancer la simulation :

   ```bash
   python main.py

Suivez les instructions à l'écran pour interagir avec la simulation du système bancaire.

## Exemple d'utilisation

   ```bash
  # Créer un nouveau compte
  c1 = Compte("Badr", 10000)

  # Effectuer des opérations sur le compte
  c1.Verser("V", 26000, "Virement du salaire du mois 12/2022")
  c1.Retirer("G", 5000, "Retrait par guichet bancaire")
  c1.AppliquerAgios()

  # Générer un relevé de compte
  c1.Releve()
  ```

## Contribuer

Les contributions sont les bienvenues ! Si vous rencontrez des problèmes ou avez des suggestions d'amélioration, veuillez ouvrir une issue ou soumettre une pull request.

## Licence

Ce projet est sous licence MIT.

N'hésitez pas à personnaliser le contenu en fonction de vos besoins spécifiques et d'ajouter des sections ou des informations supplémentaires.
