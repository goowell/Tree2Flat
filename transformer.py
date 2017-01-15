
def _get_value_from_dict(data, keys):
    v = data
    for k in keys:
        v = v.get(k)
        if v is None:
            break
    return v

def _list_mapping(source, mapping):
    flat_list = []
    for l in source:
        flat_list.append(dict_mapping(l, mapping))
    return flat_list

def dict_mapping(source, mapping):
    flat_dict = {}
    for m in mapping:
        if len(m) == 2:            
            v = _get_value_from_dict(source,m[0])
        elif len(m) == 3:
            v = _list_mapping(_get_value_from_dict(source,m[0]), m[2])
        else:
            v = None
            print('invalid mapping rule: %' % m)
        if v is None:
            continue
        flat_dict.update({m[1]:v})
    return flat_dict

def main():
    print(dict_mapping(in_data, mapping))


if __name__ == '__main__':
    import sys
    from data import mapping, in_data
    sys.exit(int(main() or 0))