#include"atm.h"

Atm::Atm(const Collection<Pereche>& collection)
{
    this->banknotes=collection;
}

Atm::~Atm()
{
}

Transaction Atm::atm(double sum)
{
    //Take all current banknotes.
    Collection<Pereche> currentCollection = this->banknotes;
    //Create a vector for the banknotes used in transaction.
    VectorDinamic<Pereche> usedBanknotes(100);
    double currentSum = sum;

    for (int i = 0; i < currentCollection.size() && currentSum > 0; ++i) {
        //We take a banknote in turn.
        Pereche money = currentCollection.getAt(i);
        //We see how many banknotes we can use to pay that amount.
        int numNotes = min(int(currentSum / money.getValue()), money.getOccurrences());
        if (numNotes > 0) {
            //Update the vector.
            usedBanknotes.push_back(Pereche(money.getValue(), numNotes));
            //We subtract from the current amount the amount paid with the current banknote.
            currentSum -= numNotes * money.getValue();
            currentCollection.update(i, Pereche(money.getValue(), money.getOccurrences() - numNotes));
        }
    }
    if (currentSum > 0) {
        throw runtime_error("Insufficient funds to complete the transaction.");
    }
    Transaction transaction(sum, usedBanknotes);
    //Update the banknote collection with the modified collection.
    this->banknotes = currentCollection;
    //return the transaction
    return transaction;
}

void Atm::add(double sum)
{
    this->transactions.push_back(this->atm(sum));
}

Collection<Pereche> Atm::getCollection()
{
    return this->banknotes;
}

VectorDinamic<Transaction> Atm::getTransactions() const
{
    return this->transactions;
}

void Atm::setCollection(const Collection<Pereche>& collection)
{
    this->banknotes = collection;
}

int Atm::getNo(int position)
{
    return banknotes.getAt(position).getOccurrences();
}

double Atm::getValue(int position)
{
    return banknotes.getAt(position).getValue();
}
