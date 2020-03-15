# Algorithms
Problems & Algorithms

A collection of algorithms which i have practiced and used for problem solving.
# AutoComplete :
    Implementation of Automcomplete feature using Trie
    
# Dutch National Flag:
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. We're not allowed to use any sorting           function that Python provides.

    Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n)              solution but it will not count as single traversal.
    
# Rearrange Digits:
    Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. We can assume that all     array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. We're not                 allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

    for e.g. [1, 2, 3, 4, 5]

    The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more        than one possible answers, return any one. 
    
# Search in a Rotated Sorted Array:
    Given a sorted array which is rotated at some random pivot point.
    Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

    Given a target value to search. If found in the array return its index, otherwise return -1.
    Lets assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

    Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
 
 # Finding the Square Root of an Integer:
    Find the square root of the integer without using any Python library. We have to find the floor value of the square root.
    For example if the given number is 16, then the answer would be 4.

    If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
    The expected time complexity is O(log(n))

# Max and Min in a Unsorted Array
    In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time.       Do not use Python's inbuilt functions to find min and max.

    Bonus Challenge: Is it possible to find the max and min in a single traversal?
    
# HTTPRouter using a Trie
    We are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned            previously.

    There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an       excellent and very efficient data structure for this purpose.

   The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out        what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
    First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will       contain a part of the http path at each node, building from the root node /

    In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass      an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the    sake of simplicity we will just use a string that we can print out to ensure we got the right handler

    We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large     number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the       parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

    (root, None) -> ("about", None) -> ("me", "About Me handler")

    We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really       just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

