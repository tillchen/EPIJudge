#include <string>
#include <vector>

using std::string;
using std::vector;

int LevenshteinDistance(const string& A, const string& B) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  generic_test_main(argc, argv, "levenshtein_distance.tsv",
                    &LevenshteinDistance);
  return 0;
}
