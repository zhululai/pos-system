# POS System
Our supermarket sells three items, each of which has a stock-keeping code and a price. Multibuy offers are applicable to some items. Your objective is to implement the logic behind a Point of Sale (POS) system for our supermarket using the Python programming language.

## Inventory
| **Item** | **Code** | **Offer**                  |
| -------- | -------- | -------------------------- |
| Apple    | A        | Three for the price of two |
| Banana   | B        | Three for £1               |
| Pear     | P        | None                       |

## Tasks
- Create a source file containing a function named `checkout` that takes a list of item codes and their current prices and returns the total price in pence, after applying any relevant offers. For example `checkout(['B', 'A', 'B', 'P', 'B'], {'A': 25, 'B': 40, 'P': 30})` should return `155`.
- Create a second source file containing code to verify the behaviour of your `checkout` function.
- [Optional] Add an object type `Checkout` to your first source file that can instantiated with the current prices, for example `Checkout({'A': 25, 'B': 40, 'P': 30})`. It should provide two methods: `scan(code)` and `total()`. The latter should be callable at any time to obtain a correct total for the items scanned so far. Add test(s) for `Checkout` to your second source file.
