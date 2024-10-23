//
// Created by Home on 12.05.2024.
//
#pragma once

#include "collection.h"
#include "money.h"
#include "C:\Users\Home\CLionProjects\L2(2)\transaction.h"

class Atm
{
private:
    Collection<Pereche> banknotes;
    VectorDinamic<Transaction>transactions;
public:
    Atm(const Collection<Pereche>& collection);
    ~Atm();
    Transaction atm(double sum);
    void add(double sum);
    Collection<Pereche> getCollection();
    VectorDinamic<Transaction> getTransactions() const;
    void setCollection(const Collection<Pereche>& collection);
    int getNo(int postion);
    double getValue(int position);
};


