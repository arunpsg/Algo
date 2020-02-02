**Request Routing in a Web Server with a Trie:**

This problem is about a Trie with handler.
Input path string has been parsed by splitting on "/".

Time complexity of Trie in worst case is O(n), where n is the number of path parts

Space Complexity:
O(n) where n is the number of children of root
Auxillary space:
For Insert, an array is used to store the path parts need to be considered.
Which is again O(n) where n is the number of path parts 