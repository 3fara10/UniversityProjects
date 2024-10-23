#include "atm.h"
#include "collection.h"
#include"tests.h"
#include "ui.h"
class Money;

int main()
{
    Collection<Money> banknotes;
    banknotes.add(Money(100, 50));
    banknotes.add(Money(50, 45));
    banknotes.add(Money(10, 100));

    Atm atm(banknotes);

    UI ui(atm);
    ui.run();

    return 0;
}