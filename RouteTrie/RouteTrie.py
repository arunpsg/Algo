# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, route_handler, error_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(route_handler)
        self.error_handler = error_handler

    def insert(self, path, handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for part in path:
            if part:
                # print("RouteTrie insert path : ", path)
                # node.insert(path, self.error_handler)
                node.children[part] = RouteTrieNode()
                node = node.children[part]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        # print("find path : ", path)
        for path_node in path:
            # print("path_node : ", path_node)
            # for key in node.children.keys():
            #     print("node.children.keys : ", key)
            if path_node and path_node in node.children.keys():
                # print("node : ", node.children[path_node])
                # print("path_node : ", path_node)
                node = node.children[path_node]
                if node.handler is None:
                    node.handler = "not found handler"
                    # print("not node node.handler : ", node.handler)
            else:
                node.handler = self.error_handler
                # print("node.handler : ", node.handler)
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler = None):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, error_handler):

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler, error_handler)

    def add_handler(self, path, handler):

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.trie.insert(path_parts, handler)

    def lookup(self, path):

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        if path is "":
            return self.trie.error_handler
        elif path == "/":
            return self.trie.root.handler
        path_parts = self.split_path(path)

        if path_parts[len(path_parts)-1] == '':
            path_parts.pop(len(path_parts)-1)

        return self.trie.find(path_parts)

    def split_path(self, path):
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    #     print("path : ", path)
    #     print("[item for item in path.split()] : ", [item for item in path.split("/")])
        return [item for item in path.split("/")]
    pass
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(""))  # should print 'not found handler'