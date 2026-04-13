item(1, margherita).
item(2, pepperoni).
item(3, veggie).
item(4, chicken).
item(5, pasta).
item(6, bread).


set_prices :-
    item(_, Item),
    write('Enter price for '), write(Item), write(': '),
    read(P),
    assert(price(Item, P)),
    fail.
set_prices.


show_menu :-
    nl, write('------ MENU WITH PRICES ------'), nl,
    item(N, Item),
    price(Item, Price),
    write(N), write('. '), write(Item),
    write(' - Rs.'), write(Price), nl,
    fail.
show_menu.

take_order :-
    write('Enter item number (0 to stop): '),
    read(Choice),
    handle_order(Choice).

handle_order(0) :- !.

handle_order(Choice) :-
    item(Choice, Item),
    price(Item, Price),
    write('Enter quantity: '),
    read(Qty),
    assert(order(Item, Qty, Price)),
    take_order.

print_orders :-
    nl, write('------ ORDER DETAILS ------'), nl,
    order(Item, Qty, Price),
    Sub is Qty * Price,

    write('Item: '), write(Item), nl,
    write('Price: '), write(Price), nl,
    write('Quantity: '), write(Qty), nl,
    write('Subtotal: '), write(Sub), nl,
    write('-------------------------'), nl,

    fail.
print_orders.


calculate_total(Total) :-
    findall(Sub, (order(_, Q, P), Sub is Q*P), List),
    sum_list(List, Total).


final_bill :-
    print_orders,
    calculate_total(Total),
    nl,
    write('TOTAL AMOUNT = '), write(Total), nl.


start :-
    set_prices,
    show_menu,
    take_order,
    final_bill.
