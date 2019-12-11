/*

To compile:
    g++ -Wall -Wextra -Werror gini.cpp
*/

#include <iostream>
#include <cmath>

template<typename Iter>
double gini(Iter first, Iter last) {
    /* Compute Gini index of array x.
    */

    int n = 0;
    double num = 0;
    double den = 0;
    for (auto it = first; it != last; ++it) {
        for (auto ti = first; ti != it; ++ti) {
            num += abs(*it - *ti)*2;
        }
        n += 1;
        den += *it;
    }
    den *= 2*n;

    return num/den;

}

int main() {
    double arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
    std::cout << gini(&arr[0], &arr[13]) << '\n';
}
