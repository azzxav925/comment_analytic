import time
from comments import categorised_comments, final_categorised_comments
from ai import create_thread, create_message, run_thread, get_response, retrieve_run
import json

with open('comments.json', 'r', encoding='utf-8') as file:
    comments = json.load(file)

gpt_comments = [{"message_id": comment["message_id"], "comment": comment["comment"]} for comment in comments]

for i in range(0, len(comments), 20):
    try:
        thread = create_thread()
        batch = gpt_comments[i:i + 20]
        create_message(thread.id, f"{batch}")
        run = run_thread(thread.id)
        run_id = run.id
        status = retrieve_run(thread.id, run_id).status
        while not status == "completed":
            time.sleep(1)
            status = retrieve_run(thread.id, run_id).status
        string_comment = get_response(thread.id)[0][0].text.value
        categorised_comment = json.loads(string_comment)
        for j in range(len(categorised_comment)):
            categorised_comments[j]["number"] += categorised_comment[j]["number"]
            for f in range(len(categorised_comment[j]["comment_ids"])):
                categorised_comments[j]["comment_ids"].append(categorised_comment[j]["comment_ids"][f])
    except:
        pass


positive_ids = categorised_comments[0]["comment_ids"]
negative_ids = categorised_comments[1]["comment_ids"]
questions_ids = categorised_comments[2]["comment_ids"]
advice_ids = categorised_comments[3]["comment_ids"]
assistance_ids = categorised_comments[4]["comment_ids"]
general_ids = categorised_comments[5]["comment_ids"]
issues_ids = categorised_comments[6]["comment_ids"]
acknowledgements_ids = categorised_comments[7]["comment_ids"]


for j in range(len(comments)):
    if comments[j]["message_id"] in positive_ids:
        final_categorised_comments[0]["number"] = categorised_comments[0]["number"]
        final_categorised_comments[0]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in negative_ids:
        final_categorised_comments[1]["number"] = categorised_comments[1]["number"]
        final_categorised_comments[1]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in questions_ids:
        final_categorised_comments[2]["number"] = categorised_comments[2]["number"]
        final_categorised_comments[2]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in advice_ids:
        final_categorised_comments[3]["number"] = categorised_comments[3]["number"]
        final_categorised_comments[3]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in assistance_ids:
        final_categorised_comments[4]["number"] = categorised_comments[4]["number"]
        final_categorised_comments[4]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in general_ids:
        final_categorised_comments[5]["number"] = categorised_comments[5]["number"]
        final_categorised_comments[5]["comments"].append(comments[j]["comment"])
    elif comments[j]["message_id"] in issues_ids:
        final_categorised_comments[6]["number"] = categorised_comments[6]["number"]
        final_categorised_comments[6]["comments"].append(comments[j]["comment"])
    else:
        final_categorised_comments[7]["number"] = categorised_comments[7]["number"]
        final_categorised_comments[7]["comments"].append(comments[j]["comment"])

with open('categorised_comments.json', 'w', encoding='utf-8') as f:
    json.dump(final_categorised_comments, f, ensure_ascii=False, indent=4)

print(categorised_comments)
