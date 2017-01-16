
def _get_value_from_dict(data, keys):
    v = data
    for k in keys:
        v = v.get(k)
        if v is None:
            print('invalid keys: ' + str(keys))
            break
    return v


def _list_mapping(tree_list, mapping_rule):
    flat_list = []
    for l in tree_list:
        flat_list.append(tree_to_flat(l, mapping_rule))
    return flat_list

def _is_valid_rule(rule):
    if not isinstance(rule, list):
        return False
    for m in rule:
        if not isinstance(m, tuple):
            return False
        if not isinstance(m[0], list):
            return False
        if not (len(m) == 2 or len(m) == 3):
            return False
        if len(m) == 3 and not _is_valid_rule(m[2]):
            return False
    return True


def tree_to_flat(tree_dict, mapping_rule):
    '''x'''

    flat_dict = {}
    if not _is_valid_rule(mapping_rule):
        print('invalid mapping rule')
        return flat_dict

    for m in mapping_rule:
        if len(m) == 2:
            v = _get_value_from_dict(tree_dict, m[0])
        elif len(m) == 3:
            v = _list_mapping(_get_value_from_dict(tree_dict, m[0]), m[2])
        else:
            v = None
            print('invalid mapping rule:' + str(m))
        if v is None:
            continue
        flat_dict.update({m[1]: v})
    return flat_dict


def main():
    '''demo'''

    invalid_rule = [(['1'], '2'), (1, 2, 3), (1, 2, 3, 4)]
    # mapping.extend(invalid_rule)
    print(mapping)
    print(tree_to_flat(in_data, mapping))


if __name__ == '__main__':
    import sys
    from data import mapping, in_data

    sys.exit(int(main() or 0))
