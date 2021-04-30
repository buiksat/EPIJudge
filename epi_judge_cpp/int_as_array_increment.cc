#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
vector<int> PlusOne(vector<int> A) {
    size_t n = A.size();
    long i = n - 1;
    size_t current = 0;
    while (i >= 0){
        if (A[i] + 1 < 10){
            A[i] = A[i] + 1;
            current = 0;
            break;
        } else {
            current = 1;
            A[i] = 0;
            i--;
        }
    }
    if (current == 1){
        A[0] = 1;
        A.emplace_back(0);
    }
    return A;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  return GenericTestMain(args, "int_as_array_increment.cc",
                         "int_as_array_increment.tsv", &PlusOne,
                         DefaultComparator{}, param_names);
}
