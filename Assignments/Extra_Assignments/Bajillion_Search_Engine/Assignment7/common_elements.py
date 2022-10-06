"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    """
    Logic:
    1. Creating 2 dictionaries, d1 and d2 that will store the elements in list1 and list2.
    2. Dictionaries are used here because the iteration takes O(1) time to search an element, unlike O(n) for lists.
    3. The first two for loops add elements to the dict. from respective lists.
    4. The third for loop searches for common elements in both the dicts, ie both the lists as dicts are made from lists.
    5. The run-time complexity for the code is O(max(n, m)), where n is len(list1) and m is len(list2). It is indirectly
    a O(n) complexity function.
    """
    d1, d2 = dict(), dict()
    for i in list1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    for i in list2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    ans = list()  # Contains list of common elements.
    for i in d1:
        if i in d2:
            ans.append(i)

    return ans

def main():
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
