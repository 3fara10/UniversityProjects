//
// Created by Home on 10.05.2024.
//
#include <cassert>
#include <iostream>
#include <stdexcept>
#include "collection.h"
#include "vectordinamic.h"
#include"C:\Users\Home\CLionProjects\L2(2)\transaction.h"
#include"money.h"
void testConstructor()
{
    try
    {
        VectorDinamic<int> x(2);
        VectorDinamic<int> y(-3);
        assert(false);
    }
    catch(std::invalid_argument ex)
    {
        assert(true);
        //std::cout<<ex.what()<<std::endl;
    }
}

void testMoneyClass()
{
    // Test default constructor
    Pereche money1;
    assert(money1.getValue() == 0.0);
    assert(money1.getOccurrences() == 0);

    // Test parameterized constructor
    Pereche money2(10.5, 2);
    assert(money2.getValue() == 10.5);
    assert(money2.getOccurrences() == 2);

    // Test setters and getters
    money1.setValue(15.75);
    money1.setOccurrences(3);
    assert(money1.getValue() == 15.75);
    assert(money1.getOccurrences() == 3);

    assert(money2 < money1);
}

void testCollection() {
    Collection<int> collection;

    // Test add and size methods
    collection.add(10);
    collection.add(20);
    collection.add(30);
    assert(collection.size() == 3);

    // Test search method
    assert(collection.search(10) == true);
    assert(collection.search(40) == false);

    // Test occurrences method
    assert(collection.nrOccurrences(10) == 1);
    assert(collection.nrOccurrences(20) == 1);
    assert(collection.nrOccurrences(30) == 1);
    assert(collection.nrOccurrences(40) == 0);

    // Test remove method
    assert(collection.remove(20) == true);
    assert(collection.size() == 2);
    assert(collection.search(20) == false);
    assert(collection.nrOccurrences(20) == 0);

    // Test assignment operator
    Collection<int> collection2 = collection;
    assert(collection2.size() == 2);
    assert(collection2.search(10) == true);
    assert(collection2.search(30) == true);
}
void testTransaction()
{
    // Test default constructor
    Transaction transactive1;
    assert(transactive1.getId() != 0);
    assert(transactive1.getSum() == 0);

    // Test parameterized constructor
    VectorDinamic<Pereche> bancnote;
    bancnote.push_back(Pereche(10, 5));
    bancnote.push_back(Pereche(20, 3));
    Transaction transaction2(200.0, bancnote);
    assert(transaction2.getSum() == 200.0);

    // Test setter and getter methods
    transactive1.setId(1);
    transactive1.setSuma(100.0);
    assert(transactive1.getId() == 1);
    assert(transactive1.getSum() == 100.0);

    // Test getAll method
    VectorDinamic<Pereche> allBancnote1 = transactive1.getAll();
    assert(allBancnote1.size() == 0);
    assert(transactive1.getSum() == 100); // No money added yet

    VectorDinamic<Pereche> allBancnote2 = transaction2.getAll();
    assert(allBancnote2.size() != 0);
    assert(transaction2.getSum() == 200.0); // Sum of the money added

    // Test setMoney method
    transactive1.setMoney(0, Pereche(50, 2));
    assert(transactive1.getSum() == 50 * 2); // Total sum should be 100

}
void tests()
{
    testTransaction();
    testCollection();
    testConstructor();
    testMoneyClass();

}