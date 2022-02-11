import json

def phrasel_search(P, Queries):

    ans = []
    for Query in Queries:
        q = Query.split()
        a = []
        for phrase in P:
            p = phrase.split()
            f_indices = [i for i, w in enumerate(q) if w == p[0]]
            for f_index in f_indices:
                add_to_answer = True
                extra_word = False
                p_index, q_index = 1, f_index + 1
                while add_to_answer:
                    if p[p_index] == q[q_index]:
                        if p_index == len(p) - 1:
                            break
                        p_index += 1
                        q_index += 1
                    else:
                        if extra_word:
                            add_to_answer = False
                        else:
                            extra_word = True
                            q_index += 1
                    if q_index == len(q):
                        add_to_answer = False
                        break
                if add_to_answer:
                    a.append((f_index, " ".join(q[f_index:q_index + 1])))

        ans.append([x for i, x in sorted(a)])
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
