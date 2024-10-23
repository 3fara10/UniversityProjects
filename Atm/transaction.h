//
// Created by Home on 10.05.2024.
//
#pragma once
#include <random>
#include <unordered_set>
#include<ctime>
#include "money.h"
#include "vectordinamic.h"

class Transaction
{
private:
    //The transaction ID.
    int idTransaction;
    //The amount that was made in this transaction.
    double sum;
    //The banknotes that were used in the current transaction.
    VectorDinamic<Pereche> banknotes;

    //A function to generate the id.
    static int generateId();

public:
    //The default constructor.
    Transaction();

    //Parameterized constructors
    Transaction(double newSum);
    Transaction(double newSum, const VectorDinamic<Pereche>& newBanknotes);
    //Deconstructor
    ~Transaction();

    //Returns the id of the current transaction.
    int getId() const;
    //Returns the sum of the current transaction.
    double getSum() const;
    //Returns the number of banknotes used in the current transaction.
    int getSize() const;

    //Returns a Money object from the given position.
    Pereche getAt(int position) const;
    //Returns all the banknotes used in the current transaction.
    const VectorDinamic<Pereche>& getAll() const;

    //Setters
    void setId(int newId);
    void setSuma(double newSuma);
    void setMoney(int position, const Pereche& money);

    //The assignment operator
    Transaction& operator=(const Transaction& other);
};


#pragma once
#include"C:\Users\Home\CLionProjects\L2(2)\transaction.h"

inline Transaction::Transaction()
{
    this->idTransaction = this->generateId();
    this->sum = 0;
}

inline Transaction::Transaction(double newSum)
{
    this->idTransaction = this->generateId();
    this->sum = newSum;
}

inline Transaction::Transaction(double newSum, const VectorDinamic<Pereche>& newBancnote)
{
    this->idTransaction = this->generateId();
    this->sum = newSum;
    this->banknotes = newBancnote;
}

inline Transaction::~Transaction()
{
}


inline int Transaction::getId() const
{
    return this->idTransaction;
}

inline double Transaction::getSum() const
{
    return this->sum;
}

inline int Transaction::getSize() const
{
    return this->banknotes.size();
}


inline Pereche Transaction::getAt(int position) const
{
    return this->banknotes.getAt(position);
}

inline const VectorDinamic<Pereche>& Transaction::getAll() const
{
    return this->banknotes;
}

inline void Transaction::setId(int newId)
{
    this->idTransaction = newId;
}

inline void Transaction::setSuma(double newSuma)
{
    this->sum = newSuma;
}

inline void Transaction::setMoney(int position, const Pereche& money)
{
    Pereche x = this->banknotes.update(position, money);
}

inline Transaction& Transaction::operator=(const Transaction& other)
{
    if (this == &other) {

        return *this;
    }
    this->idTransaction = other.idTransaction;
    this->sum = other.sum;
    this->banknotes = other.banknotes;

    return *this;
}

inline int Transaction::generateId()
{
    //Init a random number from 1 to 1000000
    static std::mt19937 random(static_cast<unsigned int>(std::time(nullptr)));
    static std::uniform_int_distribution<int> dist(1, 1000000);

    int newId = dist(random);
    return newId;
}
