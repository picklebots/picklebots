
def inList(in_lst, search_lst):
    
    '''
    To test if an item or one of the items in a list are present inside another list.
    can be used in when conditions
    '''

    if type(in_lst) is list:
        for i in in_lst:
            if i in search_lst:
                return True
        return False
    else:
        if in_lst in search_lst:
            return True
        else:
            return False


class FilterModule (object):

    def filters(self):
        return {"inList": inList}
