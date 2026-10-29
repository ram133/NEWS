import json

def add_emails(new_emails, json_path="subscribers.json"):
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"subscribers": []}

    subs = set(data.get("subscribers", []))
    subs.update([e.strip().lower() for e in new_emails])

    data["subscribers"] = sorted(list(subs))

    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully added emails. Total subscribers: {len(data['subscribers'])}")

if __name__ == "__main__":
    my_emails = ["crh2509@icloud.com", "3659745@gmail.com"]
    add_emails(my_emails)
