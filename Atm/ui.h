#pragma once
#include "atm.h"

class UI {
private:
    Atm atm;
    static void showMenu();
    void addTransaction();
    void verifyTransaction();
    void printBanknotes();
    void printTransactions();
    void transaction(double amount);
public:
    UI(const Atm& atm);
    void run();
};

