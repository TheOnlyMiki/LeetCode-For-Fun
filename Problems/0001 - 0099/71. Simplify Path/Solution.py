class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Option 2
        valid = []

        for name in path.split('/'):
            # ../  ./  //  Cases
            if name == "" or name == ".":
                continue
            elif name == "..":
                if valid:
                    valid.pop()
            # Other case
            else:
                valid.append(name)

        return '/' + '/'.join(valid)

        # Option 1 - too slow
        """
        if path[-1] != '/':
            path += '/'

        stack_path = []
        stack_subpath = ['/']
        last = None
        c = None
        name = None

        for i in range(1, len(path)):
            c = path[i]
            last = stack_subpath[-1]
            name = ""

            if c == '/':
                while last != '/':
                    name += last
                    stack_subpath.pop()
                    last = stack_subpath[-1]

                if name == "..":
                    if len(stack_path) != 0 and stack_path[-1] != "":
                        stack_path.pop()
                elif name == "." or name == "":
                    continue
                else:
                    stack_path.append(name[::-1])
            else:
                stack_subpath.append(c)

        return '/' + '/'.join(stack_path)
        """
