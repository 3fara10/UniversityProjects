
#pragma once
#include<istream>
using namespace std;
class Pereche {
private:
    double value;
    int occurrences;
public:
    Pereche();
    Pereche(double newValue,int newOccurrences);
    ~Pereche();

    double getValue() const;
    int getOccurrences() const;
    void setValue(double newValue);
    void setOccurrences(int newOccurrences);

    bool operator <(const Pereche& money) const;
    friend ostream& operator<<(ostream& os, const Pereche& money);
    friend istream& operator>>(istream& is, Pereche& money);
    Pereche& operator=(const Pereche& newMoney);
};
