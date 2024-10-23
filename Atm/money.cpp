#pragma once
#include "money.h"
Pereche::Pereche()
{
    this->value = 0;
    this->occurrences=0;
}

Pereche::Pereche(double newValue,int newOccurrences)
{
    this->value = newValue;
    this->occurrences=newOccurrences;
}

Pereche::~Pereche()
{
}

double Pereche::getValue() const
{
    return this->value;
}

int Pereche::getOccurrences() const
{
    return this->occurrences;
}

void Pereche::setValue(double newValue)
{
    this->value = newValue;
}

void Pereche::setOccurrences(int newOccurrences)
{
    this->occurrences=newOccurrences;
}

bool Pereche::operator<(const Pereche& money) const
{
    return this->value < money.value;
}

Pereche& Pereche::operator=(const Pereche& newMoney)
{
    this->value=newMoney.value;
    this->occurrences=newMoney.occurrences;
    return *this;
}

ostream& operator<<(ostream& os, const Pereche& money)
{
    os << money.getValue();
    return os;
}

istream& operator>>(istream& is, Pereche& money)
{
    is >> money.value;
    return is;
}
