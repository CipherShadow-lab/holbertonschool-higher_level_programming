#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")


    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return
    
    data = response.json()
    filtered_posts = []

    for post in data:
        filtered_post = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        filtered_posts.append(filtered_post)
    
    with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()

        for post in filtered_posts:
            writer.writerow(post)
