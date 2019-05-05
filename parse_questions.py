import json
questions = []
with open("sorular.txt", encoding='utf-8') as inf:
    all_lines = inf.readlines()
    counter = 0
    for i in range (0, len(all_lines), 5):
        print(f"Counter: {counter}, i: {i}")
        question = all_lines[i].strip()
        answers = []
        a_cnt = 0
        for line in all_lines[i+1:i+4]:
            a_cnt += 1
            answers.append(line.strip())
        q_id = counter + 1
        questions.append({'text': question, 'answers': answers, 'id': q_id})
        counter += 1
with open("sorular.json", "w+", encoding='utf-8') as outf:
    json.dump({'questions':questions}, outf, ensure_ascii=False, indent=4)