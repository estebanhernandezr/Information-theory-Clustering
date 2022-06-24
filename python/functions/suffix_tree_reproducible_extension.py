def reproducible_extension(STD, s, lim=None, limsup=None):
    v = STD.root
    i = 0
    l = 0
    while i < len(s):
        if v.has_transition(s[i]):
            if lim is not None and v.transition_links[s[i]].new_idx < lim:
                return

            if limsup is not None and v.transition_links[s[i]].idx >= limsup:
                return (v.idx, l)

            label = STD.edgeLabel(v.transition_links[s[i]], v)
            idx = 0
            while i+idx < len(s) and idx < len(label):
                if s[i+idx] == label[idx]:
                    idx += 1
                    l += 1
                else:
                    if lim is not None:
                        return (v.transition_links[s[i]].new_idx, l)
                    else:
                        return (v.transition_links[s[i]].idx, l)

            v = v.transition_links[s[i]]
            i += idx
        else:
            if lim is not None:
                return (v.new_idx, l)
            else:
                return (v.idx, l)

    if lim is not None:
        return (v.new_idx, l)
    else:
        return (v.idx, l)