#include <algorithm>
#include <iterator>
#include <string>
#include <vector>

#include "test_framework/test_utils_serialization_traits.h"

using std::string;
using std::vector;

struct Name {
  bool operator<(const Name& that) const {
    return first_name != that.first_name ? first_name < that.first_name
                                         : last_name < that.last_name;
  }

  string first_name, last_name;
};

void EliminateDuplicate(vector<Name>* A) {
  // Implement this placeholder.
  return;
}

template <>
struct SerializationTraits<Name>
    : UserSerTraits<Name, std::string, std::string> {};

std::ostream& operator<<(std::ostream& out, const Name& n) {
  return out << n.first_name;
}

vector<Name> EliminateDuplicateWrapper(vector<Name> data) {
  EliminateDuplicate(&data);
  return data;
}

bool Comp(vector<std::string> expected, vector<Name> result) {
  std::sort(begin(expected), end(expected));
  std::sort(begin(result), end(result));
  return std::equal(
      begin(expected), end(expected), begin(result), end(result),
      [](const std::string& s, const Name& n) { return s == n.first_name; });
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  generic_test_main(argc, argv, "remove_duplicates.tsv",
                    &EliminateDuplicateWrapper, &Comp);
  return 0;
}
