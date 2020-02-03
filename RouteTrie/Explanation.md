**Request Routing in a Web Server with a Trie:**

This problem is about a Trie with handler.
Input path string has been parsed by splitting on "/".
Router class includes the trie and the trie nodes, 
add_handler function uses the helper to split the path by '/'
insert - iteratively sets the trie along with the handler, 
lookup - uses the split_path function and the find function to iteratively look inside the nested tries for that part of the path. 
split_path - helper function uses String splitting to gather the parts after splitting

Time complexity of Trie in worst case is O(n), where n is the number of path parts

Space Complexity:
O(n) where n is the number of children of root
Auxillary space:
For Insert, an array is used to store the path parts need to be considered.
Which is again O(n) where n is the number of path parts 