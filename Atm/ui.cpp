#include "ui.h"
#include <iostream>

UI::UI(const Atm& atm) : atm(atm) {}

void UI::showMenu() {
    std::cout << "ATM Menu:\n";
    std::cout << "1. Add transaction\n";
    std::cout << "2. Verify transaction\n";
    std::cout << "3. Display banknotes\n";
    std::cout << "4. Display transactions\n";
    std::cout << "5. Exit\n";
}

void UI::addTransaction() {
    double amount;
    std::cout << "Enter transaction amount :" ;
    std::cin >> amount;
    this->atm.add(amount);
    this->transaction(amount);
}

void UI::verifyTransaction() {
    double amount;
    std::cout << "Enter the amount to verify: ";
    std::cin >> amount;
    this->transaction(amount);
}

void UI::printBanknotes() {
    Collection<Pereche> collection = atm.getCollection();
    std::cout << "The banknotes are:"<<endl;

    for (int i = 0; i < collection.size(); ++i) {
        Pereche money;
        money = collection.getAt(i);
        std::cout << "Value: " << money.getValue() << ", Number of: " << money.getOccurrences() << std::endl;
    }
}

void UI::printTransactions() {
    VectorDinamic<Transaction> transactions = atm.getTransactions();
    std::cout << "The transactions are:"<<endl;

    for (int i = 0; i < transactions.size(); ++i) {
        Transaction transaction;
        transaction = transactions.getAt(i);
        std::cout << "Transaction ID: " << transaction.getId() << ", Amount: " << transaction.getSum() << "\n";
        std::cout << "Used banknotes:\n";

        for (int j = 0; j < transaction.getAll().size(); ++j) {
            Pereche money;
            money = transaction.getAll().getAt(j);
            std::cout << "Value: " << money.getValue() << ", Number of: " << money.getOccurrences() << std::endl;
        }
    }
}

void UI::transaction(double amount)
{
    try {
        Transaction transaction;
        transaction = atm.atm(amount);
        std::cout << "Transaction ID: " << transaction.getId() << endl;
        std::cout << "Used banknotes:" << endl;

        for (int i = 0; i < transaction.getAll().size(); ++i) {
            Pereche money;
            money = transaction.getAll().getAt(i);
            std::cout << "Value: " << money.getValue() << ", Number of: " << money.getOccurrences() << std::endl;
        }

    }
    catch (const std::exception& e) {
        std::cout << e.what() << endl;
    }
}

void UI::run()
{
    bool run = true;
    while (run)
    {
        showMenu();
        char option;
        cout << "Enter the option: ";
        cin >> option;
        
        switch (option)
        {
            case '1':
            {
                this->addTransaction();
                break;
            }
            case '2':
            {
                this->verifyTransaction();
                break;
            }
            case '3':
            {
                this->printBanknotes();
                break;
            }
            case '4':
            {
                this->printTransactions();
                break;
            }
            case'5':
            {
                run = false;
                break;
            }
            default:
                std::cout << "Invalid option. Try again!";
                std::cout << std::endl;
        }
    }
}