
#pragma once
#include "vectordinamic.h"
template<typename TElem>
class Collection {
private:
    VectorDinamic<TElem> elements;
public:
    Collection();
    Collection(const Collection& c);
    ~Collection();

    void add(const TElem& elem);
    void update(int position,const TElem& elem);
    bool remove(const TElem& elem);
    bool search(const TElem& elem);
    int size() const;
    int nrOccurrences(TElem elem);
    TElem getAt(int position);

    void operator=(const Collection& c);

};

template<typename TElem>
Collection<TElem>::Collection()
{

}
template<typename TElem>
Collection<TElem>::Collection(const Collection& c)
{
    this->elements=c.elements;
}
template<typename TElem>
Collection<TElem>::~Collection()
{

}
template<typename TElem>
void Collection<TElem>::operator=(const Collection& c) {
    this->elements = c.elements;
}
template<typename TElem>
void Collection<TElem>::add(const TElem& elem) {
    this->elements.push_back(elem);
}

template <typename TElem>
void Collection<TElem>::update(int position, const TElem& elem)
{
    if (position < 0 || position >= elements.size()) {
        throw std::out_of_range("Index out of range");
    }
    TElem elem1=this->elements.update(position,elem);
}

template<typename TElem>
bool Collection<TElem>::remove(const TElem& elem) {
    for (int i = 0; i < this->elements.size(); ++i) {
        if (elements.getAt(i) == elem) {
            elements.sterge(i);
            return true;
        }
    }
    return false;
}
template<typename TElem>
bool Collection<TElem>::search(const TElem& elem) {
    for (int i = 0; i < this->elements.size(); ++i) {
        if (elements.getAt(i) == elem) {
            return true;
        }
    }
    return false;
}
template<typename TElem>
int Collection<TElem>::size() const {
    return this->elements.size();
}
template<typename TElem>
int Collection<TElem>::nrOccurrences(TElem elem)
{
    int count = 0;
    for (int i = 0; i < elements.size(); ++i) {
        if (elements.getAt(i) == elem) {
            count++;
        }
    }
    return count;
}
template<typename TElem>
TElem Collection<TElem>::getAt(int position)
{
    return this->elements.getAt(position);
}
