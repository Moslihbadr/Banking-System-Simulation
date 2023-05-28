# Banking System Simulation

This is a Python implementation of a banking system simulation. It includes classes for managing bank accounts, performing operations such as deposits and withdrawals, applying interest, and generating account statements.

## Features

- Create a bank account with a unique account number and account holder's name.
- Perform various operations on the account, including deposits and withdrawals.
- Apply interest to the account balance.
- Close the account and generate an account statement.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Simulation

1. Clone the repository or download the source code.
2. Open the terminal and navigate to the project directory.
3. Run the following command to execute the simulation:

   ```bash
   python main.py

Follow the on-screen instructions to interact with the banking system simulation.

## Usage Example
```bash
# Create a new account
c1 = Compte("Badr", 10000)

# Perform operations on the account
c1.Verser("V", 26000, "Virement du salaire du mois 12/2022")
c1.Retirer("G", 5000, "Retrait par guichet bancaire")
c1.AppliquerAgios()

# Generate an account statement
c1.Releve()
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

Feel free to customize the content based on your specific needs and add any additional sections or information.
