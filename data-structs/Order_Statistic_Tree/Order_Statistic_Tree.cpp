#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>

// order_of_key(k) : Number of items strictly smaller than k .
// find_by_order(k) : K-th element in a set (counting from zero). //This is what you need 