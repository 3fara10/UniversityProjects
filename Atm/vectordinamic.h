//
// Created by Home on 10.05.2024.
//
#pragma once
#include<stdexcept>
template <class TElem>
class VectorDinamic
{
private:
    int capacity;
    int nrElems;
    TElem* elems;
    void resize();
public:
    VectorDinamic();
    //The parametrized constructor
    VectorDinamic(int capacitate);
    ~VectorDinamic();
    VectorDinamic(const VectorDinamic<TElem>& other);
    //Return the number of elements
    int size() const;

    //Return the element of the i position
    TElem getAt(int i)const;

    //Add an element at the final
    void push_back(const TElem& e);
    //Add an element at the i position
    void addAt(int i, TElem e);
    //Delete an element of the i position
    TElem update(int i,TElem e);
    TElem sterge(int i);

    VectorDinamic<TElem>& operator=(const VectorDinamic& other);

};

template <class TElem>
void VectorDinamic<TElem>::resize()
{
    this->capacity = this->capacity * 2;
    TElem* newElems = new TElem[this->capacity];
    for (int i = 0; i < this->nrElems; i++)
    {
        newElems[i] = this->elems[i];
    }
    delete[] this->elems;
    this->elems = newElems;
}

template <class TElem>
VectorDinamic<TElem>::VectorDinamic()
{
    this->capacity = 100;
    this->nrElems = 0;
    this->elems = new TElem[this->capacity];
}

template <class TElem>
VectorDinamic<TElem>::VectorDinamic(int capacitate)
{
    if (capacitate <= 0)
    {
        throw std::invalid_argument("Invalid input exception: capacity must be greater than 0");
    }
    this->capacity = capacitate;
    this->nrElems = 0;
    this->elems = new TElem[this->capacity];
}

template <class TElem>
VectorDinamic<TElem>::~VectorDinamic()
{
    delete []this->elems;
}

template<class TElem>
inline VectorDinamic<TElem>::VectorDinamic(const VectorDinamic<TElem>& other)
{
    this->capacity = other.capacity;
    this->nrElems = other.nrElems;
    this->elems = new TElem[capacity];
    for (int i = 0; i < nrElems; ++i) {
        this->elems[i] = other.elems[i];
    }
}

template <class TElem>
int VectorDinamic<TElem>::size() const
{
    return this->nrElems;
}

template <class TElem>
TElem VectorDinamic<TElem>::getAt(int i) const
{
    if (i < 0 || i >= this->nrElems)
    {
        throw std::invalid_argument("Invalid input exception: index out of bounds");
    }
    return this->elems[i];
}

template <class TElem>
void VectorDinamic<TElem>::push_back(const TElem& e)
{
    if (this->nrElems == this->capacity)
    {
        this->resize();
    }
    this->elems[this->nrElems] = e;
    ++this->nrElems;
}

template <class TElem>
void VectorDinamic<TElem>::addAt(int i, TElem e)
{
    if (i < 0 || i > this->nrElems)
    {
        throw std::invalid_argument("Invalid input exception: index out of bounds");
    }
    if (this->nrElems == this->capacity)
    {
        resize();
    }
    for (int j = this->nrElems; j > i; --j)
    {
        this->elems[j] = this->elems[j - 1];
    }
    this->elems[i] = e;
    ++this->nrElems;
}

template <class TElem>
TElem VectorDinamic<TElem>::update(int i, TElem e)
{
    if (i < 0 || i > this->nrElems)
    {
        throw std::invalid_argument("Invalid input exception: index out of bounds");
    }

    this->elems[i]=e;
    return this->elems[i];
}


template <class TElem>
TElem VectorDinamic<TElem>::sterge(int i)
{
    if (i < 0 || i >= this->nrElems)
    {
        throw std::invalid_argument("Invalid input exception: index out of bounds");
    }
    TElem value = this->elems[i];
    for (int j = i; j < this->nrElems - 1; j++)
    {
        this->elems[j] = this->elems[j + 1];
    }
    --this->nrElems;
    return value;
}

template <class TElem>
VectorDinamic<TElem>& VectorDinamic<TElem>::operator=(const VectorDinamic& other)
{
    if (this == &other) {
        return *this;
    }
    delete[] this->elems;
    this->capacity = other.capacity;
    this->nrElems = other.nrElems;
    this->elems = new TElem[capacity];
    for (int i = 0; i < nrElems; ++i) {
        this->elems[i] = other.elems[i];
    }

    return *this;
}
