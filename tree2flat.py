
def _get_value_from_dict(data, keys):
    v = data
    for k in keys:
        v = v.get(k)
        if v is None:
            break
    return v


def _list_mapping(tree_list, mapping_rule):
    flat_list = []
    for l in tree_list:
        flat_list.append(tree_to_flat(l, mapping_rule))
    return flat_list


def tree_to_flat(tree_dict, mapping_rule):
    '''x'''
    flat_dict = {}
    for m in mapping_rule:
        if len(m) == 2:
            v = _get_value_from_dict(tree_dict, m[0])
        elif len(m) == 3:
            v = _list_mapping(_get_value_from_dict(tree_dict, m[0]), m[2])
        else:
            v = None
            print('invalid mapping rule:', m)
        if v is None:
            continue
        flat_dict.update({m[1]: v})
    return flat_dict


def main():
    '''demo'''

    # print(tree_to_flat(in_data, mapping))
    print(tree_to_flat(in_data, [(1,2,3,4)]))


if __name__ == '__main__':
    import sys
    from data import mapping, in_data

    sys.exit(int(main() or 0))
